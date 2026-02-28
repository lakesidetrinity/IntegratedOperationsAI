# streamlit_app.py
import streamlit as st
import PyPDF2

st.set_page_config(page_title="Integrated Operations AI", layout="wide")

st.title("Wisconsin Home Care AI App")
st.markdown(
    "Welcome to your Integrated Operations system for Home Care. "
    "This app helps with client intake, care plans, employee workflows, and marketing."
)

# -------------------------
# Participant/Client Section
# -------------------------
st.header("Participant / Client")
uploaded_pdf = st.file_uploader("Upload Participant Business Info or H&P PDF", type=["pdf"])
if uploaded_pdf:
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        st.write("PDF uploaded successfully. Preview text:")
        st.text_area("Preview", text, height=200)
        st.info("AI integration for functional screen (F-00044) and care plan (F-21278) will go here.")
    except Exception as e:
        st.error(f"Error reading PDF: {e}")

# -------------------------
# Employee / Volunteers Section
# -------------------------
st.header("Employee / Volunteers")
st.info("Onboarding, competency exams, and DHS 12 background check tracking will go here.")

# -------------------------
# Business Operations Section
# -------------------------
st.header("Business Operations")
st.info("Policies & Procedures, QA audits, and DHS 105.17 compliance features will go here.")

# -------------------------
# Marketing Section
# -------------------------
st.header("Marketing")
st.info("AI-driven flyer, business card, and brochure generation will go here.")

# -------------------------
# Footer / Notes
# -------------------------
st.write("---")
st.write("This is the moderate starter app. You can expand AI functionality, dashboards, and integrations later.")