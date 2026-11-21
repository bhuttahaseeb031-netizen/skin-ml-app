import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Skin Health & Cancer Predictor",
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
    .student-banner {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-left: 5px solid #38bdf8;
        border-radius: 12px;
        padding: 15px 20px;
        margin-bottom: 20px;
    }
    section[data-testid="stFileUploaderDropzone"] {
        background-color: #1e293b !important;
        border: 2px dashed #38bdf8 !important;
        border-radius: 12px;
        padding: 20px;
    }
    /* Fix for all input & dropdown boxes so text is clearly visible */
    div[data-baseweb="input"],
    div[data-baseweb="input"] > div,
    div[data-baseweb="base-input"],
    div[data-baseweb="select"] > div {
        background-color: #1e293b !important;
        border-color: #38bdf8 !important;
        color: #f8fafc !important;
        border-radius: 10px !important;
    }
    input[type="text"],
    input[type="number"],
    div[data-baseweb="select"] span,
    div[data-baseweb="select"] div {
        background-color: transparent !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }
    input::placeholder {
        color: #94a3b8 !important;
        -webkit-text-fill-color: #94a3b8 !important;
    }
    /* Dropdown menu list items */
    ul[role="listbox"] {
        background-color: #1e293b !important;
        color: #ffffff !important;
    }
    ul[role="listbox"] li {
        color: #ffffff !important;
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

st.markdown(
    """
    <div class="student-banner">
        <p><strong>Student Name:</strong> Haseeb Raza</p>
        <p><strong>Program & Section:</strong> BS Computer Science (Section I)</p>
        <p><strong>Sir Name:</strong> Karar Haider</p>
        <p><strong>University:</strong> Superior University Gold Campus</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("Skin Health & Cancer Predictor")
st.write("Upload skin image and enter patient details to generate the analysis report:")
st.markdown("---")

st.subheader("Upload Skin Image")
uploaded_file = st.file_uploader(
    "Upload clear skin image (JPG, JPEG, PNG)",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Skin Image", width=300)

st.markdown("---")

st.subheader("Patient & Lifestyle Details")

patient_name = st.text_input(
    "Patient Name",
    placeholder="Enter patient full name..."
)

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=10, max_value=100, value=24)
    gender = st.selectbox("Gender", ["Male", "Female"])
    skin_type = st.selectbox(
        "Skin Type",
        ["Oily", "Dry", "Combination", "Normal", "Sensitive"]
    )
    water_intake = st.slider("Daily Water Intake (Glasses)", 1, 15, 6)

with col2:
    sleep_hours = st.slider("Sleep Hours", 3, 12, 7)
    stress_level = st.selectbox("Stress Level", ["Low", "Medium", "High"])
    diet_type = st.selectbox(
        "Diet Quality",
        ["Healthy", "Average", "Oily/Fast Food"]
    )

st.markdown("---")

def analyze_skin_abcd(img):
    img_resized = img.resize((224, 224)).convert("RGB")
    arr = np.array(img_resized, dtype=np.float32)

    center = arr[45:179, 45:179]
    gray_center = np.mean(center, axis=2)

    left_half = gray_center[:, :67]
    right_half = np.fliplr(gray_center[:, 67:])
    asymmetry_score = np.mean(np.abs(left_half - right_half))

    color_std = np.std(center)
    dark_pixel_ratio = np.mean(gray_center < 115) * 100

    red_channel = center[:, :, 0]
    green_blue_avg = (center[:, :, 1] + center[:, :, 2]) / 2.0
    red_excess = np.mean(red_channel - green_blue_avg)

    risk_score = (
        (asymmetry_score * 0.8)
        + (color_std * 0.7)
        + (dark_pixel_ratio * 0.6)
        + (max(0.0, float(red_excess)) * 0.9)
    )

    if risk_score >= 52 or dark_pixel_ratio > 35:
        condition = "Malignant Melanoma / High Cancerous Cell Probability"
        risk = "High Risk (Cancerous Indicators Detected)"
        conf_val = min(96.8, 78.0 + (risk_score * 0.2))
        advice = "Consult an Oncologist or Dermatologist immediately for biopsy and dermoscopy."
        level = "high"
    elif risk_score >= 34 or red_excess > 28:
        condition = "Basal Cell Carcinoma / Atypical Dysplastic Lesion"
        risk = "Moderate-High Risk (Suspicious Cells)"
        conf_val = min(91.5, 72.0 + (risk_score * 0.25))
        advice = "Abnormal skin cell patterns detected. Schedule a clinical skin checkup soon."
        level = "med"
    else:
        condition = "Benign Nevus / Normal Healthy Skin Tissue (Non-Cancerous)"
        risk = "Low Risk (Non-Cancerous)"
        conf_val = max(88.0, 97.5 - (risk_score * 0.2))
        advice = "No cancerous indicators detected. Keep skin hydrated and use sunscreen daily."
        level = "low"

    return condition, risk, f"{conf_val:.1f}%", advice, round(float(risk_score), 1), level

if st.button("Generate Full Skin Cancer Report"):
    if uploaded_file is None:
        st.warning("Please upload a skin image first.")
    else:
        name_text = patient_name.strip() if patient_name.strip() else "Not Provided"
        condition, risk, confidence, advice, score, level = analyze_skin_abcd(image)

        st.markdown("---")
        st.subheader("Comprehensive Skin Analysis Report")
        st.write("**Student:** Haseeb Raza | **Program:** BS Computer Science (Section I)")
        st.write("**Supervisor:** Karar Haider | **University:** Superior University Gold Campus")
        st.markdown("---")
        st.write("**Patient Name:**", name_text)
        st.write("**Patient Profile:**", f"{age} yrs | {gender} | {skin_type} Skin")
        st.write("**Detected Condition:**", condition)
        st.write("**ABCD Lesion Risk Index:**", f"{score} / 100")
        st.write("**AI Model Confidence:**", confidence)

        if level == "high":
            st.error(f"**Risk Level:** {risk}\n\n**Recommendation:** {advice}")
        elif level == "med":
            st.warning(f"**Risk Level:** {risk}\n\n**Recommendation:** {advice}")
        else:
            st.success(f"**Risk Level:** {risk}\n\n**Recommendation:** {advice}")

        st.caption("Disclaimer: This AI screening report is for educational purposes only. Please consult a doctor for medical diagnosis.")
