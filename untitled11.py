import streamlit as st
from PIL import Image
import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="DermaPro Clinical OS | AI Diagnostics",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Modern Clinical Light SaaS CSS
st.markdown("""
<style>
    /* Clean Light Clinical Canvas */
    .stApp {
        background-color: #f4f7fb;
        color: #0f172a;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }

    /* Fix all input & label visibility */
    label, .stMarkdown p, h1, h2, h3, h4 {
        color: #0f172a !important;
    }

    /* Top Medical Header Banner */
    .med-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 55%, #0d9488 100%);
        padding: 28px 32px;
        border-radius: 18px;
        color: white !important;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.15);
    }
    .med-header h1 {
        color: #ffffff !important;
        font-size: 2rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .med-header p {
        color: #cbd5e1 !important;
        font-size: 0.95rem;
        margin-top: 6px;
        margin-bottom: 0;
    }
    .badge-live {
        display: inline-block;
        background: rgba(20, 184, 166, 0.2);
        border: 1px solid #2dd4bf;
        color: #5eead4 !important;
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-bottom: 10px;
    }

    /* White Elevated Cards */
    .clinical-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 22px;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
        margin-bottom: 16px;
    }
    .metric-label {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #64748b !important;
        font-weight: 600;
    }
    .metric-value {
        font-size: 1.75rem;
        font-weight: 800;
        margin: 4px 0;
    }

    /* Primary Action Button */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #0284c7, #0d9488);
        color: #ffffff !important;
        font-weight: 700;
        border: none;
        padding: 0.7rem 1.2rem;
        border-radius: 10px;
        font-size: 0.95rem;
        box-shadow: 0 4px 12px rgba(13, 148, 136, 0.25);
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #0369a1, #0f766e);
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Top Header Banner
st.markdown("""
<div class="med-header">
    <span class="badge-live">● DERMAPRO CLINICAL SUITE v3.0</span>
    <h1>DermaPro AI — Dermatological Diagnostic Workstation</h1>
    <p>Automated Dermoscopy Analysis, ABCDE Risk Scoring & Clinical Summary Generator</p>
</div>
""", unsafe_allow_html=True)

# 4. Left Sidebar: Patient Intake Form
with st.sidebar:
    st.markdown("## 🧑‍⚕️ Patient Intake")
    st.caption("Enter patient profile before running AI scan.")
    
    patient_name = st.text_input("Patient Full Name", placeholder="e.g., Ali Raza")
    col_a, col_b = st.columns(2)
    with col_a:
        age = st.number_input("Age", min_value=1, max_value=120, value=28)
    with col_b:
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        
    skin_type = st.selectbox("Fitzpatrick / Skin Type", ["Normal", "Oily", "Dry", "Combination", "Sensitive"])
    lesion_location = st.selectbox("Lesion Body Location", ["Face / Neck", "Arm / Hand", "Back / Torso", "Leg / Foot", "Other"])
    
    st.markdown("---")
    st.markdown("### 🌿 Lifestyle Factors")
    sun_exposure = st.select_slider("Daily UV / Sun Exposure", options=["Low", "Moderate", "High"])
    water_intake = st.slider("Water Intake (Glasses/Day)", 1
