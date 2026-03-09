import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # Suppresses TensorFlow warnings for cleaner output
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


# App Config Text shown on browser tab

st.set_page_config(
    page_title="Pneumonia Detection",
    page_icon="🫁",
    layout="centered"
)

# App Heading & Description
st.title("🫁 Pneumonia Detection from Chest X-ray")
st.write("Upload a chest X-ray image to predict **NORMAL** or **PNEUMONIA**.")

# Model Loading
@st.cache_resource      # Loads the trained CNN model & Caches it so it loads only once--> no need every time
def load_model():       # Internal load function
    return tf.keras.models.load_model("best_pneumonia_model3.keras")

model = load_model()

# Class Names & Threshold
CLASS_NAMES = ["NORMAL", "PNEUMONIA"]       # Maps output → human-readable labels
THRESHOLD = 0.5                             # Controls decision sensitivity

# Image Preprocessing

def preprocess_image(image):
    image = image.convert("RGB")                   # Ensures 3 channels (some X-rays are grayscale)
    image = image.resize((224, 224))               # Must match CNN input size
    img_array = np.array(image) / 255.0            # Normalizes pixels (0–1)
    img_array = np.expand_dims(img_array, axis=0)  # Shape becomes (1, 224, 224, 3)
    return img_array


# File Upload

uploaded_file = st.file_uploader(                  # Creates upload button
    "Upload Chest X-ray Image",             
    type=["jpg", "jpeg", "png"]                    # Restricts file types
)

# Check if File Uploaded
if uploaded_file is not None:                     # Code runs only after image upload to Prevents null errors
    image = Image.open(uploaded_file)             # Reads image using PIL for user conformation

    st.image(image, caption="Uploaded X-ray", width=600)

    # Predict Button
    if st.button("Predict"):                      # Prevents auto prediction
        with st.spinner("Analyzing X-ray..."):    # Shows loading animation
            processed_image = preprocess_image(image)       # Image → tensor
            prediction = model.predict(processed_image)[0][0]  # CNN outputs probability (float)

            predicted_class = (                   # Converts probability → class label
               "PNEUMONIA" if prediction >= THRESHOLD else "NORMAL"
            )
            #Shows meaningful confidence %
            confidence = prediction if predicted_class == "PNEUMONIA" else 1 - prediction

        # Display Results
        st.subheader("Prediction Result")
        st.success(f"**Prediction:** {predicted_class}")
        st.info(f"**Confidence:** {confidence * 100:.2f}%")

        st.markdown("---")
        st.caption(
            "⚠️ This tool is for educational purposes only and not a medical diagnosis."
        )    