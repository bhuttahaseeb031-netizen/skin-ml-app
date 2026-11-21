import streamlit as st
import pandas as pd
import numpy as np
import pickle

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Skin Health & Condition Predictor",
    page_icon="✨",
    layout="centered"
)

# --- 2. DARK MODE CSS THEME ---
st.markdown(
    """
    <style>
    /* Main Dark Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }

    /* Transparent Top Header */
    header[data-testid="stHeader"] {
        background-color: transparent;
    }

    /* Headings (Cyan Accent) */
    h1, h2, h3 {
        color: #38bdf8 !important;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 700;
    }

    /* Normal Text & Labels */
    p, label, .stMarkdown {
        color: #e2e8f0 !important;
    }

    /* Input Boxes, Number Inputs & Selectboxes */
    div[data-testid="stFileUploader"], 
    div[data-testid="stNumberInput"] > div,
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-radius: 10px;
        color: #f8fafc !important;
    }

    /* Predict Button Style */
    .stButton > button {
        background: linear-gradient(90deg, #0284c7 0%, #0d9488 100%);
        color: #ffffff !important;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 2rem;
        font-weight: 600;
        width: 100%;
        margin-top: 10px;
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

# --- 3. APP HEADER & DESCRIPTION ---
st.title("Skin Health & Condition Predictor")
st.write("Apni skin details aur lifestyle factors neeche enter karein taake condition predict ki ja sake.")
st.markdown("---")

# --- 4. LOAD TRAINED MODEL ---
# Apni .pkl file ka sahi naam yahan likhein
@st.cache_resource
def load_model():
    try:
        with open("skin_model.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None

model = load_model()

# --- 5. USER INPUT FORM ---
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age (Umar)", min_value=10, max_value=100, value=25)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    skin_type = st.selectbox("Skin Type", ["Oily", "Dry", "Combination", "Normal", "Sensitive"])
    hydration = st.slider("Daily Water Intake (Glasses)", 1, 15, 6)

with col2:
    sleep_hours = st.slider("Sleep Hours (Rozana Neend)", 3, 12, 7)
    stress_level = st.selectbox("Stress Level", ["Low", "Medium", "High"])
    sun_exposure = st.selectbox("Sun Exposure", ["Low", "Moderate", "High"])
    diet_quality = st.selectbox("Diet Quality", ["Healthy", "Average", "Junk/Oily"])

st.markdown("---")

# --- 6. PREDICTION LOGIC ---
if st.button("Predict Skin Condition"):
    if model is not None:
        # Encoding inputs (Apne model ki training encoding ke mutabiq adjust karein)
        gender_map = {"Male": 0, "Female": 1, "Other": 2}
        skin_map = {"Oily": 0, "Dry": 1, "Combination": 2, "Normal": 3, "Sensitive": 4}
        level_map = {"Low": 0, "Medium": 1, "Moderate": 1, "High": 2}
        diet_map = {"Healthy": 0, "Average": 1, "Junk/Oily": 2}

        features = np.array([[
            age,
            gender_map[gender],
            skin_map[skin_type],
            hydration,
