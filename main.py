import numpy as np
import os
import cv2
import caer
import keras_tuner
from keras_tuner import *
from sklearn.utils import shuffle
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers,models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import streamlit as st
from PIL import Image
import dlib
from imutils import face_utils

IMG_SIZE = (80,80)
char_path = r"C:/Users/Massamba Sene/PycharmProjects/Arendre/simpsons_characters_dataset/simpsons_dataset"
char_dict = {}
for char in os.listdir(char_path):
  char_dict[char] = len(os.listdir(os.path.join(char_path,char)))
char_dict = caer.sort_dict(char_dict, descending=True)
characters = []
count = 0
for item in char_dict:
  characters.append(item[0])
  count += 1
  if count >= 10:
      break
def create_dataset(img_folder,characters):
  img_data_array=[]
  class_name=[]
  for person in os.listdir(img_folder):
    if person in characters:
      for image in os.listdir(os.path.join(img_folder, person)):
        image_path= os.path.join(img_folder, person,  image)
        image= cv2.imread( image_path, cv2.COLOR_BGR2RGB)
        image=cv2.resize(image, IMG_SIZE,interpolation = cv2.INTER_AREA)
        image=np.array(image)
        image = image.astype('float32')
        image /= 255
        img_data_array.append(image)
        class_name.append(person)
  return img_data_array, class_name
img_data,class_name = create_dataset(r"C:/Users/Massamba Sene/PycharmProjects/Arendre/simpsons_characters_dataset/simpsons_dataset"
                                     ,characters=characters)
target_dict = {k: v for v, k in enumerate(np.unique(class_name))}
target_val=  [target_dict[class_name[i]] for i in range(len(class_name))]

#On met en place une fonction chargée de créer le modèle
def build_model(hp):
    model = keras.Sequential()
    model.add(layers.Conv2D(hp.Int("filters_1",32,128,step=32,default=96),
                            kernel_size=(3, 3),
                            activation='relu',
                            input_shape=(80, 80, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(hp.Int("filters_2",64,256,step=64,default=192),
                            kernel_size = (3, 3),
                            activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(hp.Int("filters_3",64,256,step=64,default=256),
                            kernel_size = (3, 3),
                            activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(units=hp.Int("units",64,128,step=32,default=128),
                            activation='relu'))
    model.add(layers.Dense(10,activation="softmax"))
    model.compile(
    optimizer = "rmsprop",
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics = ["accuracy"],
    )
    return model

tuner = RandomSearch(
        build_model,
        objective = "val_accuracy",
        max_trials = 5,
        executions_per_trial = 1,
        overwrite = True,
        directory = "my_dir",
        project_name = "hello_world",
)

x = np.array(img_data,dtype="float32")
y = np.array(list(map(int,target_val)),np.float32)
train_data,train_labels = shuffle(x,y,random_state=0)
x_train = train_data[:11049]
y_train = train_labels[:11049]
x_val =  train_data[11049:]
y_val = train_labels[11049:]
train_datagen = ImageDataGenerator(
            rotation_range = 10,
            width_shift_range = .1,
            height_shift_range = .1,
            shear_range = 0.3,
            zoom_range = 0.3,
            horizontal_flip = True,
            fill_mode = 'nearest',
)
val_datagen = ImageDataGenerator()
train_set = train_datagen.flow(x_train,y_train,batch_size=32)
val_set = val_datagen.flow(x_val,y_val,batch_size=32)

tuner.search(
    train_set,
    validation_data=val_set,
    epochs=5,
    callbacks=[keras.callbacks.TensorBoard("/tmp/logs_dir")]
)

models = tuner.get_best_models(num_models=1)
model = models[0]
history = model.fit_generator(train_set,
                              validation_data = val_set,
                              verbose=2,
                              epochs=5)

x_test,y_test = create_dataset(r"C:/Users/Massamba Sene/PycharmProjects/Arendre/simpsons_characters_dataset/kaggle_simpson_testset/kaggle_simpson_testset",
                               characters=characters)
target_dict = {k: v for v, k in enumerate(np.unique(y_test))}
target_val = [target_dict[y_test[i]] for i in range(len(y_test))]
x_test = np.array(x_test,np.float32)
y_test = np.array(list(map(int,target_val)),np.float32)

test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(test_acc)

model.save("C:/Users/Massamba Sene/Deep_learning/model.hdf5")


def main():
  @st.cache(allow_output_mutation=True)
  def load_model():
    model = tf.keras.models.load_model('/content/model.hdf5')
    return model
  model = load_model()
  class_names = ['bart_simpson', 'charles_montgomery_burns', 'homer_simpson', 'krusty_the_clown',
                 'lisa_simpson', 'marge_simpson', 'milhouse_van_houten', 'moe_szyslak', 'ned_flanders',
                 'principal_skinner']
  def detect_dlib(our_image):
    img = np.array(our_image.convert("RGB"))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_detector = dlib.get_frontal_face_detector()
    rects = face_detector(gray, 2)
    for (i, rect) in enumerate(rects):
      (x, y, w, h) = face_utils.rect_to_bb(rect)
      img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
    return img
  face_detector = st.container()
  face_recognizer = st.container()
  with face_detector:
    st.title("Face Detection And Recognition WebApp")
    st.text("This face detector was built using the dlib library")
    html_body = """<body style="background-color:red;"></body>"""
    st.markdown(html_body,unsafe_allow_html=True)
    html_temp = """
      <body style="background-color:red;">
      <div style="background-color:red;padding:10px;">
      <h2 style="color:white;text-align:center;">Face Detection</h2>
      </div>
      </body>
      """
    st.markdown(html_temp,unsafe_allow_html=True)
    image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg'],key=0)
    if image_file is not None:
      our_image = Image.open(image_file)
      st.text("Original Image")
      st.image(our_image)
    if st.button("Detect"):
      result_image = detect_dlib(our_image)
      st.text("Results")
      st.image(result_image)
  with face_recognizer:
    st.title("Face Recognition")
    st.text("This face recognizer is used to distinguish between simpsons characters")
    html_body = """<body style="background-color:red;"></body>"""
    st.markdown(html_body,unsafe_allow_html=True)
    html_temp = """
      <body style="background-color:red;">
      <div style="background-color:red;padding:10px;">
      <h2 style="color:white;text-align:center;">Simpsons Face Recognition</h2>
      </div>
      </body>
      """
    st.markdown(html_temp,unsafe_allow_html=True)
    image_file_2 = st.file_uploader("Upload Image",type=['jpg','png','jpeg'],key=1)
    if image_file_2 is not None:
      our_image_1 = Image.open(image_file_2)
      st.text("Original Image")
      st.image(our_image_1)
    if st.button("Recognise"):
      our_image_1= our_image_1.resize((80,80))
      our_image_1 = np.expand_dims(our_image_1,axis=0)
      our_image_1 = np.array(our_image_1)
      our_image_1 = our_image_1.astype("float32")
      our_image_1/= 255
      our_image_1 = np.array(our_image_1,dtype='float32')
      result = class_names[np.argmax(model.predict(our_image_1,1))]
      st.text("Results")
      st.text(result)
  pass
if __name__ == 'main':
  main()