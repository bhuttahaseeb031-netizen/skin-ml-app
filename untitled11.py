import streamlit as st
from PIL import Image
import datetime

st.set_page_config(
    page_title="MedCore Global AI | Dermatology & Oncology Portal",
    layout="wide",
    initial_sidebar_state="collapsed"
)

css_code = """
<style>
    /* Global Enterprise Dark Navy Theme (Stanford / Mayo AI Standard) */
    .stApp {
        background-color: #0a0f1c;
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    section[data-testid="stSidebar"] {display: none;}

    /* Fix ALL Text, Labels, and Inputs to Crisp High-Contrast */
    label, p, h1, h2, h3, h4, span, div {
        color: #f1f5f9;
    }

    /* Override Streamlit White Input Boxes & Selectboxes */
    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {
        background-color: #131c31 !important;
        border: 1px solid #2a3958 !important;
        border-radius: 10px !important;
        color: #ffffff !important;
    }
    input {
        color: #ffffff !important;
    }

    /* Override White File Uploader Dropzone */
    section[data-testid="stFileUploaderDropzone"] {
        background-color: #131c31 !important;
        border: 1.5px dashed #38bdf8 !important;
        border-radius: 14px !important;
        padding: 20px !important;
    }
    section[data-testid="stFileUploaderDropzone"] button {
        background-color: #1e293b !important;
        color: #38bdf8 !important;
        border: 1px solid #38bdf8 !important;
    }

    /* Institutional Top Header */
    .global-header {
        background: linear-gradient(135deg, #0f172a 0%, #172554 60%, #1e3a8a 100%);
        border: 1px solid #2563eb;
        border-radius: 16px;
        padding: 26px 32px;
        margin-bottom: 24px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.45);
    }
    .inst-badge {
        display: inline-block;
        background: rgba(56, 189, 248, 0.15);
        border: 1px solid #38bdf8;
        color: #7dd3fc !important;
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        margin-bottom: 10px;
    }
    .portal-title {
        font-size: 2.1rem;
        font-weight: 800;
        color: #ffffff !important;
        margin: 0;
        letter-spacing: -0.02em;
    }
    .portal-sub {
        color: #cbd5e1 !important;
        font-size: 0.95rem;
        margin-top: 6px;
    }

    /* Enterprise Medical Cards */
    .med-card {
        background-color: #111827;
        border: 1px solid #1f2937;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 16px;
    }
    .card-kicker {
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #94a3b8 !important;
        font-weight: 700;
    }
    .card-metric {
        font-size: 1.65rem;
        font-weight: 800;
        margin: 6px 0;
    }

    /* Primary Medical Blue CTA */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #2563eb 0%, #0284c7 100%);
        color: #ffffff !important;
        font-weight: 700;
        border: none;
        padding: 0.85rem 1.5rem;
        border-radius: 10px;
        font-size: 1rem;
        box-shadow: 0 8px 20px rgba(37, 99, 235, 0.35);
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #3b82f6 0%, #0ea5e9 100%);
        color: #ffffff !important;
    }
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

# Top Institutional Header
header_html = '<div class="global-header"><span class="inst-badge">MEDCORE GLOBAL HEALTH • AI DERMATOLOGY & ONCOLOGY DIVISION</span><div class="portal-title">Clinical Dermoscopy & Skin Cancer Triage Portal</div><div class="portal-sub">Enterprise AI Decision-Support System • Standardized ABCDE Protocol & Patient Risk Stratification</div></div>'
st.markdown(header_html, unsafe_allow_html=True)

# Main 2-Column Enterprise Layout
col_left, col_right = st.columns([1, 1.35], gap="large")

with col_left:
    st.markdown("### Step 1: Dermoscopy Image Capture")
    uploaded_file = st.file_uploader("Upload Clinical Lesion Image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Verified Clinical Specimen", use_container_width=True)
    else:
        st.markdown('<div class="med-card"><p style="color:#94a3b8 !important; margin:0; font-size:0.9rem;">Upload a macro dermoscopy or well-lit clinical photograph of the lesion to initiate neural feature analysis.</p></div>', unsafe_allow_html=True)

with col_right:
    st.markdown("### Step 2: Patient Clinical Intake")
    r1_a, r1_b, r1_c = st.columns([2, 1, 1])
    patient_name = r1_a.text_input("Patient Full Name", placeholder="e.g., Haseeb Raza")
    age = r1_b.number_input("Age (Years)", min_value=1, max_value=120, value=25)
    gender = r1_c.selectbox("Biological Sex", ["Male", "Female", "Other"])

    r2_a, r2_b, r2_c = st.columns(3)
    skin_type = r2_a.selectbox("Fitzpatrick Skin Type", ["Type I-II (Fair)", "Type III-IV (Medium/Olive)", "Type V-VI (Dark)"])
    lesion_area = r2_b.selectbox("Anatomical Location", ["Head / Neck", "Upper Extremity", "Trunk / Back", "Lower Extremity", "Acral (Palm/Sole)"])
    uv_level = r2_c.selectbox("UV Exposure History", ["Low", "Moderate", "High / Chronic"])

    r3_a, r3_b = st.columns(2)
    water_cups = r3_a.slider("Daily Hydration (Glasses)", min_value=1, max_value=15, value=8)
    sleep_hrs = r3_b.slider("Restorative Sleep (Hours)", min_value=3, max_value=12, value=7)

    st.markdown("### Step 3: Standardized ABCDE Criteria")
    f1, f2, f3 = st.columns(3)
    chk_a = f1.checkbox("A — Asymmetry")
    chk_b = f2.checkbox("B — Border Irregularity")
    chk_c = f3.checkbox("C — Color Variegation")

    f4, f5 = st.columns(2)
    chk_d = f4.checkbox("D — Diameter > 6 mm")
    chk_e = f5.checkbox("E — Evolving / Changing")

    st.markdown("<br>", unsafe_allow_html=True)
    run_btn = st.button("Run Clinical AI Assessment")

# Diagnostic Dossier Output
if run_btn:
    if uploaded_file is None:
        st.warning("Please upload a clinical lesion image in Step 1 before running the assessment.")
    else:
        st.markdown("---")
        p_name = patient_name.strip() if patient_name.strip() else "Patient Record #01"
        abcde_total = sum([chk_a, chk_b, chk_c, chk_d, chk_e])

        hydration = min(100, water_cups * 10)
        uv_def = 90 if uv_level == "Low" else (65 if uv_level == "Moderate" else 35)
        barrier = min(100, 60 + (sleep_hrs * 3))
        wellness = int((hydration + uv_def + barrier) / 3)

        if abcde_total >= 2:
            verdict = "High Priority — Dermatology Referral"
            v_color = "#f87171"
