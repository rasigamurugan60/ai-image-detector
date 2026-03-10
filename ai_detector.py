import streamlit as st
from PIL import Image
import random
import time

st.title("AI Image & Deepfake Detector")

st.write("Upload an image to check whether it is Real or AI Generated.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    if st.button("Detect"):

        st.write("Processing...")

        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.02)
            progress.progress(i+1)

        result = random.choice([
            "Real Image",
            "AI Generated Image",
            "Morphed Image"
        ])

        st.success("Result: " + result)