import numpy as np
import cv2
import tensorflow as tf
import streamlit as st
from PIL import Image
from streamlit_webrtc import VideoProcessorBase,RTCConfiguration,WebRtcMode,webrtc_streamer


with st.echo(code_location="below"):
    haar_cascade = cv2.CascadeClassifier("haar_faces.xml")
    
    class VideoProcessor(VideoProcessorBase):
        def __init__(self):
            self.i = 0
        def transform(self,frame):
            image = frame.to_ndarray(format="bgr24")
            gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            faces = haar_cascade.detectMultiScale(gray,1.3,5)
            for (x,y,w,h) in faces:
                cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),thickness=2)
            return image 
    
    def pil_to_cv2_image(image):
        opencv_array = np.array(image)
        cv2.imwrite('out.jpg', cv2.cvtColor(opencv_array, cv2.COLOR_RGB2BGR))
        opencv_image = cv2.imread('out.jpg')
        return opencv_image
    
    def detect_image(image):
        img = pil_to_cv2_image(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces_roi = haar_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3)
        i += self.i + 1
        for (x, y, w, h) in faces_roi:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        return img
    
    def welcome():
        st.title('Detection et classifiction des images en utilisant streamlit')
        st.subheader('Une appication simple qui vout permet de choisir entre trois options dispobible au niveau du sidebar')

    def image_detection():
        st.header("Face Detection using haarcascade")
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
        image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'], key=0)
        if image_file is not None:
            our_image = Image.open(image_file)
            st.text("Original Image")
            st.image(our_image)
        if st.button("Detect", key=20):
            result_image = detect_image(our_image)
            st.text("Results")
            st.image(result_image)

    def live_detection():
        st.header("Détection De Visage En Direct")
        html_temp = """
            <body>
            <div style="padding:15px;text-align:center;margin:25px;">
            <h4 style = "color:black;text-align:center;">Utilisation De La Webcam</h4>
            </div>
            </body>
            """
        st.markdown(html_temp, unsafe_allow_html=True)
        RTC_CONFIGURATION = RTCConfiguration({"iceServers":[{"urls": ["stun:stun.l.google.com:19302"]}]})
        webrtc_streamer(key="face_detection",video_processor_factory=VideoProcessor,mode=WebRtcMode.SENDRECV,rtc_configuration=RTC_CONFIGURATION)
        
    def simpsons_recognition():
        @st.cache(allow_output_mutation=True)
        def load_model():
            model = tf.keras.models.load_model("model.h5")
            return model
        model = load_model()
        class_names = ['bart_simpson', 'charles_montgomery_burns', 'homer_simpson', 'krusty_the_clown',
                   'lisa_simpson', 'marge_simpson', 'milhouse_van_houten', 'moe_szyslak', 'ned_flanders',
                   'principal_skinner']
        st.header("Face Recognition using a built deep learning model")
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
            
    selected_box = st.sidebar.selectbox(
            'Choisissez une des options suivantes',
            ('Bienvenue', 'Detection en direct', 'Detection sur une image uploadée',
         'Reconnaissance des personnages de Simpsons'))     
    if selected_box == 'Bienvenue':
        welcome()
    if selected_box == 'Detection en direct':
        live_detection()
    if selected_box == 'Detection sur une image uploadée':
        image_detection()
    if selected_box == 'Reconnaissance des personnages de Simpsons':
        simspons_recognition()
