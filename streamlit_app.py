import streamlit as st
import easyocr
from PIL import Image
import numpy as np
from io import StringIO

# --- Streamlit Page Setup ---
st.set_page_config(page_title="Integrated Operations AI", layout="wide")
st.title("Wisconsin Home Care AI App")

# --- File Uploader ---
st.header("Upload Scanned Document (Images Only, JPG/PNG Recommended)")

uploaded_files = st.file_uploader(
    "Upload scanned document (you can select multiple images)",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if uploaded_files:
    st.info("Starting OCR... Please wait.")
    reader = easyocr.Reader(['en'], gpu=False)
    full_extracted_text = ""

    # --- Process Each Uploaded Image ---
    for i, uploaded_file in enumerate(uploaded_files):
        st.info(f"Processing image {i+1} of {len(uploaded_files)}")
        image = Image.open(uploaded_file)
        image_np = np.array(image)
        result = reader.readtext(image_np, detail=0)
        page_text = " ".join(result)
        page_text = " ".join(page_text.split())  # Clean extra spaces
        full_extracted_text += page_text + "\n"

    st.success("OCR Complete")
    st.text_area("Extracted Text Preview", full_extracted_text, height=300)

    # --- Draft Care Plan Generation ---
    st.header("Generated Draft Care Plan")
    extracted_lower = full_extracted_text.lower()

    if "mobility" in extracted_lower:
        st.write("• Assist with mobility and transfers as needed.")
    if "diabetes" in extracted_lower:
        st.write("• Monitor blood glucose and assist with diabetic care.")
    if "dementia" in extracted_lower:
        st.write("• Provide cognitive support and supervision for safety.")
    if "fall" in extracted_lower:
        st.write("• Implement fall prevention interventions.")
    if "hypertension" in extracted_lower:
        st.write("• Monitor blood pressure and manage hypertension.")
    if "medication" in extracted_lower:
        st.write("• Assist with medication management as prescribed.")
    if "nutrition" in extracted_lower:
        st.write("• Provide meal support and dietary assistance.")
    if "continence" in extracted_lower:
        st.write("• Support toileting and continence care.")

    # --- Optional Download ---
    care_plan_text = "Generated Care Plan:\n" + full_extracted_text
    st.download_button(
        "Download Care Plan as Text File",
        care_plan_text,
        file_name="care_plan.txt"
    )