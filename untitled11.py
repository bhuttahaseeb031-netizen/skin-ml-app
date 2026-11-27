import streamlit as st
from PIL import Image
import numpy as np
from datetime import datetime
from fpdf import FPDF

# 1. Page Configuration
st.set_page_config(
    page_title="DERMACARE GLOBAL | AI Clinical Portal",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Dark Clinical Portal CSS (High Contrast & Zero Glitches)
css_code = """
<style>
.stApp {
    background: radial-gradient(circle at 15% 15%, #0f172a 0%, #090d16 55%, #030712 100%);
    color: #f8fafc;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

section[data-testid="stSidebar"] {
    display: none;
}

header[data-testid="stHeader"] {
    background: transparent !important;
}

label, p, h1, h2, h3, h4, span {
    color: #f1f5f9 !important;
}

/* Portal Header Banner */
.portal-header {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 55%, #0284c7 100%);
    border: 1px solid rgba(56, 189, 248, 0.35);
    border-radius: 20px;
    padding: 26px 32px;
    margin-bottom: 24px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
}
.portal-badge {
    display: inline-block;
    background: rgba(56, 189, 248, 0.2);
    border: 1px solid rgba(56, 189, 248, 0.5);
    color: #7dd3fc !important;
    font-size: 0.78rem;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 999px;
    letter-spacing: 0.06em;
}
.portal-title {
    color: #ffffff !important;
    font-size: 2.1rem;
    font-weight: 800;
    margin: 8px 0 4px 0;
}

/* Clinical Cards */
.clinical-panel {
    background: rgba(15, 23, 42, 0.72);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid rgba(148, 163, 184, 0.2);
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.45);
}
.panel-heading {
    color: #38bdf8 !important;
    font-size: 1.15rem;
    font-weight: 700;
    margin-bottom: 16px;
    border-bottom: 1px solid rgba(56, 189, 248, 0.25);
    padding-bottom: 8px;
}

/* Inputs & Select Boxes */
div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {
    background-color: #0f172a !important;
    border: 1.5px solid #334155 !important;
    border-radius: 10px !important;
    color: #f8fafc !important;
}
input {
    color: #f8fafc !important;
    -webkit-text-fill-color: #f8fafc !important;
    font-weight: 600 !important;
}

/* Primary Action Button */
div.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #0284c7 0%, #2563eb 100%);
    color: #ffffff !important;
    font-weight: 700;
    border: none;
    padding: 0.8rem 1.4rem;
    border-radius: 12px;
    font-size: 1.02rem;
    box-shadow: 0 8px 22px rgba(37, 99, 235, 0.35);
}

/* PDF Download Button */
div.stDownloadButton > button {
    width: 100%;
    background: linear-gradient(9
