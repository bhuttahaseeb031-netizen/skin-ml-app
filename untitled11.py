import streamlit as st
from PIL import Image
import numpy as np
from datetime import datetime
from fpdf import FPDF

# 1. Page Configuration
st.set_page_config(
    page_title="DermaPro Clinical OS | AI Diagnostics",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Next-Level Dark Clinical CSS (Glassmorphism + Neon Accents)
css_code = """
<style>
/* Main Background */
.stApp {
    background: radial-gradient(circle at 15% 15%, #0f172a 0%, #090d16 60%, #020617 100%);
    color: #f8fafc;
}

/* Sidebar Styling */
section[data-testid="stSidebar"] {
    background-color: rgba(15, 23, 42, 0.95) !important;
    border-right: 1px solid rgba(56, 189, 248, 0.2);
}
section[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}

/* Header Banner (Upgraded from your original med-header) */
.med-header {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #0d9488 100%);
    padding: 28px 32px;
    border-radius: 20px;
    margin-bottom: 24px;
    border: 1px solid rgba(56, 189, 248, 0.35);
    box-shadow: 0 20px 40px -15px rgba(13, 148, 136, 0.35);
}
.med-header h1 {
    color: #ffffff !important;
    font-size: 2.1rem;
    font-weight: 800;
    margin: 0 0 6px 0;
    letter-spacing: -0.5px;
}
.med-header p {
    color: #cbd5e1 !important;
    font-size: 1.02rem;
    margin: 0;
}

/* Glass Cards */
.clinical-card {
    background: rgba(30, 41, 59, 0.55);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid rgba(148, 163, 184, 0.15);
    border-radius: 18px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.4);
}
.card-title {
    color: #38bdf8 !important;
    font-size: 1.15rem;
    font-weight: 700;
    margin-bottom: 16px;
    border-bottom: 1px solid rgba(56, 189, 248, 0.2);
    padding-bottom: 8px;
}

/* Result Status Badges */
.badge-low {
    background: linear-gradient(90deg, rgba(16, 185, 129, 0.2), rgba(5, 150, 105, 0.1));
    border-left: 5px solid #10b981;
    color: #34d399;
    padding: 14px 18px;
    border-radius: 10px;
    font-weight: 700;
    font-size: 1.15rem;
    margin: 12px 0;
}
.badge-high {
    background: linear-gradient(90deg, rgba(239, 68, 68, 0.2), rgba(220, 38, 38, 0.1));
    border-left: 5px solid #ef4444;
    color: #f87171;
    padding: 14px 18px;
    border-radius: 10px;
    font-weight: 700;
    font-size: 1.15rem;
    margin: 12px 0;
}

/* Labels & Inputs */
label, .stMarkdown p, h1, h2, h3, h4 {
    color: #f1f5f9 !important;
}
div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {
    background-color: rgba(15, 23, 42, 0.85) !important;
    border: 1px solid rgba(56, 189, 248, 0.3) !important;
    color: #ffffff !important;
    border-radius: 10px !important;
}
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

# 3. PDF Report Generator
def generate_clinical_pdf(p_name, p_age, p_gender, lesion_loc, diagnosis, confidence, risk, notes):
    pdf = FPDF()
    pdf.add_page()
    
    # Header
    pdf.set_fill_color(15, 23, 42)
    pdf.rect(0, 0, 210, 42, 'F')
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 19)
    pdf.cell(0, 18, "DermaPro Clinical OS | AI Diagnostic Report", ln=True, align="C")
    
    pdf.set_text_color(56, 189, 248)
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 8, f"Report Date: {datetime.now().strftime('%d %b %Y - %I:%M %p')}", ln=True, align="C")
    pdf.ln(18)
    
    # Patient Info
    pdf.set_text_color(15, 23, 42)
    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 9, "PATIENT PROFILE", ln=True)
    pdf.set_draw_color(13, 148, 136)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(4)
    
    pdf.set_font("Helvetica", "", 11)
    pdf.cell(48, 8, "Patient Name:")
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 8, p_name if p_name.strip() else "Anonymous Patient", ln=True)
    
    pdf.set_font("Helvetica", "", 11)
    pdf.cell(48, 8, "Age / Gender:")
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 8, f"{p_age} Years / {p_gender}", ln=True)
    
    pdf.set_font("Helvetica", "", 11)
    pdf.cell(48, 8, "Lesion Location:")
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 8, lesion_loc, ln=True)
    pdf.ln(8)
    
    # Diagnostic Summary
    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 9, "AI SCREENING
