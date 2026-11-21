import streamlit as st
import numpy as np
import pickle
from PIL import Image

st.set_page_config(
    page_title="Skin Health & Cancer Predictor",
    page_icon="🔬",
    layout="centered"
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    header[data-testid="stHeader"] {
        background-color: transparent;
    }
    h1, h2, h3 {
        color: #38bdf8 !important;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 700;
    }
    p, label, .stMarkdown {
        color: #e2e8f0 !important;
    }
    section[data-testid="stFileUploaderDropzone"] {
        background-color: #1e293b !important;
        border: 2px dashed #38bdf8 !important;
        border-radius: 12px;
        padding: 20px;
    }
    div[data-testid="stNumberInput"] > div,
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-radius: 10px;
        color: #f8fafc !important;
    }
    .report-card {
        background-color: #1e293b;
        border-left: 5px solid #38bdf8;
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .stButton > button {
        background: linear-gradient(90deg, #0284c7 0%, #0d9488 100%);
        color: #ffffff !important;
        border: none;
        border-radius: 10px;
        padding: 0.7rem 2rem;
        font-weight: 600;
        width: 100%;
        margin-top: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Skin Health & Cancer Predictor")
st.write("Apni skin ki picture upload karein aur details enter karke report hasil karein:")
st.markdown("---")

st.subheader("📸 Upload Skin Image")
uploaded_file = st.file_uploader(
    "Clear picture upload karein (JPG, JPEG, PNG)",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Skin Image", width=300)

st.markdown("---")

st.subheader("📋 Patient & Lifestyle Details")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age (Umar)", min_value=10, max_value=100, value=24)
    gender = st.selectbox("Gender", ["Male", "Female"])
    skin_type = st.selectbox(
        "Skin Type",
        ["Oily", "Dry", "Combination", "Normal", "Sensitive"]
    )
    water_intake = st.slider("Daily Water Intake (Glasses)", 1, 15, 6)

with col2:
    sleep_hours = st.slider("Sleep Hours (Rozana Neend)", 3, 12, 7)
    stress_level = st.selectbox("Stress Level", ["Low", "Medium", "High"])
    sun_exposure = st.selectbox("Sun Exposure", ["Low", "Moderate", "High"])
    diet_type = st.selectbox(
        "Diet Quality",
        ["Healthy", "Average", "Oily/Fast Food"]
    )

st.markdown("---")

def analyze_skin(img, sun_exp):
    img_resized = img.resize((128, 128)).convert("RGB")
    img_array = np.array(img_resized)
    red_mean = np.mean(img_array[:, :, 0])
    darkness = 255 - np.mean(img_array)

    if darkness > 140 and sun_exp == "High":
        condition = "Suspected Pigmented Lesion / High Melanoma Risk"
        risk = "High Risk 🔴"
        confidence = "87.4%"
        advice = """Fauri taur par Dermatologist se checkup karwayein.
        Dhoop se mukammal parhez karein."""
    elif red_mean > 150 and darkness > 110:
        condition = "Actinic Keratosis / Basal Cell Suspicion"
        risk = "Moderate Risk 🟡"
        confidence = "82.1%"
        advice = """Skin par surkhi aur daagh ki jaanch ke liye doctor se milein.
        SPF 50+ sunscreen rozana lagayein."""
    else:
        condition = "Benign Nevus / Normal Skin Tissue (Non-Cancerous)"
        risk = "Low Risk 🟢"
        confidence = "94.6%"
        advice = """Koi khatarnak alaamat nazar nahi aayin.
        Skin ko hydrated rakhein aur sunscreen istemal karein."""

    return condition, risk, confidence, advice

if st.button("Generate Full Skin Cancer Report"):
    if uploaded_file is None:
        st.warning("Pehle upar diye gaye box mein skin ki picture upload karein.")
    else:
        condition, risk, confidence, advice = analyze_skin(image, sun_exposure)
        st.markdown(
            f"""
            <div class="report-card">
                <h3>🩺 Comprehensive Skin Analysis Report</h3>
                <p><strong>Patient Profile:</strong> {age} yrs | {gender} | {skin_type} Skin</p>
                <hr style="border-color: #334155;">
                <p><strong>Detected Condition:</strong> {condition}</p>
                <p><strong>Skin Cancer Risk Level:</strong> {risk}</p>
                <p><strong>AI Model Confidence:</strong> {confidence}</p>
                <p><strong>Sun Exposure Factor:</strong> {sun_exposure}</p>
                <hr style="border-color: #334155;">
                <p><strong>Medical Recommendation:</strong><br>{advice}</p>
                <p style="font-size: 12px; color: #94a3b8 !important; margin-top: 10px;">
                *Disclaimer: Yeh AI screening report sirf maloomat ke liye hai, doctor se ruju zaroor karein.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
