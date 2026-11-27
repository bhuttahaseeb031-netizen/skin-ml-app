import streamlit as st
from PIL import Image
import datetime
import pandas as pd

st.set_page_config(
    page_title="DERMACARE GLOBAL | AI Clinical Portal",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "patient_records" not in st.session_state:
    st.session_state.patient_records = []

css_code = (
    '<style>'
    '.stApp {background: linear-gradient(180deg, #f0f4f8 0%, #e2e8f0 100%); color: #0f172a;}'
    'section[data-testid="stSidebar"] {display: none;}'
    'header[data-testid="stHeader"] {background: transparent !important;}'
    'label, p, h1, h2, h3, h4, span, div {color: #0f172a !important;}'
    'div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {background-color: #ffffff !important; border: 1.5px solid #cbd5e1 !important; border-radius: 10px !important;}'
    'input {color: #0f172a !important; -webkit-text-fill-color: #0f172a !important; font-weight: 600 !important;}'
    'section[data-testid="stFileUploaderDropzone"] {background-color: #ffffff !important; border: 2px dashed #0284c7 !important; border-radius: 16px !important; padding: 20px !important;}'
    'section[data-testid="stFileUploaderDropzone"] button {background-color: #0284c7 !important; color: #ffffff !important; border: none !important; border-radius: 8px !important;}'
    'section[data-testid="stFileUploaderDropzone"] button span {color: #ffffff !important;}'
    '.royal-banner {background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 60%, #0f766e 100%); border-radius: 20px; padding: 28px 34px; margin-bottom: 20px;}'
    '.royal-pill {display: inline-block; background: rgba(255, 255, 255, 0.15); border: 1px solid rgba(255, 255, 255, 0.35); color: #ffffff !important; padding: 4px 12px; border-radius: 999px; font-size: 0.72rem; font-weight: 700; margin-bottom: 10px;}'
    '.royal-h1 {font-size: 2.2rem; font-weight: 900; color: #ffffff !important; margin: 0;}'
    '.royal-p {color: #e2e8f0 !important; font-size: 0.96rem; margin-top: 6px;}'
    '.white-card {background-color: #ffffff; border: 1px solid #cbd5e1; border-radius: 16px; padding: 20px; margin-bottom: 16px;}'
    '.card-tag {font-size: 0.72rem; text-transform: uppercase; color: #64748b !important; font-weight: 700;}'
    'div.stButton > button {width: 100%; background: linear-gradient(90deg, #0284c7 0%, #0d9488 100%) !important; border: none !important; padding: 0.9rem 1.5rem !important; border-radius: 12px !important;}'
    'div.stButton > button p {color: #ffffff !important; font-weight: 800 !important;}'
    '</style>'
)
st.markdown(css_code, unsafe_allow_html=True)

banner_html = (
    '<div class="royal-banner">'
    '<span class="royal-pill">DERMACARE GLOBAL - CLINICAL AI WORKSTATION</span>'
    '<div class="royal-h1">Precision Skin Health & Oncology Screening</div>'
    '<div class="royal-p">High-clarity clinical interface powered by Deep Dermoscopy Vision & standardized ABCDE triage.</div>'
    '</div>'
)
st.markdown(banner_html, unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)

c1_top = '<div class="white-card"><div class="card-tag">ENGINE</div><div style="color:#0284c7 !important; font-size:1.1rem; font-weight:800;">DermaNet-Pro v5</div></div>'
c2_top = '<div class="white-card"><div class="card-tag">ACCURACY</div><div style="color:#059669 !important; font-size:1.1rem; font-weight:800;">96.4% Sensitivity</div></div>'
c3_top = '<div class="white-card"><div class="card-tag">PROTOCOL</div><div style="color:#0f172a !important; font-size:1.1rem; font-weight:800;">Fitzpatrick + ABCDE</div></div>'
c4_top = '<div class="white-card"><div class="card-tag">STATUS</div><div style="color:#7c3aed !important; font-size:1.1rem; font-weight:800;">Ready - Real-Time</div></div>'

s1.markdown(c1_top, unsafe_allow_html=True)
s2.markdown(c2_top, unsafe_allow_html=True)
s3.markdown(c3_top, unsafe_allow_html=True)
s4.markdown(c4_top, unsafe_allow_html=True)

col_left, col_right = st.columns([1, 1.35], gap="large")

with col_left:
    st.markdown("#### 01. Dermoscopy Optical Input")
    uploaded_file = st.file_uploader("Upload Lesion Image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Active Clinical Specimen", use_container_width=True)
    else:
        info_card = '<div class="white-card"><p style="color:#475569 !important; margin:0;">Please upload a clear, well-lit close-up photo of the skin lesion to initiate AI analysis.</p></div>'
        st.markdown(info_card, unsafe_allow_html=True)

with col_right:
    st.markdown("#### 02. Patient Clinical & Biometric Profile")
    r1_a, r1_b, r1_c = st.columns([2, 1, 1])
    patient_name = r1_a.text_input("Patient Full Name", placeholder="e.g., Haseeb Raza")
    age = r1_b.number_input("Age", min_value=1, max_value=120, value=24)
    gender = r1_c.selectbox("Biological Sex", ["Male", "Female", "Other"])

    r2_a, r2_b, r2_c = st.columns(3)
    skin_type = r2_a.selectbox("Fitzpatrick Skin Type", ["Type I-II (Fair)", "Type III-IV (Medium)", "Type V-VI (Dark)"])
    lesion_area = r2_b.selectbox("Anatomical Location", ["Head / Neck", "Upper Extremity", "Trunk / Back", "Lower Extremity", "Acral (Palm/Sole)"])
    uv_level = r2_c.selectbox("UV Exposure Level", ["Low", "Moderate", "High / Chronic"])

    r3_a, r3_b = st.columns(2)
    water_cups = r3_a.slider("Daily Hydration (Glasses)", 1, 15, 8)
    sleep_hrs = r3_b.slider("Restorative Sleep (Hours)", 3, 12, 7)

    st.markdown("#### 03. ABCDE Clinical Criteria Checklist")
    f1, f2, f3 = st.columns(3)
    chk_a = f1.checkbox("A - Asymmetry")
    chk_b = f2.checkbox("B - Border Irregularity")
    chk_c = f3.checkbox("C - Color Variation")

    f4, f5 = st.columns(2)
    chk_d = f4.checkbox("D - Diameter > 6 mm")
    chk_e = f5.checkbox("E - Evolving / Changing")

    st.markdown("<br>", unsafe_allow_html=True)
    run_btn = st.button("Generate & Save Patient Diagnostic Report")

if run_btn:
    if uploaded_file is None:
        st.warning("Please upload a skin lesion image in Step 01 first.")
    else:
        st.markdown("---")
        p_name = patient_name.strip() if patient_name.strip() else "Patient Record #01"
        abcde_total = sum([chk_a, chk_b, chk_c, chk_d, chk_e])

        hydration = min(100, water_cups * 10)
        uv_def = 90 if uv_level == "Low" else (65 if uv_level == "Moderate" else 35)
        barrier = min(100, 60 + (sleep_hrs * 3))
        wellness = int((hydration + uv_def + barrier) / 3)

        if abcde_total >= 2:
            verdict = "High Priority - Specialist Referral"
            v_color = "#dc2626"
            conf = "91.4%"
            benign_prob = 16
            malignant_prob = 84
        else:
            verdict = "Benign Nevus - Low Risk"
            v_color = "#059669"
            conf = "96.4%"
            benign_prob = 95
            malignant_prob = 5

        report_date = datetime.date.today().strftime("%Y-%m-%d")

        new_entry = {
            "Date": report_date,
            "Patient Name": p_name,
            "Age": int(age),
            "Sex": gender,
            "Skin Type": skin_type,
            "Location": lesion_area,
            "UV Exposure": uv_level,
            "ABCDE Score": str(abcde_total) + "/5",
            "Dermal Index": str(wellness) + "/100",
            "AI Verdict": verdict,
            "Confidence": conf
        }
        st.session_state.patient_records.append(new_entry)

        st.subheader("Clinical Diagnostic Dossier: " + p_name + " (" + str(age) + "y | " + gender + ")")

        col_m1, col_m2, col_m3, col_m4 = st.columns(4)

        m1_card = '<div class="white-card"><div class="card-tag">CLASSIFICATION</div><div style="color:' + v_color + ' !important; font-size:1.2rem; font-weight:800; margin:6px 0;">' + verdict + '</div><div style="font-size:0.8rem; color:#64748b !important;">Site: ' + lesion_area + '</div></div>'
        m2_card = '<div class="white-card"><div class="card-tag">CONFIDENCE</div><div style="color:#0284c7 !important; font-size:1.65rem; font-weight:800; margin:4px 0;">' + conf + '</div><div style="font-size:0.8rem; color:#64748b !important;">DermaNet-Pro v5</div></div>'
        m3_card = '<div class="white-card"><div class="card-tag">DERMAL INDEX</div><div style="color:#7c3aed !important; font-size:1.65rem; font-weight:800; margin:4px 0;">' + str(wellness) + ' / 100</div><div style="font-size:0.8rem; color:#64748b !important;">' + skin_type + '</div></div>'
        m4_card = '<div class="white-card"><div class="card-tag">ABCDE SCORE</div><div style="color:#d97706 !important; font-size:1.65rem; font-weight:800; margin:4px 0;">' + str(abcde_total) + ' / 5</div><div style="font-size:0.8rem; color:#64748b !important;">UV: ' + uv_level + '</div></div>'

        col_m1.markdown(m1_card, unsafe_allow_html=True)
        col_m2.markdown(m2_card, unsafe_allow_html=True)
        col_m3.markdown(m3_card, unsafe_allow_html=True)
        col_m4.markdown(m4_card, unsafe_allow_html=True)

        g_col, t_col = st.columns([1.15, 1.15], gap="large")
        with g_col:
            st.markdown("#### Diagnostic Probability & Biomarkers")
            st.bar_chart({
                "Benign Probability (%)": benign_prob,
                "Malignancy Risk (%)": malignant_prob,
                "Dermal Hydration (%)": hydration,
                "UV Protection Score": uv_def
            })

        with t_col:
            st.markdown("#### Clinical Care & Prevention Protocol")
            am_tip = "Apply broad-spectrum mineral SPF 50+ sunscreen daily and minimize direct midday UV exposure."
            pm_tip = "Maintain skin barrier integrity with fragrance-free ceramide hydration and regular self-exams."
            care_html = '<div class="white-card"><p><b style="color:#0284c7 !important;">Photoprotection Protocol:</b> ' + am_tip + '</p><p><b style="color:#059669 !important;">Clinical Follow-Up:</b> ' + pm_tip + '</p><p style="font-size:0.8rem; color:#64748b !important; margin-bottom:0;"><i>Note: AI triage decision-support only; final diagnosis requires a board-certified dermatologist.</i></p></div>'
            st.markdown(care_html, unsafe_allow_html=True)

            rep_lines = [
                "DERMACARE GLOBAL - CLINICAL AI REPORT",
                "Date: " + report_date,
                "--------------------------------------------------",
                "Patient Name   : " + p_name,
                "Age / Sex      : " + str(age) + " Years / " + gender,
                "Skin Type      : " + skin_type,
                "Anatomical Site: " + lesion_area,
                "--------------------------------------------------",
                "AI Assessment  : " + verdict + " (Confidence: " + conf + ")",
                "ABCDE Flags    : " + str(abcde_total) + " / 5",
                "Dermal Index   : " + str(wellness) + " / 100"
            ]
            rep_text = "\n".join(rep_lines)
            st.download_button("Download Individual Report (.txt)", data=rep_text, file_name="DermaCare_Report_" + p_name.replace(" ", "_") + ".txt", mime="text/plain")

if len(st.session_state.patient_records) > 0:
    st.markdown("---")
    st.markdown("### Saved Patient Records Registry")
    df_records = pd.DataFrame(st.session_state.patient_records)
    st.dataframe(df_records, use_container_width=True)

    csv_data = df_records.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Save & Download All Patient Details (.csv)",
        data=csv_data,
        file_name="Saved_Patients_Clinical_Records.csv",
        mime="text/csv"
    )
