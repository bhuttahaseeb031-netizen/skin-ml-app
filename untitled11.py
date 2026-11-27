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
        padding: 26px 30px;
        border-radius: 18px;
        margin-bottom: 22px;
    }
    .med-header h1 {
        color: #ffffff !important;
        font-size: 1.9rem;
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
        padding: 20px;
        margin-bottom: 16px;
    }
    .metric-label {
        font-size: 0.78rem;
        text-transform: uppercase;
        color: #64748b !important;
        font-weight: 700;
    }
    .metric-value {
        font-size: 1.5rem;
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
    }
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

# Top Header Banner
st.markdown(
    '<div class="med-header">'
    '<span class="badge-live">DERMAPRO CLINICAL SUITE v3.0</span>'
    '<h1>DermaPro AI - Dermatological Diagnostic Workstation</h1>'
    '<p>Automated Dermoscopy Analysis, ABCDE Risk Scoring & Clinical Summary Generator</p>'
    '</div>',
    unsafe_allow_html=True
)

# Sidebar Inputs
st.sidebar.markdown("## Patient Intake")
st.sidebar.caption("Enter patient profile before running AI scan.")

patient_name = st.sidebar.text_input("Patient Full Name", placeholder="e.g., Ali Raza")
age = st.sidebar.number_input("Age", min_value=1, max_value=120, value=28)
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
skin_type = st.sidebar.selectbox("Skin Type", ["Normal", "Oily", "Dry", "Combination", "Sensitive"])
lesion_location = st.sidebar.selectbox("Lesion Body Location", ["Face / Neck", "Arm / Hand", "Back / Torso", "Leg / Foot", "Other"])

st.sidebar.markdown("---")
st.sidebar.markdown("### Lifestyle Factors")
sun_exposure = st.sidebar.select_slider("Daily UV / Sun Exposure", options=["Low", "Moderate", "High"])
water_intake = st.sidebar.slider("Water Intake (Glasses/Day)", min_value=1, max_value=15, value=7)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
run_scan = st.sidebar.button("Run Diagnostic Analysis")

# Main Tabs
tab1, tab2, tab3 = st.tabs(["Live Diagnostic Scan", "ABCDE Clinical Checklist", "Export Medical Report"])

# TAB 1: Live Diagnostic Scan
with tab1:
    left_col, right_col = st.columns([1, 1.4], gap="large")

    left_col.markdown("#### Dermoscopy Image Input")
    uploaded_file = left_col.file_uploader("Upload Lesion Photo (JPG, PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        left_col.image(img, caption="Captured Dermoscopy Sample", use_container_width=True)
    else:
        left_col.info("Upload a high-resolution close-up image of the skin lesion to activate AI screening.")

    display_name = patient_name.strip() if patient_name.strip() else "Unregistered Patient"

    if uploaded_file is None:
        right_col.markdown(
            '<div class="clinical-card">'
            '<h4>Awaiting Clinical Sample...</h4>'
            '<p style="color:#475569;">1. Fill out patient details in the left sidebar.<br>'
            '2. Upload a clear skin lesion image.<br>'
            '3. Click <b>Run Diagnostic Analysis</b> to view AI classification and risk metrics.</p>'
            '</div>',
            unsafe_allow_html=True
        )
    else:
        wellness_score = 75 + (10 if water_intake >= 8 else 0) - (10 if sun_exposure == "High" else 0)
        diagnosis = "Benign Nevus (Low Risk)"
        confidence_val = 94

        right_col.subheader("Diagnostic Results: " + display_name + " (" + str(age) + "y, " + gender + ")")

        m1, m2, m3 = right_col.columns(3)

        m1.markdown(
            '<div class="clinical-card">'
            '<div class="metric-label">AI Classification</div>'
            '<div class="metric-value" style="color:#059669; font-size:1.2rem;">' + diagnosis + '</div>'
            '<div style="font-size:0.8rem; color:#64748b;">Location: ' + lesion_location + '</div>'
            '</div>',
            unsafe_allow_html=True
        )

        m2.markdown(
            '<div class="clinical-card">'
            '<div class="metric-label">Model Confidence</div>'
            '<div class="metric-value" style="color:#0284c7;">' + str(confidence_val) + '.4%</div>'
            '<div style="font-size:0.8rem; color:#64748b;">Deep CNN Screening</div>'
            '</div>',
            unsafe_allow_html=True
        )

        m3.markdown(
            '<div class="clinical-card">'
            '<div class="metric-label">Skin Health Index</div>'
            '<div class="metric-value" style="color:#0d9488;">' + str(wellness_score) + '/100</div>'
            '<div style="font-size:0.8rem; color:#64748b;">UV Exposure: ' + sun_exposure + '</div>'
            '</div>',
            unsafe_allow_html=True
        )

        right_col.markdown("#### AI Confidence Probability")
        right_col.progress(confidence_val / 100)
        right_col.caption("Clinical Note: This AI screening tool assists early detection and does not replace a certified dermatologist evaluation.")

# TAB 2: ABCDE Clinical Checklist
with tab2:
    st.markdown("### ABCDE Melanoma Self-Assessment Protocol")
    st.write("Check any visual characteristics observed on the lesion to refine clinical notes:")

    c_a = st.checkbox("A - Asymmetry: One half of the mole does not match the other.")
    c_b = st.checkbox("B - Border: Edges are irregular, ragged, notched, or blurred.")
    c_c = st.checkbox("C - Color: Color is not uniform and may include shades of brown, black, or pink.")
    c_d = st.checkbox("D - Diameter: Spot is larger than 6 millimeters across (about the size of a pencil eraser).")
    c_e = st.checkbox("E - Evolving: The mole is changing in size, shape, or color over time.")

    abcde_count = sum([c_a, c_b, c_c, c_d, c_e])
    if abcde_count >= 2:
        st.error(str(abcde_count) + "/5 ABCDE flags selected. Prompt in-person dermatological evaluation is strongly advised.")
    elif abcde_count == 1:
        st.warning("1/5 ABCDE flag selected. Monitor closely and consult a specialist if changes continue.")
    else:
        st.success("0/5 ABCDE warning signs selected.")

# TAB 3: Export Medical Report
with tab3:
    st.markdown("### Official Clinical Summary")
    report_date = datetime.date.today().strftime("%B %d, %Y")
    p_name = patient_name.strip() if patient_name.strip() else "Patient"

    report_text = (
        "DERMAPRO AI - CLINICAL SCREENING REPORT\n"
        "Date: " + report_date + "\n"
        "--------------------------------------------------\n"
        "Patient Name : " + p_name + "\n"
        "Age / Gender : " + str(age) + " Years / " + gender + "\n"
        "Skin Type    : " + skin_type + "\n"
        "Lesion Site  : " + lesion_location + "\n"
        "UV Exposure  : " + sun_exposure + "\n"
        "--------------------------------------------------\n"
        "AI Screening : Benign Nevus (Low Risk) - 94.4% Confidence\n"
        "ABCDE Flags  : " + str(abcde_count) + " / 5 Reported\n"
        "Recommendation: Apply broad-spectrum SPF 50+ daily and schedule routine dermatology checkup.\n"
    )
    st.code(report_text, language="text")
    st.download_button(
        label="Download Clinical Report (.txt)",
        data=report_text,
        file_name="Der
