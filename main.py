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

def main():
    @st.cache(allow_output_mutation=True)
    def load_model():
        model = tf.keras.models.load_model(r"C:/Users/Massamba Sene/Deep_learning/model.h5")
        return model
    model = load_model()
    class_names = ['bart_simpson', 'charles_montgomery_burns', 'homer_simpson', 'krusty_the_clown',
                 'lisa_simpson', 'marge_simpson', 'milhouse_van_houten', 'moe_szyslak', 'ned_flanders',
                 'principal_skinner']
    def pil_to_cv2_image(image):
        opencv_array = np.array(image)
        cv2.imwrite('out.jpg', cv2.cvtColor(opencv_array, cv2.COLOR_RGB2BGR))
        opencv_image = cv2.imread('out.jpg')
        return opencv_image

    def detect_image(image):
        img = pil_to_cv2_image(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces_roi = haar_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3)
        for (x, y, w, h) in faces_roi:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        return img
    face_detector = st.container()
    face_recognizer = st.container()

    def detect_live():
        image = cv2.VideoCapture(0)
        haar_cascade = cv2.CascadeClassifier("haar_face.xml")
        while True:
            isTrue, frame = image.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces_roi = haar_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3)
            for (x, y, w, h) in faces_roi:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)
                cv2.imshow("Frames", frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        image.release()
        cv2.destroyAllWindows()


    with face_detector:
        st.title("Face Detection And Recognition WebApp")
        st.text("This face detector was built using the dlib library")
        html_body = """<body style="background-color:red;"></body>"""
        st.markdown(html_body, unsafe_allow_html=True)
        html_temp = """
            <body style="background-color:red;">
            <div style="background-color:red;padding:10px;">
            <h2 style="color:white;text-align:center;">Face Detection</h2>
            </div>
            </body>
            """
        st.markdown(html_temp, unsafe_allow_html=True)
        html_temp = """
            <body>
            <div style="padding:15px;text-align:center;margin: 25px;">
            <h4 style = "color:black;text-align:cznter;">Detect Using uploaded Image</h4>
            </div>
            </body>
            """
        st.markdown(html_temp, unsafe_allow_html=True)
        image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'], key=0)
        if image_file is not None:
            our_image = Image.open(image_file)
            st.text("Original Image")
            st.image(our_image)
        if st.button("Detect", key=20):
            result_image = detect_image(our_image)
            st.text("Results")
            st.image(result_image)
        html_temp = """
            <body>
            <div style="padding:15px;text-align:center;margin:25px;">
            <h4 style = "color:black;text-align:center;"> Detect Using Webcam</h4>
            </div>
            </body>
            """
        st.markdown(html_temp, unsafe_allow_html=True)
        if st.button("Detect", key=10):
            detect_live()

    with face_recognizer:
        st.title("Face Recognition")
        st.text("This face recognizer is used to distinguish between simpsons characters")
        html_body = """<body style="background-color:red;"></body>"""
        st.markdown(html_body, unsafe_allow_html=True)
        html_temp = """
            <body style="background-color:red;">
            <div style="background-color:red;padding:10px;">
            <h2 style="color:white;text-align:center;">Simpsons Face Recognition</h2>
            </div>
            </body>
            """
        st.markdown(html_temp, unsafe_allow_html=True)
        image_file_2 = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'], key=1)
        if image_file_2 is not None:
            our_image_1 = Image.open(image_file_2)
            st.text("Original Image")
            st.image(our_image_1)
        if st.button("Recognise"):
            if image_file_2 is not None:
                opencv_image = pil_to_cv2_image(our_image_1)
                opencv_image = cv2.resize(opencv_image, (80, 80), interpolation=cv2.INTER_AREA)
                opencv_image = np.array(opencv_image)
                opencv_image = opencv_image.astype('float32')
                opencv_image = np.expand_dims(opencv_image, axis=0)
                opencv_image /= 255
                result = class_names[np.argmax(model.predict(opencv_image))]
                st.text("Results")
                st.text("Ce personnage est " + result)
    if __name__ == 'main':
        main()
