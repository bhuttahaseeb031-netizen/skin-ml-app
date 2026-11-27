import streamlit as st
from PIL import Image
import datetime
import pandas as pd
from fpdf import FPDF

# 1. Page Configuration (Must be the very first Streamlit command)
st.set_page_config(
    page_title="DERMACARE GLOBAL | AI Clinical Portal",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Session State Initialization
if "patient_records" not in st.session_state:
    st.session_state.patient_records = []
if "saved_reports" not in st.session_state:
    st.session_state.saved_reports = []

# 3. Clean High-Clarity Clinical CSS (No global div color conflicts)
css_code = """
<style>
.stApp {
    background: linear-gradient(180deg, #f0f4f8 0%, #e2e8f0 100%);
    color: #0f172a;
}

section[data-testid="stSidebar"] {
    display: none;
}

header[data-testid="stHeader"] {
    background: transparent !important;
}

/* Scoped Text & Label Contrast */
.stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4,
label[data-testid="stWidgetLabel"] p, .stCheckbox label p {
    color: #0f172a !important;
}

/* Input & Dropdown Styling */
div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    border: 1.5px solid #cbd5e1 !important;
    border-radius: 10px !important;
}
input {
    color: #0f172a !important;
    -webkit-text-fill-color: #0f172a !important;
    font-weight: 600 !important;
}

/* File Uploader Dropzone */
section[data-testid="stFileUploaderDropzone"] {
    background-color: #ffffff !important;
    border: 2px dashed #0284c7 !important;
    border-radius: 16px !important;
    padding: 20px !important;
}
section[data-testid="stFileUploaderDropzone"] button {
    background-color: #0284c7 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
}
section[data-testid="stFileUploaderDropzone"] button span {
    color: #ffffff !important;
}

/* Royal Clinical Header Banner */
.royal-banner {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 60%, #0f766e 100%);
    border-radius: 20px;
    padding: 28px 34px;
    margin-bottom: 20px;
    box-shadow: 0 16px 35px rgba(15, 23, 42, 0.25);
}
.royal-pill {
    display: inline-block;
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.35);
    color: #ffffff !important;
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 700;
    margin-bottom: 10px;
}
.royal-h1 {
    font-size: 2.2rem;
    font-weight: 900;
    color: #ffffff !important;
    margin: 0;
}
.royal-p {
    color: #e2e8f0 !important;
    font-size: 0.96rem;
    margin-top: 6px;
}

/* White Clinical Cards */
.white-card {
    background-color: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 16px;
    box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);
}
.card-tag {
    font-size: 0.72rem;
    text-transform: uppercase;
    color: #64748b !important;
    font-weight: 700;
}

/* Primary Action Button */
div.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #0284c7 0%, #0d9488 100%) !important;
    border: none !important;
    padding: 0.9rem 1.5rem !important;
    border-radius: 12px !important;
    box-shadow: 0 8px 20px rgba(2, 132, 199, 0.28);
}
div.stButton > button p {
    color: #ffffff !important;
    font-weight: 800 !important;
}

/* PDF Download Button */
div.stDownloadButton > button {
    width: 100%;
    background: linear-gradient(90deg, #059669 0%, #10b981 100%) !important;
    border: none !important;
    padding: 0.9rem 1.5rem !important;
    border-radius: 12px !important;
    box-shadow: 0 8px 20px rgba(5, 150, 105, 0.28);
}
div.stDownloadButton > button p {
    color: #ffffff !important;
    font-weight: 800 !important;
}
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

# Helper to prevent FPDF Unicode crashes on special characters/emojis
def safe_pdf_text(text: str) -> str:
    return str(text).encode("latin-1", "replace").decode("latin-1")

# 4. Safe PDF Generator Function
def generate_dossier_pdf(report_id, gen_time, img_name, p_name, age, gender, skin_type, lesion_area,
                         uv_level, water_cups, hydration, sleep_hrs, abcde_total,
                         a_flag, b_flag, c_flag, d_flag, e_flag,
                         verdict, risk_tier, conf, benign_prob, malignant_prob, wellness, action_plan):
    pdf = FPDF()
    pdf.add_page()
    
    # Header Banner
    pdf.set_fill_color(15, 23, 42)
    pdf.rect(0, 0, 210, 42, 'F')
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 17)
    pdf.cell(0, 15, "DERMACARE GLOBAL - CLINICAL ONCOLOGY DOSSIER", ln=True, align="C")
    
    pdf.set_text_color(147, 197, 253)
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 8, safe_pdf_text(f"Report ID: {report_id}  |  Generated: {gen_time}"), ln=True, align="C")
    pdf.ln(18)
    
    # Section 1: Patient & Biometric Profile
    pdf.set_text_color(15, 23, 42)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "1. PATIENT & BIOMETRIC PROFILE", ln=True)
    pdf.set_draw_color(2, 132, 199)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(3)
    
    details = [
        ("Full Name:", p_name),
        ("Age / Sex:", f"{age} Years / {gender}"),
        ("Fitzpatrick Skin Type:", skin_type),
        ("Anatomical Location:", lesion_area),
        ("UV Exposure Level:", uv_level),
        ("Daily Hydration:", f"{water_cups} Glasses/Day ({hydration}%)"),
        ("Restorative Sleep:", f"{sleep_hrs} Hours/Night"),
        ("Specimen File:", img_name)
    ]
    for label, val in details:
        pdf
