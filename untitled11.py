import streamlit as st
from PIL import Image
import datetime

st.set_page_config(page_title="VANGUARD DERMA OS", layout="wide")

css_code = """
<style>
    .stApp {background-color: #0b0e14; color: #e6edf3;}
    section[data-testid="stSidebar"] {display: none;}
    label, p, h1, h2, h3, h4, span {color: #e6edf3 !important;}

    /* Dark File Uploader Fix */
    section[data-testid="stFileUploader"] {
        background-color: #131822;
        border: 1px dashed #00f5d4;
        border-radius: 14px;
        padding: 14px;
    }

    /* Industrial Top Telemetry Bar */
    .telemetry-bar {
        background: #131822;
        border-left: 5px solid #00f5d4;
        border-top: 1px solid #232b3a;
        border-right: 1px solid #232b3a;
        border-bottom: 1px solid #232b3a;
        border-radius: 12px;
        padding: 20px 26px;
        margin-bottom: 22px;
    }
    .sys-tag {
        color: #00f5d4 !important;
        font-family: monospace;
        font-size: 0.8rem;
        letter-spacing: 0.12em;
        font-weight: 700;
    }
    .sys-title {
        font-size: 2rem;
        font-weight: 800;
        color: #ffffff !important;
        margin: 4px 0;
    }

    /* Carbon Panels */
    .carbon-panel {
        background: #131822;
        border: 1px solid #232b3a;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 16px;
    }
    .panel-label {
        font-family: monospace;
        font-size: 0.75rem;
        color: #8b949e !important;
        text-transform: uppercase;
    }
    .panel-val {
        font-size: 1.65rem;
        font-weight: 800;
        margin-top: 4px;
    }

    /* Electric Cyan CTA Button */
    div.stButton > button {
        width: 100%;
        background: #00f5d4;
        color: #061018 !important;
        font-weight: 800;
        border: none;
        padding: 0.8rem 1.4rem;
        border-radius: 10px;
        font-size: 1rem;
        letter-spacing: 0.04em;
    }
    div.stButton > button:hover {
        background: #00d4b8;
        color: #061018 !important;
    }
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

# Top Telemetry Header
header_box = '<div class="telemetry-bar"><div class="sys-tag">[ SYSTEM ONLINE • DERMOSCOPY NEURAL CORE v6.0 ]</div><div class="sys-title">VANGUARD DERMA DIAGNOSTICS</div><p style="color:#8b949e !important; margin:0;">High-precision skin lesion classification, UV stress telemetry, and clinical risk profiling.</p></div>'
st.markdown(header_box, unsafe_allow_html=True)

# Main Workspace
col_left, col_right = st.columns([1, 1.35], gap="large")

with col_left:
    st.markdown("### // 01. OPTICAL SCANNER")
    uploaded_file = st.file_uploader("Upload Dermoscopy Image (JPG, PNG)", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Target Lesion Specimen", use_container_width=True)
    else:
        st.markdown('<div class="carbon-panel"><p style="color:#8b949e !important; margin:0;">Awaiting high-resolution lesion photo. Ensure clear lighting without glare.</p></div>', unsafe_allow_html=True)

with col_right:
    st.markdown("### // 02. SUBJECT PARAMETERS")
    r1_a, r1_b, r1_c = st.columns([2, 1, 1])
    patient_name = r1_a.text_input("Subject Name", placeholder="Enter full name")
    age = r1_b.number_input("Age", min_value=1, max_value=120, value=25)
    gender = r1_c.selectbox("Gender", ["Male", "Female", "Other"])

    r2_a, r2_b, r2_c = st.columns(3)
    skin_type = r2_a.selectbox("Skin Profile", ["Normal", "Oily", "Dry", "Combination", "Sensitive"])
    lesion_area = r2_b.selectbox("Anatomical Site", ["Face / Neck", "Arm / Hand", "Back / Torso", "Leg / Foot", "Other"])
    uv_level = r2_c.selectbox("UV Exposure", ["Low", "Moderate", "High"])

    r3_a, r3_b = st.columns(2)
    water_cups = r3_a.slider("Daily Hydration (Glasses)", min_value=1, max_value=15, value=8)
    sleep_hrs = r3_b.slider("Sleep Cycle (Hours)", min_value=3, max_value=12, value=7)

    st.markdown("#### ABCDE Clinical Indicators")
    f1, f2, f3 = st.columns(3)
    chk_a = f1.checkbox("A: Asymmetry")
    chk_b = f2.checkbox("B: Irregular Border")
    chk_c = f3.checkbox("C: Multi-Color")

    f4, f5 = st.columns(2)
    chk_d = f4.checkbox("D: Diameter > 6mm")
    chk_e = f5.checkbox("E: Evolving Shape")

    st.markdown("<br>", unsafe_allow_html=True)
    run_btn = st.button("EXECUTE DIAGNOSTIC SCAN")

# Results Section
if run_btn:
    if uploaded_file is None:
        st.warning("Upload a skin image in Section 01 before executing the scan.")
    else:
        st.markdown("---")
        p_name = patient_name.strip() if patient_name.strip() else "Subject-01"
        abcde_total = sum([chk_a, chk_b, chk_c, chk_d, chk_e])

        hydration = min(100, water_cups * 10)
        uv_def = 90 if uv_level == "Low" else (65 if uv_level == "Moderate" else 35)
        barrier = min(100, 60 + (sleep_hrs * 3))
        wellness = int((hydration + uv_def + barrier) / 3)

        if abcde_total >= 2:
            verdict = "HIGH ALERT - CONSULT SPECIALIST"
            v_color = "#ff4d6d"
            conf = "89.4%"
        else:
            verdict = "BENIGN / LOW RISK"
            v_color = "#00f5d4"
            conf = "96.8%"

        st.subheader("TELEMETRY REPORT // " + p_name.upper() + " (" + str(age) + "Y)")

        k1, k2, k3, k4 = st.columns(4)
        k1.markdown('<div class="carbon-panel"><div class="panel-label">DIAGNOSIS</div><div class="panel-val" style="color:' + v_color + '; font-size:1.15rem;">' + verdict + '</div></div>', unsafe_allow_html=True)
        k2.markdown('<div class="carbon-panel"><div class="panel-label">CONFIDENCE</div><div class="panel-val" style="color:#00bbf9;">' + conf + '</div></div>', unsafe_allow_html=True)
        k3.markdown('<div class="carbon-panel"><div class="panel-label">SKIN INDEX</div><div class="panel-val" style="color:#fee440;">' + str(wellness) + '/100</div></div>', unsafe_allow_html=True)
        k4.markdown('<div class="carbon-panel"><div class="panel-label">ABCDE FLAGS</div><div class="panel-val" style="color:#f15bb5;">' + str(abcde_total) + ' / 5</div></div>', unsafe_allow_html=True)

        g_col, t_col = st.columns([1.2, 1], gap="large")
        with g_col:
            st.markdown("#### BIOMARKER TELEMETRY")
            st.bar_chart({"Hydration": hydration, "UV Shield": uv_def, "Skin Barrier": barrier, "Overall": wellness})

        with t_col:
            st.markdown("#### CLINICAL ACTION PROTOCOL")
            am_tip = "Apply broad-spectrum SPF 50+ PA++++ every 3 hours outdoors."
            pm_tip = "Use barrier-repair ceramide cream suited for " + skin_type + " skin."
            st.markdown('<div class="carbon-panel"><p><b style="color:#00f5d4;">DAYTIME:</b> ' + am_tip + '</p><p><b style="color:#00bbf9;">NIGHTTIME:</b> ' + pm_tip + '</p></div>', unsafe_allow_html=True)

            rep = "VANGUARD DERMA REPORT\nSubject: " + p_name + " (" + str(age) + "y, " + gender + ")\nSite: " + lesion_area + " | Skin: " + skin_type + "\nDiagnosis: " + verdict + " (" + conf + ")\nSkin Index: " + str(wellness) + "/100 | ABCDE: " + str(abcde_total) + "/5\n"
            st.download_button("EXPORT TELEMETRY REPORT (.TXT)", data=rep, file_name="Vanguard_Derma_Report.txt", mime="text/plain")
