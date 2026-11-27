import streamlit as st
from PIL import Image
import datetime

st.set_page_config(
    page_title="DERMACARE GLOBAL | AI Clinical Portal",
    layout="wide",
    initial_sidebar_state="collapsed"
)

css_code = '<style>.stApp {background: linear-gradient(180deg, #f0f4f8 0%, #e2e8f0 100%); color: #0f172a; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;} section[data-testid="stSidebar"] {display: none;} header[data-testid="stHeader"] {background: transparent !important;} label, p, h1, h2, h3, h4, span, div {color: #0f172a !important;} div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {background-color: #ffffff !important; border: 1.5px solid #cbd5e1 !important; border-radius: 10px !important; color: #0f172a !important;} input {color: #0f172a !important; -webkit-text-fill-color: #0f172a !important; font-weight: 600 !important;} section[data-testid="stFileUploaderDropzone"] {background-color: #ffffff !important; border: 2px dashed #0284c7 !important; border-radius: 16px !important; padding: 20px !important;} section[data-testid="stFileUploaderDropzone"] button {background-color: #0284c7 !important; color: #ffffff !important; border: none !important; border-radius: 8px !important;} section[data-testid="stFileUploaderDropzone"] button span {color: #ffffff !important;} .royal-banner {background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 60%, #0f766e 100%); border-radius: 20px; padding: 28px 34px; margin-bottom: 20px; box-shadow: 0 14px 35px rgba(15, 23, 42, 0.18);} .royal-pill {display: inline-block; background: rgba(255, 255, 255, 0.15); border: 1px solid rgba(255, 255, 255, 0.35); color: #ffffff !important; padding: 4px 12px; border-radius: 999px; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.08em; margin-bottom: 10px;} .royal-h1 {font-size: 2.2rem; font-weight: 900; color: #ffffff !important; margin: 0;} .royal-p {color: #e2e8f0 !important; font-size: 0.96rem; margin-top: 6px;} .white-card {background-color: #ffffff; border: 1px solid #cbd5e1; border-radius: 16px; padding: 20px; margin-bottom: 16px; box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);} .card-tag {font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; color: #64748b !important; font-weight: 700;} div.stButton > button {width: 100%; background: linear-gradient(90deg, #0284c7 0%, #0d9488 100%) !important; border: none !important; padding: 0.9rem 1.5rem !important; border-radius: 12px !important; font-size: 1.05rem !important; box-shadow: 0 8px 20px rgba(2, 132, 199, 0.28) !important;} div.stButton > button p {color: #ffffff !important; font-weight: 800 !important;}</style>'
st.markdown(css_code, unsafe_allow_html=True)

# 1. Top Header Banner
banner_html = '<div class="royal-banner"><span class="royal-pill">DERMACARE GLOBAL - CLINICAL AI WORKSTATION</span><div class="royal-h1">Precision Skin Health & Oncology Screening</div><div class="royal-p">High-clarity clinical interface powered by Deep Dermoscopy Vision & standardized ABCDE triage.</div></div>'
st.markdown(banner_html, unsafe_allow_html=True)

# 2. Top Status Strip
s1, s2, s3, s4 = st.columns(4)

c1_top = '<div class="white-card"><div class="card-tag">DIAGNOSTIC ENGINE</div><div style="color:#0284c7 !important; font-size:1.1rem; font-weight:800;">DermaNet-Pro v5</div></div>'
c2_top = '<div class="white-card"><div class="card-tag">CLINICAL ACCURACY</div><div style="color:#059669 !important; font-size:1.1rem; font-weight:800;">96.4% Sensitivity</div></div>'
c3_top = '<div class="white-card"><div class="card-tag">PROTOCOL</div><div style="color:#0f172a !important; font-size:1.1rem; font-weight:800;">Fitzpatrick + ABCDE</div></div>'
c4_top = '<div class="white-card"><div class="card-tag">STATUS</div><div style="color:#7c3aed !important; font-size:1.1rem; font-weight:800;">Ready - Real-Time</div></div>'

s1.markdown(c1_top, unsafe_allow_html=True)
s2.markdown(c2_top, unsafe_allow_html=True)
s3.markdown(c3_top, unsafe_allow_html=True)
s4.markdown(c4_top, unsafe_allow_html=True
