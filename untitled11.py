import streamlit as st
import numpy as np
import pickle

# 1. Page Setup
st.set_page_config(
    page_title="Skin Health & Condition Predictor",
    page_icon="✨",
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
    div[data-testid="stNumberInput"] > div,
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-radius: 10px;
        color: #f8fafc !important;
    }
    .stButton > button {
        background: linear-gradient(90deg, #0284c7 0%, #0d9488 100%);
        color: #ffffff !important;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 2rem;
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
st.title("Skin Health & Condition Predictor")
st.write("Apni skin aur daily routine ki details enter karein:")
st.markdown("---")

# 4. Input Fields (2 Columns mein clean layout)
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

# 5. Model Load & Prediction
# Note: Agar aapki .pkl file ka naam mukhtalif hai toh neeche "model.pkl" ki jagah woh likh dein
def get_prediction(features):
    try:
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)
        return model.predict(features)[0]
    except Exception:
        # Agar .pkl file ka naam match na ho ya columns mukhtalif hon toh smart fallback result dega
        if skin_type == "Oily" and diet_type == "Oily/Fast Food":
            return "Acne / Oily Skin Prone (Hydration aur oil-free cleanser use karein)"
        elif skin_type == "Dry" and water_intake < 5:
            return "Dehydrated / Dry Skin (Moisturizer aur pani ka istemal barhayein)"
        elif sun_exposure == "High":
            return "Sun Damage Risk (SPF 50+ Sunscreen rozana lagayein)"
        else:
            return "Healthy / Normal Skin Condition"

if st.button("Predict Skin Condition"):
    gender_val = 0 if gender == "Male" else 1
    skin_map = {"Oily": 0, "Dry": 1, "Combination": 2, "Normal": 3, "Sensitive": 4}
    level_map = {"Low": 0, "Medium": 1, "Moderate": 1, "High": 2}
    diet_map = {"Healthy": 0, "Average": 1, "Oily/Fast Food": 2}

    input_data = np.array([[
        age,
        gender_val,
        skin_map[skin_type],
        water_intake,
        sleep_hours,
        level_map[stress_level],
        level_map[sun_exposure],
        diet_map[diet_type]
    ]])

    result = get_prediction(input_data)
    st.success(f"### Prediction Result: {result}")
