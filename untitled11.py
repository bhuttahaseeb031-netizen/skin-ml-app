import streamlit as st
from PIL import Image
import datetime

st.set_page_config(
    page_title="DERMAVISION PRO | Global AI Dermatology Suite",
    layout="wide",
    initial_sidebar_state="collapsed"
)

css_code = """
<style>
    /* Flagship Linear / Apple Dark Pro Canvas */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #172033 0%, #090d16 55%, #05070c 100%);
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Inter", "Segoe UI", sans-serif;
    }
    section[data-testid="stSidebar"] {display: none;}
    header[data-testid="stHeader"] {background: transparent !important;}

    /* Crisp High-Contrast Typography */
    label, p, h1, h2, h3, h4, span, div {
        color: #f1f5f9;
    }

    /* Dark Sleek Inputs & Dropdowns */
    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {
        background-color: rgba(15, 23, 42, 0.9) !important;
        border: 1px solid rgba(148, 163, 184, 0.25) !important;
        border-radius: 10px !important;
        color: #ffffff !important;
    }
    input {color: #ffffff !important;}

    /* Dark Glass Uploader */
    section[data-testid="stFileUploaderDropzone"] {
        background-color: rgba(15, 23, 42, 0.75) !important;
        border: 1.5px dashed #38bdf8 !important;
        border-radius: 16px !important;
        padding: 24px !important;
    }
    section[data-testid="stFileUploaderDropzone"] button {
        background: linear-gradient(90deg, #0284c7, #2563eb) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }

    /* Top Flagship Hero Banner */
    .flagship-hero {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.85) 0%, rgba(15, 23, 42, 0.95) 100%);
        border: 1px solid rgba(56, 189, 248, 0.35);
        border-radius: 20px;
        padding: 28px 34px;
        margin-bottom: 18px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.55);
    }
    .hero-pill {
        display: inline-block;
        background: rgba(56, 189, 248, 0.14);
        border: 1px solid rgba(56, 189, 248, 0.5);
        color: #38bdf8 !important;
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        margin-bottom: 10px;
    }
    .hero-h1 {
        font-size: 2.3rem;
        font-weight: 900;
        background: linear-gradient(90deg, #ffffff 0%, #bae6fd 50%, #38bdf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        letter-spacing: -0.02em;
    }
    .hero-p {
        color: #94a3b8 !important;
        font-size: 0.96rem;
        margin-top: 6px;
    }

    /* Status Strip Cards */
    .strip-card {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(148, 163, 184, 0.16);
        border-radius: 14px;
        padding: 14px 18px;
        margin-bottom: 20px;
    }
    .strip-lbl {
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #94a3b8 !important;
        font-weight: 700;
    }
    .strip-val {
        font-size: 1.05rem;
        font-weight: 800;
        color: #f8fafc !important;
        margin-top: 2px;
    }

    /* Section Panel Box */
    .pro-panel {
        background: rgba(15, 23, 42, 0.72);
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 18px;
        padding: 22px;
        margin-bottom: 16px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
    }

    /* Primary Glowing CTA Button */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #0ea5e9 0%, #2563eb 50%, #4f46e5 100%);
        color: #ffffff !important;
        font-weight: 800;
        border: none;
        padding: 0.9rem 1.5rem;
        border-radius: 12px;
        font-size: 1.05rem;
        letter-spacing: 0.02em;
        box-shadow: 0 10px 28px rgba(14, 165, 233, 0.35);
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #38bdf8 0%, #3b82f6 50%, #6366f1 100%);
        color: #ffffff !important;
    }
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

# 1. Flagship Hero Banner
hero_html = '<div class="flagship-hero"><span class="hero-pill">DERMAVISION PRO • GLOBAL CLINICAL AI PLATFORM</span><div class="hero-h1">Next-Generation Dermoscopy & Oncology Triage</div><div class="hero-p">Enterprise-grade skin lesion screening powered by Deep Vision Neural Networks & standardized ABCDE clinical scoring.</div></div>'
st.markdown(hero_html, unsafe_allow_html=True)

# 2. Live System Telemetry Strip (4 Top Mini Cards)
s1, s2, s3, s4 = st.columns(4)
s1.markdown('<div class="strip-card"><div class="strip-lbl">NEURAL ARCHITECTURE</div><div class="strip-val" style="color:#38bdf8 !important;">DermaNet-V4 Pro</div></div>', unsafe_allow_html=True)
s2.markdown('<div class="strip-card"><div class="strip-lbl">VALIDATION ACCURACY</div><div class="strip-val" style="color:#34d399 !important;">96.4% Sensitivity</div></div>', unsafe_allow_html=True)
s3.markdown('<div class="strip-card"><div class="strip-lbl">CLINICAL STANDARD</div><div class="strip-val">Fitzpatrick + ABCDE</div></div>', unsafe_allow_html=True)
s4.markdown('<div class="strip-card"><div class="strip-lbl">SYSTEM STATUS</div><div class="strip-val" style="color:#a78bfa !important;">Online • Instant Triage</div></div>', unsafe_allow_html=True)

# 3. Main Workspace (2 Balanced Columns)
col_left, col_right = st.columns([1, 1.35], gap="large")

with col_left:
    st.markdown("#### 01. Dermoscopy Optical Input")
    uploaded_file = st.file_uploader("Drop High-Resolution Lesion Image (JPG, PNG)", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Active Clinical Specimen", use_container_width=True)
    else:
        st.markdown('<div class="pro-panel"><p style="color:#94a3b8 !important; margin:0; font-size:0.9rem;">Upload a macro dermoscopy photo or sharp close-up image of the skin area to begin neural feature extraction.</p></div>', unsafe_allow_html=True)

with col_right:
    st.markdown("#### 02. Patient Clinical & Biometric Profile")
    r1_a, r1_b, r1_c = st.columns([2, 1, 1])
    patient_name = r1_a.text_input("Patient Full Name", placeholder="e.g., Haseeb Raza")
    age = r1_b.number_input("Age", min_value=1, max_value=120, value=24)
    gender = r1_c.selectbox("Biological Sex", ["Male", "Female", "Other"])

    r2_a, r2_b, r2_c = st.columns(3)
    skin_type = r2_a.selectbox("Fitzpatrick Skin Type", ["Type I-II (Fair)", "Type III-IV (Medium)", "Type V-VI (Dark)"])
    lesion_area = r2_b.selectbox("Anatomical Location", ["Head / Neck", "Upper Extremity", "Trunk / Back", "Lower Extremity", "Acral (Palm/Sole)"])
    uv_level = r2_c.selectbox("UV Exposure Level", ["Low", "Moderate", "High / Chronic"])

    r3_a, r3_b = st.columns(2)
    water_cups = r
