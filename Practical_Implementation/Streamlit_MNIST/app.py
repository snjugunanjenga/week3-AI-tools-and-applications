import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model (use .h5 for compatibility)
model = tf.keras.models.load_model('mnist_cnn.keras')  # Update path if needed
st.title("MNIST Digit Classifier")
uploaded_file = st.file_uploader("Upload a digit image", type=["png", "jpg"])
if uploaded_file:
    img = Image.open(uploaded_file).convert('L').resize((28, 28))
    img = np.array(img) / 255.0
    img = img.reshape(1, 28, 28, 1)
    pred = model.predict(img)
    st.write(f"Predicted Digit: {np.argmax(pred)}")