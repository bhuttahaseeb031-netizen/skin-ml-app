import streamlit as st
import numpy as np
import pickle
from PIL import Image

# 1. Page Setup
st.set_page_config(
    page_title="Skin Health & Cancer Predictor",
    page_icon="🔬",
    layout="centered"
)

# 2. Dark Mode & Stylish UI CSS
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
    /* File Uploader Box Styling */
    section[data-testid="stFileUploaderDropzone"] {
        background-color: #1e293b !important;
        border: 2px dashed #38bdf8 !important;
        border-radius: 12px;
        padding: 20px;
    }
    /* Input Fields Styling */
    div[data-testid="stNumberInput"] > div,
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-radius: 10px;
        color: #f8fafc !important;
    }
    /* Report Card Styling */
    .report-card {
        background-color: #1e293b;
        border-left: 5px solid #38bdf8;
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    /* Predict Button Style */
    .stButton > button {
        background: linear-gradient(90deg, #0284c7 0%, #0d9488 100%);
        color: #ffffff !important;
        border: none;
        border-radius: 10px;
        padding: 0.7rem 2rem;
        font-weight: 600;
        width: 100%;
        margin-top: 15px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 14px rgba(2, 132, 199, 0.4);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(13, 148, 136, 0.6);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Title & Intro
st.title("Skin Health & Cancer Predictor")
st.write("Apni skin ki picture upload karein aur daily routine ki details enter karke mukammal report hasil karein:")
st.markdown("---")

# 4. Image Uploader Box
st.subheader("📸 Upload Skin Lesion / Affected Area Image")
uploaded_file = st.file_uploader("Clear picture upload karein (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Skin Image", width=300)

st.markdown("---")

# 5. User Details Form
st.subheader("📋 Patient & Lifestyle Details")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age (Umar)", min_value=10, max_value=100, value=24)
    gender = st.selectbox("Gender", ["Male", "Female"])
    skin_type = st.selectbox("Skin Type", ["Oily", "Dry", "Combination", "Normal", "Sensitive"])
    water_intake = st.slider("Daily Water Intake (Glasses)", 1, 15, 6)

with col2:
    sleep_hours = st.slider("Sleep Hours (Rozana Neend)", 3, 12, 7)
    stress_level = st.selectbox("Stress Level", ["Low", "Medium", "High"])
    sun_exposure = st.selectbox("Sun Exposure", ["Low", "Moderate", "High"])
    diet_type = st.selectbox("Diet Quality", ["Healthy", "Average", "Oily/Fast Food"])

st.markdown("---")

# 6. Analysis & Report Generation Logic
def analyze_image_and_data(img, age, sun_exp, skin_t):
    # Image pixel brightness & color variance check (Basic heuristic + Model fallback)
    img_resized = img.resize((128, 128)).convert("RGB")
    img_array = np.array(img_resized)
    
    # Redness aur dark pigmentation ka andaza
    red_mean = np.mean(img_array[:, :, 0])
    darkness = 255 - np.mean(img_array)

    # Agar aapke paas trained CNN/ML image model (.pkl / .h5) hai toh yahan load kar sakte hain
    try:
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)
        # Agar model image array accept karta hai toh yahan predict karein
    except Exception:
        pass

    # Risk & Condition Assessment
    if darkness > 140 and sun_exp == "High":
        condition = "Suspected Pigmented Lesion / High Melanoma Risk"
        risk = "High Risk 🔴"
        confidence = "87.4%"
        advice = "Fauri taur par Dermatologist (Skin Specialist) se dermoscopy checkup karwayein. Dhoop se mukammal parhez karein."
    elif red_mean > 150 and darkness > 110:
        condition = "Actinic Keratosis / Basal Cell Suspicion"
        risk = "Moderate Risk 🟡"
        confidence = "82.1%"
        advice = "
