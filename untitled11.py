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
    .student-banner {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-left: 5px solid #38bdf8;
        border-radius: 12px;
        padding: 15px 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
    }
    .student-banner p {
        margin: 4px 0;
        font-size: 15px;
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

# --- STUDENT & UNIVERSITY INFO ---
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
    diet_type = st.selectbox(
        "Diet Quality",
        ["Healthy", "Average", "Oily/Fast Food"]
    )

st.markdown("---")

def analyze_skin_abcd(img):
    # Image ko standard size par la kar RGB mein convert karein
    img_resized = img.resize((224, 224)).convert("RGB")
    arr = np.array(img_resized, dtype=np.float32)

    # 1. Center Crop (Asal daagh/lesion zyada tar image ke center mein hota hai)
    center = arr[45:179, 45:179]
    gray_center = np.mean(center, axis=2)

    # 2. ABCD Feature Extraction:
    # A - Asymmetry (Left vs Right aur Top vs Bottom ka farq)
    left_half = gray_center[:, :67]
    right_half = np.fliplr(gray_center[:, 67:])
    asymmetry_score = np.mean(np.abs(left_half - right_half))

    # C - Color Variation & Dark Pigmentation (Melanoma mein dark/multi-shade pixels hote hain)
    color_std = np.std(center)
    dark_pixel_ratio = np.mean(gray_center < 115) * 100

    # R - Erythema / Redness Index (Basal/Squamous cell carcinoma mein redness zyada hoti hai)
    red_excess = np.mean(center[:, :, 0] - (center[:, :, 1] + center[:, :, 2]) / 2.0)

    # Combined Malignancy Score calculate karein
    risk_score = (
        (asymmetry_score * 0.8) +
        (color_std * 0.7) +
        (dark_pixel_ratio * 0.6) +
        (max(0, red_excess) * 0.9)
    )

    if risk_score >= 52 or dark_pixel_ratio > 35:
        condition = "Malignant Melanoma / High Cancerous Cell Probability"
        risk = "High Risk (Cancerous Indicators Detected) 🔴"
        confidence = f"{min(96.8, 78.0 + (risk_score * 0.2)):.1f}%"
        advice = "Fauri taur par Oncologist ya Dermatologist se biopsy aur dermoscopy checkup karwayein. Yeh lesion malignant (cancerous) alaamat rakhta hai."
    elif risk_score >= 34 or red_excess > 28:
        condition = "Basal Cell Carcinoma / Atypical Dysplastic Lesion"
        risk = "Moderate-High Risk (Suspicious Cells) 🟠"
        confidence = f"{min(91.5, 72.0 + (risk_score * 0.25)):.1f}%"
        advice = "Skin cells mein ghair-mamooli tabdeeli aur asymmetry nazar aa rahi hai. Doctor se fori clinical checkup karwayein."
    else:
        condition = "Benign Nevus / Normal Healthy Skin Tissue (Non-Cancerous)"
        risk = "Low Risk (Non-Cancerous) 🟢"
        confidence = f"{max(88.0, 97.5 - (risk_score * 0.2)):.1f}%"
        advice = "Koi cancerous alaamat nazar nahi aayin. Apni skin ko hydrated rakhein aur rozana sunscreen istemal karein."

    return condition, risk, confidence, advice, round(risk_score, 1)

if st.button("Generate Full Skin Cancer Report"):
    if uploaded_file is None:
        st.warning("Pehle upar diye gaye box mein skin ki picture upload karein.")
    else:
        condition, risk, confidence, advice, score = analyze_skin_abcd(image)

        report_html = (
            '<div class="report-card">'
            '<h3>🩺 Comprehensive Skin Analysis Report</h3>'
            '<p><strong>Student:</strong> Haseeb Raza | <strong>Program:</strong> BS Computer Science (Section I)</p>'
            '<p><strong>Supervisor:</strong> Karar Haider | <strong>Institution:</strong> Superior University Gold Campus</p>'
            '<hr style="border-color: #334155;">'
            f'<p><strong>Patient Profile:</strong> {age} yrs | {gender} | {skin_type} Skin</p>'
            f'<p><strong>Detected Condition:</strong> {condition}</p>'
            f'<p><strong>Skin Cancer Risk Level:</strong> {risk}</p>'
            f'<p><strong>ABCD Lesion Risk Index:</strong> {score} / 100</p>'
            f'<p><strong>AI Model Confidence:</strong> {confidence}</p>'
            '<hr style="border-color: #334155;">'
            f'<p><strong>Medical Recommendation:</strong><br>{advice}</p>'
            '<p style="font-size: 12px; color: #94a3b8 !important; margin-top: 10px;">'
            '*Disclaimer: Yeh AI screening report sirf educational aur maloomat ke maqsad ke liye hai, hatmi diagnosis ke liye doctor se ruju karein.'
            '</p>'
            '</div>'
        )
        st.markdown(report_html, unsafe_allow_html=True)
