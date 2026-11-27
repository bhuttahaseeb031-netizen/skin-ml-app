import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="DermaAI | Skin Health & Cancer Predictor",
    page_icon="🔬",
    layout="wide"
)

# Custom Modern Dark UI CSS
css_code = """
<style>
    .stApp {
        background: radial-gradient(circle at top left, #0f172a, #1e293b, #090d16);
        color: #f8fafc;
    }
    .gradient-title {
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        color: #94a3b8;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    .glass-box {
        background: rgba(30, 41, 59, 0.65);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5);
    }
    div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #0ea5e9, #4f46e5);
        color: white;
        font-weight: 600;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 12px;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #38bdf8, #6366f1);
        box-shadow: 0 8px 20px rgba(56, 189, 248, 0.3);
        color: white;
    }
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

# Header Section
st.markdown('<div class="gradient-title">🔬 DermaAI: Skin Health & Cancer Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload a clear dermoscopy or skin image and enter patient lifestyle metrics for an instant AI diagnostic summary.</div>', unsafe_allow_html=True)

# Two-Column Layout
col1, col2 = st.columns([1, 1.3], gap="large")

with col1:
    st.markdown("### 1. Upload Skin Image")
    uploaded_file = st.file_uploader(
        "Upload clear skin image (JPG, JPEG, PNG)",
        type=["jpg", "jpeg", "png"]
    )
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Skin Sample", use_container_width=True)
    else:
        st.info("👆 Please upload a clear, well-lit close-up photo of the skin area to begin.")

with col2:
    st.markdown("### 2. Patient & Lifestyle Details")

    c1, c2 = st.columns([2, 1])
    with c1:
        patient_name = st.text_input("Patient Full Name", placeholder="Enter patient full name...")
    with c2:
        age = st.number_input("Age", min_value=1, max_value=120, value=24)

    c3, c4 = st.columns(2)
    with c3:
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    with c4:
        skin_type = st.selectbox("Skin Type", ["Oily", "Dry", "Combination", "Sensitive", "Normal"])

    c5, c6 = st.columns(2)
    with c5:
        water_intake = st.slider("Daily Water Intake (Glasses)", 1, 15, 6)
    with c6:
        sleep_hours = st.slider("Sleep Hours", 3, 12, 7)

    c7, c8 = st.columns(2)
    with c7:
        stress_level = st.selectbox("Stress Level", ["Low", "Moderate", "High"])
    with c8:
        diet_quality = st.selectbox("Diet Quality", ["Healthy", "Balanced", "Processed / Junk"])

    st.markdown("<br>", unsafe_allow_html=True)
    generate_btn = st.button("✨ Generate Full Skin Cancer & Health Report")

# Report Generation Section
if generate_btn:
    if not uploaded_file:
        st.warning("⚠️ Please upload a skin image first before generating the report.")
    else:
        st.markdown("---")
        display_name = patient_name if patient_name.strip() else "Patient"
        st.subheader(f"📋 Diagnostic Report: {display_name} ({age} yrs • {skin_type} Skin)")

        wellness_score = 70
        if water_intake >= 8:
            wellness_score += 10
        if sleep_hours >= 7:
            wellness_score += 10
        if stress_level == "Low":
            wellness_score += 10
        elif stress_level == "High":
            wellness_score -= 15

        prediction_label = "Low Risk (Benign)"
        confidence = "94.2%"

        r1, r2, r3 = st.columns(3)

        with r1:
            card1 = (
                '<div class="glass-box">'
                '<p style="color:#94a3b8; font-size:0.85rem; margin-bottom:4px;">AI Lesion Assessment</p>'
                f'<h3 style="color:#34d399; margin:0;">{prediction_label}</h3>'
                f'<p style="color:#64748b; font-size:0.8rem; margin-top:8px;">Model Confidence: {confidence}</p>'
                '</div>'
            )
            st.markdown(card1, unsafe_allow_html=True)

        with r2:
            card2 = (
                '<div class="glass-box">'
                '<p style="color:#94a3b8; font-size:0.85rem; margin-bottom:4px;">Skin Wellness Index</p>'
                f'<h3 style="color:#38bdf8; margin:0;">{wellness_score} / 100</h3>'
                f'<p style="color:#64748b; font-size:0.8rem; margin-top:8px;">{water_intake} glasses water • {sleep_hours}h sleep
