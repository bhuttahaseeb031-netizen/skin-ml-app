import streamlit as st
from PIL import Image
import datetime

st.set_page_config(
    page_title="AURA DERMA | Next-Gen AI Skin Intelligence",
    layout="wide",
    initial_sidebar_state="collapsed"
)

css_code = """
<style>
    /* Ultra-Modern Obsidian & Emerald Theme */
    .stApp {
        background: linear-gradient(180deg, #06090f 0%, #0b1120 100%);
        color: #f1f5f9;
    }

    /* Hide default Streamlit sidebar space */
    section[data-testid="stSidebar"] {
        display: none;
    }

    /* Fix all input & label contrast */
    label, .stMarkdown p, h1, h2, h3, h4, .stCheckbox span, .stRadio label {
        color: #e2e8f0 !important;
    }

    /* Hero Top Navigation & Title Bar */
    .hero-banner {
        background: linear-gradient(120deg, rgba(16, 185, 129, 0.14) 0%, rgba(6, 182, 212, 0.12) 50%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 22px;
        padding: 28px 34px;
        margin-bottom: 26px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
    }
    .pill-tag {
        display: inline-block;
        background: rgba(16, 185, 129, 0.18);
        border: 1px solid #10b981;
        color: #34d399 !important;
        padding: 4px 14px;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        margin-bottom: 10px;
    }
    .hero-title {
        font-size: 2.3rem;
        font-weight: 900;
        background: linear-gradient(90deg, #ffffff 0%, #34d399 55%, #22d3ee 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    .hero-sub {
        color: #94a3b8 !important;
        font-size: 0.98rem;
        margin-top: 6px;
    }

    /* Bento Grid Cards */
    .bento-card {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(148, 163, 184, 0.15);
        border-radius: 20px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
    }
    .stat-title {
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #94a3b8 !important;
        font-weight: 600;
    }
    .stat-num {
        font-size: 1.85rem;
        font-weight: 800;
        margin: 6px 0;
    }

    /* Neon Gradient Button */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #10b981 0%, #06b6d4 100%);
        color: #042f2e !important;
        font-weight: 800;
        border: none;
        padding: 0.85rem 1.5rem;
        border-radius: 14px;
        font-size: 1.05rem;
        letter-spacing: 0.02em;
        box-shadow: 0 10px 25px rgba(16, 185, 129, 0.35);
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #34d399 0%, #22d3ee 100%);
        color: #042f2e !important;
    }
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

# Top Hero Banner
banner_html = (
    '<div class="hero-banner">'
    '<span class="pill-tag">AURA DERMA AI • NEURAL DIAGNOSTICS v4.0</span>'
    '<div class="hero-title">Next-Gen Skin Health & Melanoma Intelligence</div>'
    '<div class="hero-sub">Full-screen Bento Diagnostic Engine combining Dermoscopy Vision with Biometric Lifestyle Scoring.</div>'
    '</div>'
)
st.markdown(banner_html, unsafe_allow_html=True)

# Main 2-Column Bento Layout (Full Width, No Sidebar)
col_left, col_right = st.columns([1.05, 1.35], gap="large")

with col_left:
    st.markdown("### 01. Dermoscopy Vision Input")
    uploaded_file = st.file_uploader("Drop high-resolution skin lesion image (JPG, PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Active Neural Scan Sample", use_container_width=True)
    else:
        placeholder_box = (
            '<div class="bento-card" style="text-align:center; padding:45px 20px; border: 1px dashed rgba(52, 211, 153, 0.4);">'
            '<h4 style="color:#34d399 !important; margin-bottom:8px;">Ready for Optical Scan</h4>'
            '<p style="color:#94a3b8 !important; font-size:0.9rem;">Upload a well-lit close-up photo of the skin area above to activate neural feature extraction.</p>'
            '</div>'
        )
        st.markdown(placeholder_box, unsafe_allow_html=True)

with col_right:
    st.markdown("### 02. Patient Biometrics & Lifestyle")

    r1_c1, r1_c2, r1_c3 = st.columns([2, 1, 1])
    with r1_c1:
        patient_name = st.text_input("Patient Name", placeholder="e.g., Zoya Khan")
    with r1_c2:
        age = st.number_input("Age", min_value=1, max_value=120, value=25)
    with r1_c3:
        gender = st.selectbox("Gender", ["Female", "Male", "Other"])

    r2_c1, r2_c2, r2_c3 = st.columns(3)
    with r2_c1:
        skin_type = st.selectbox("Skin Profile", ["Combination", "Oily", "Dry", "Sensitive", "Normal"])
    with r2_c2:
        lesion_site = st.selectbox("Body Region", ["Face / Neck", "Arm / Shoulder", "Upper Back", "Leg / Foot", "Other"])
    with r2_c3:
        sun_uv = st.selectbox("UV Exposure", ["Low", "Moderate", "High"])

    r3_c1, r3_c2 = st.columns(2)
    with r3_c1:
        water_glasses = st.slider("Hydration (Glasses / Day)", min_value=1, max_value=15, value=8)
    with r3_c2:
        sleep_hrs = st.slider("Recovery Sleep (Hours)", min_value=3, max_value=12, value=7)

    with
