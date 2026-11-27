import streamlit as st
from PIL import Image
import datetime

st.set_page_config(
    page_title="DERMA-LUXE AI | Precision Skin Intelligence",
    layout="wide",
    initial_sidebar_state="collapsed"
)

css_code = """
<style>
    /* Luxury Deep Obsidian & Violet-Gold Theme */
    .stApp {
        background: radial-gradient(circle at 15% 15%, #1e1b4b 0%, #090d16 45%, #05070c 100%);
        color: #f8fafc;
    }

    /* Hide Sidebar for Full-Screen App Experience */
    section[data-testid="stSidebar"] {
        display: none;
    }

    /* Clean Label & Heading Contrast */
    label, .stMarkdown p, h1, h2, h3, h4, .stCheckbox span {
        color: #f1f5f9 !important;
    }

    /* Top Luxury Glass Navbar */
    .top-nav {
        background: linear-gradient(90deg, rgba(99, 102, 241, 0.18) 0%, rgba(236, 72, 153, 0.15) 50%, rgba(245, 158, 11, 0.12) 100%);
        border: 1px solid rgba(165, 180, 252, 0.25);
        border-radius: 24px;
        padding: 26px 32px;
        margin-bottom: 24px;
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.55);
    }
    .brand-pill {
        display: inline-block;
        background: linear-gradient(90deg, #6366f1, #ec4899);
        color: #ffffff !important;
        padding: 4px 14px;
        border-radius: 999px;
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.1em;
        margin-bottom: 10px;
    }
    .main-heading {
        font-size: 2.2rem;
        font-weight: 900;
        background: linear-gradient(90deg, #ffffff 0%, #c4b5fd 50%, #f9a8d4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }

    /* Premium Bento Cards */
    .luxe-card {
        background: rgba(15, 23, 42, 0.78);
        border: 1px solid rgba(196, 181, 253, 0.18);
        border-radius: 20px;
        padding: 22px;
        margin-bottom: 16px;
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.4);
    }
    .kpi-tag {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #a5b4fc !important;
        font-weight: 700;
    }
    .kpi-big {
        font-size: 1.75rem;
        font-weight: 900;
        margin: 6px 0;
    }

    /* Glowing Action Button */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #6366f1 0%, #ec4899 50%, #f59e0b 100%);
        color: #ffffff !important;
        font-weight: 800;
        border: none;
        padding: 0.85rem 1.5rem;
        border-radius: 14px;
        font-size: 1.05rem;
        letter-spacing: 0.03em;
        box-shadow: 0 10px 28px rgba(236, 72, 153, 0.35);
    }
    div.stButton > button:hover {
        opacity: 0.92;
        color: #ffffff !important;
    }
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

# Top Hero Header
st.markdown(
    '<div class="top-nav">'
    '<span class="brand-pill">DERMA-LUXE AI • CLINICAL VISION ENGINE v5.0</span>'
    '<div class="main-heading">Precision Skin Cancer & Biomarker Studio</div>'
    '<p style="color:#cbd5e1 !important; margin-top:6px; margin-bottom:0;">Next-generation dermoscopy screening, visual biomarker analytics, and personalized daily skin protocol.</p>'
    '</div>',
    unsafe_allow_html=True
)

# Step 1 & Step 2 Workspace
col_scan, col_profile = st.columns([1, 1.35], gap="large")

with col_scan:
    st.markdown("### Step 1: Optical Dermoscopy Upload")
    uploaded_file = st.file_uploader("Upload Skin Lesion Photo (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="High-Res Lesion Sample Loaded", use_container_width=True)
    else:
        st.markdown(
            '<div class="luxe-card" style="text-align:center; padding:48px 20px; border: 1px dashed rgba(244, 114, 182, 0.45);">'
            '<h4 style="color:#f472b6 !important; margin-bottom:8px;">No Optical Sample Detected</h4>'
            '<p style="color:#94a3b8 !important; font-size:0.9rem;">Upload a clear, zoomed-in photo of the skin mole or patch to unlock AI Biomarker Analytics.</p>'
            '</div>',
            unsafe_allow_
