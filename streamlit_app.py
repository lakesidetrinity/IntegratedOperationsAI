import streamlit as st
import easyocr
from PIL import Image
import numpy as np

st.set_page_config(page_title="Integrated Operations AI", layout="wide")

st.title("Wisconsin Home Care AI App")

st.header("Upload Scanned Document (Image Format Recommended)")

uploaded_file = st.file_uploader(
    "Upload scanned document (JPG or PNG)",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    st.info("Running OCR... Please wait.")

    image = Image.open(uploaded_file)
    image_np = np.array(image)

    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(image_np, detail=0)

    extracted_text = " ".join(result)

    st.success("OCR Complete")
    st.text_area("Extracted Text Preview", extracted_text, height=300)

    st.header("Generated Draft Care Plan")

    if "mobility" in extracted_text.lower():
        st.write("• Assist with mobility and transfers as needed.")
    if "diabetes" in extracted_text.lower():
        st.write("• Monitor blood glucose and assist with diabetic care.")
    if "dementia" in extracted_text.lower():
        st.write("• Provide cognitive support and supervision for safety.")
    if "fall" in extracted_text.lower():
        st.write("• Implement fall prevention interventions.")