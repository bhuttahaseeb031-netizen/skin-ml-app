import streamlit as st

st.markdown(
    """
    <style>
    /* 1. Main Dark Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }

    /* 2. Top Header Bar ko Transparent rakhna */
    header[data-testid="stHeader"] {
        background-color: transparent;
    }

    /* 3. Headings (Glowing Cyan/Teal Accent) */
    h1, h2, h3 {
        color: #38bdf8 !important;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 700;
    }

    /* 4. Normal Text aur Labels ko Clear White rakhna */
    p, label, .stMarkdown {
        color: #e2e8f0 !important;
    }

    /* 5. Input Boxes, Selectboxes aur File Uploader (Dark Glass Card) */
    div[data-testid="stFileUploader"], 
    div[data-testid="stNumberInput"] > div,
    div[data-baseweb="select"] > div {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-radius: 12px;
        color: #f8fafc !important;
    }

    /* File Uploader Inner Box */
    section[data-testid="stFileUploaderDropzone"] {
        background-color: #0f172a !important;
        border: 1px dashed #38bdf8 !important;
        border-radius: 10px;
    }

    /* 6. Stylish Gradient Button */
    .stButton > button {
        background: linear-gradient(90deg, #0284c7 0%, #0d9488 100%);
        color: #ffffff !important;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.8rem;
        font-weight: 600;
        letter-spacing: 0.5px;
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
