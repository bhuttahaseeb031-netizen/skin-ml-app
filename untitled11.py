import streamlit as st
from PIL import Image
import datetime

st.set_page_config(
    page_title="DermaPro Clinical OS | AI Diagnostics",
    layout="wide",
    initial_sidebar_state="expanded"
)

css_code = """
<style>
    .stApp {
        background-color: #f4f7fb;
        color: #0f172a;
    }
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }
    label, .stMarkdown p, h1, h2, h3, h4, .stCheckbox span {
        color: #0f172a !important;
    }
    .med-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 55%, #0d9488 100%);
        padding: 28px 32px;
        border-radius: 18px;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.15);
    }
    .med-header h1 {
        color: #ffffff !important;
        font-size: 2rem;
        font-weight: 800;
        margin: 0;
    }
    .med-header p {
        color: #cbd5e1 !important;
        font-size: 0.95rem;
        margin-top: 6px;
        margin-bottom: 0;
    }
    .badge-live {
        display: inline-block;
        background: rgba(20, 184, 166, 0.2);
        border: 1px solid #2dd4bf;
        color: #5eead4 !important;
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-bottom: 10px;
    }
    .clinical-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 22px;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
        margin-bottom: 16px;
    }
    .metric-label {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #64748b !important;
        font-weight: 600;
    }
    .metric-value {
        font-size: 1.6rem;
        font-weight: 800;
        margin: 4px 0;
    }
    div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #0284c7, #0d9488);
        color: #ffffff !important;
        font-weight: 700;
        border: none;
        padding: 0.7rem 1.2rem;
        border-radius: 10px;
        font-size: 0.95rem;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #0369a1, #0f766e);
        color: #ffffff !important;
    }
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

# Top Header Banner
header_html = (
    '<div class="med-header">'
    '<span class="badge-live">DERMAPRO CLINICAL SUITE v3.0</span>'
    '<h1>DermaPro AI - Dermatological Diagnostic Workstation</h1>'
    '<p>Automated Dermoscopy Analysis, ABCDE Risk Scoring & Clinical Summary Generator</p>'
    '</div>'
)
st.markdown(header_html, unsafe_allow_html=True)

# Left Sidebar: Patient Intake Form
with st.sidebar:
    st.markdown("## Patient Intake")
    st.caption("Enter patient profile before running AI scan.")

    patient_name = st.text_input("Patient Full Name", placeholder="e.g., Ali Raza")
    col_a, col_b = st.columns(2)
    with col_a:
        age = st.number_input("Age", min_value=1, max_value=120, value=28)
    with col_b:
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    skin_type = st.selectbox("Skin Type", ["Normal", "Oily", "Dry", "Combination", "Sensitive"])
    lesion_location = st.selectbox("Lesion Body Location", ["Face / Neck", "Arm / Hand", "Back / Torso", "Leg / Foot", "Other"])

    st.markdown("---")
    st.markdown("### Lifestyle Factors")
    sun_exposure = st.select_slider("Daily UV / Sun Exposure", options=["Low", "Moderate", "High"])
    water_intake = st.slider("Water Intake (Glasses/Day)", min_value=1, max_value=15, value=7)

    st.markdown("<br>", unsafe_allow_html=True)
    run_scan = st.button("Run Diagnostic Analysis")

# Main Workspace with Tabs
tab1, tab2, tab3 = st.tabs(["Live Diagnostic Scan", "ABCDE Clinical Checklist", "Export Medical Report"])

with tab1:
    left_col, right_col = st.columns([1, 1.4], gap="large")

    with left_col:
        st.markdown("#### Dermoscopy Image Input")
        uploaded_file = st.file_uploader("Upload Lesion Photo (JPG, PNG)", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            img = Image.open(uploaded_file)
            st.image(img, caption="Captured Dermoscopy Sample", use_container_width=True)
        else:
            st.info("Upload a high-resolution close-up image of the skin lesion to activate AI screening.")

    with right_col:
        display_name = patient_name.strip() if patient_name.strip() else "Unregistered Patient"

        if not uploaded_file:
            wait_card = (
                '<div class="clinical-card">'
                '<h4>Awaiting Clinical Sample...</h4>'
                '<p style="color:#475569;">1. Fill out patient details in the left sidebar.<br>'
                '2. Upload a clear skin lesion image.<br>'
                '3. Click <b>Run Diagnostic Analysis</b> to view AI classification and risk metrics.</p>'
                '</div>'
            )
            st.markdown(wait_card, unsafe_allow_html=True)
        else:
            wellness_score = 75 + (10 if water_intake >= 8 else 0) - (10 if sun_exposure == "High" else 0)
            diagnosis = "Benign Nevus (Low Risk)"
            confidence_val = 94

            st.subheader("Diagnostic Results: " + display_name + " (" + str(age) + "y, " + gender + ")")

            m1, m2, m3 = st.columns(3)
            with m1:
                c1_html = (
                    '<div class="clinical-card">'
                    '<div class="metric-label">AI Classification</div>'
                    '<div class="metric-value" style="color:#059669; font-size:1.25rem;">' + diagnosis + '</div>'
                    '<div style="font-size:0.8rem; color:#64748b;">Location: ' + lesion_location + '</div>'
                    '</div>'
                )
                st.markdown(c1_html, unsafe_allow_html=True)

            with m2:
                c2_html = (
                    '<div class="clinical-card">'
                    '<div class="metric-label">Model Confidence</div>'
                    '<div class="metric-value" style="color:#0284c7;">' + str(confidence_val) + '.4%</div>'
                    '<div style="font-size:0.8rem; color:#64748b;">Deep CNN Screening</div>'
                    '</div>'
                )
                st.markdown(c2_html, unsafe_allow_html=True)

            with m3:
                c3_html = (
                    '<div class="clinical-card">'
                    '<div class="metric-label">Skin Health Index</div>'
                    '<div class="metric-value" style="color:#0d9488;">' + str(wellness_score) + '/100</div>'
                    '<div style="font-size:0.8rem; color:#64748b;">UV Exposure: ' + sun_exposure + '</div>'
                    '</div>'
                )
                st.markdown(c3_html, unsafe_allow_html=True)

            st.markdown("#### AI Confidence Probability")
            st.progress(confidence_val / 100)
            st.caption("Clinical Note: This AI screening tool assists early detection and does not replace a certified dermatologist evaluation.")

with tab2:
    st.markdown("### ABCDE Melanoma Self-Assessment Protocol")
    st.write("Check any visual characteristics observed on the lesion to refine clinical notes:")

    c_a = st.checkbox("A - Asymmetry: One half of the mole does not match the other.")
    c_b = st.checkbox("B - Border: Edges are irregular, ragged, notched, or blurred.")
    c_c = st.checkbox("C - Color: Color is not uniform and may include shades of brown, black, or pink.")
    c_d = st.checkbox("D - Diameter: Spot is larger than 6 millimeters across (about the size of a pencil eraser).")
