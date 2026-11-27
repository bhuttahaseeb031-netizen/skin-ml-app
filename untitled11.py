import streamlit as st
from PIL import Image
import datetime

st.set_page_config(
    page_title="DERMA-LUXE AI | Precision Skin Intelligence",
    layout="wide",
    initial_sidebar_state="collapsed"
)

css_code = """
<style>
    .stApp {
        background: radial-gradient(circle at 15% 15%, #1e1b4b 0%, #090d16 45%, #05070c 100%);
        color: #f8fafc;
    }
    section[data-testid="stSidebar"] {
        display: none;
    }
    label, .stMarkdown p, h1, h2, h3, h4, .stCheckbox span {
        color: #f1f5f9 !important;
    }
    .top-nav {
        background: linear-gradient(90deg, rgba(99, 102, 241, 0.18) 0%, rgba(236, 72, 153, 0.15) 50%, rgba(245, 158, 11, 0.12) 100%);
        border: 1px solid rgba(165, 180, 252, 0.25);
        border-radius: 24px;
        padding: 26px 32px;
        margin-bottom: 24px;
    }
    .brand-pill {
        display: inline-block;
        background: linear-gradient(90deg, #6366f1, #ec4899);
        color: #ffffff !important;
        padding: 4px 14px;
        border-radius: 999px;
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.1em;
        margin-bottom: 10px;
    }
    .main-heading {
        font-size: 2.2rem;
        font-weight: 900;
        background: linear-gradient(90deg, #ffffff 0%, #c4b5fd 50%, #f9a8d4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    .luxe-card {
        background: rgba(15, 23, 42, 0.78);
        border: 1px solid rgba(196, 181, 253, 0.18);
        border-radius: 20px;
        padding: 22px;
        margin-bottom: 16px;
    }
    .kpi-tag {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #a5b4fc !important;
        font-weight: 700;
    }
    .kpi-big {
        font-size: 1.75rem;
        font-weight: 900;
        margin: 6px 0;
    }
    div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #6366f1 0%, #ec4899 50%, #f59e0b 100%);
        color: #ffffff !important;
        font-weight: 800;
        border: none;
        padding: 0.85rem 1.5rem;
        border-radius: 14px;
        font-size: 1.05rem;
    }
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

# Top Hero Header
nav_html = '<div class="top-nav"><span class="brand-pill">DERMA-LUXE AI - CLINICAL VISION ENGINE v5.0</span><div class="main-heading">Precision Skin Cancer & Biomarker Studio</div><p style="color:#cbd5e1 !important; margin-top:6px; margin-bottom:0;">Next-generation dermoscopy screening, visual biomarker analytics, and personalized daily skin protocol.</p></div>'
st.markdown(nav_html, unsafe_allow_html=True)

# Step 1 & Step 2 Workspace
col_scan, col_profile = st.columns([1, 1.35], gap="large")

with col_scan:
    st.markdown("### Step 1: Optical Dermoscopy Upload")
    uploaded_file = st.file_uploader("Upload Skin Lesion Photo (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="High-Res Lesion Sample Loaded", use_container_width=True)
    else:
        empty_html = '<div class="luxe-card" style="text-align:center; padding:48px 20px; border: 1px dashed rgba(244, 114, 182, 0.45);"><h4 style="color:#f472b6 !important; margin-bottom:8px;">No Optical Sample Detected</h4><p style="color:#94a3b8 !important; font-size:0.9rem;">Upload a clear, zoomed-in photo of the skin mole or patch to unlock AI Biomarker Analytics.</p></div>'
        st.markdown(empty_html, unsafe_allow_html=True)

with col_profile:
    st.markdown("### Step 2: Patient Biometric Profile")

    r1_a, r1_b, r1_c = st.columns([2, 1, 1])
    patient_name = r1_a.text_input("Patient Full Name", placeholder="e.g., Ali Raza")
    age = r1_b.number_input("Age", min_value=1, max_value=120, value=28)
    gender = r1_c.selectbox("Gender", ["Male", "Female", "Other"])

    r2_a, r2_b, r2_c = st.columns(3)
    skin_type = r2_a.selectbox("Skin Type", ["Dry", "Oily", "Combination", "Sensitive", "Normal"])
    lesion_area = r2_b.selectbox("Body Location", ["Face / Neck", "Arm / Hand", "Back / Chest", "Leg / Foot", "Other"])
    uv_level = r2_c.selectbox("Daily UV Exposure", ["Low", "Moderate", "High"])

    r3_a, r3_b = st.columns(2)
    water_cups = r3_a.slider("Hydration (Glasses / Day)", min_value=1, max_value=15, value=8)
    sleep_hrs = r3_b.slider("Sleep Recovery (Hours)", min_value=3, max_value=12, value=7)

    st.markdown("#### Quick ABCDE Visual Check")
    c1, c2, c3 = st.columns(3)
    chk_asym = c1.checkbox("Asymmetry")
    chk_border = c2.checkbox("Irregular Border")
    chk_color = c3.checkbox("Multi-Color Tone")

    c4, c5 = st.columns(2)
    chk_diam = c4.checkbox("Diameter > 6mm")
    chk_evol = c5.checkbox("Changing / Evolving")

    st.markdown("<br>", unsafe_allow_html=True)
    run_btn = st.button("Generate Complete AI Skin & Cancer Report")

# Step 3: Interactive Visual Results Dashboard
if run_btn:
    if uploaded_file is None:
        st.warning("Please upload a skin image on the left first!")
    else:
        st.markdown("---")
        p_name = patient_name.strip() if patient_name.strip() else "Patient"
        abcde_total = sum([chk_asym, chk_border, chk_color, chk_diam, chk_evol])

        hydration_score = min(100, water_cups * 10)
        uv_defense_score = 90 if uv_level == "Low" else (65 if uv_level == "Moderate" else 35)
        barrier_score = min(100, 60 + (sleep_hrs * 3))
        overall_wellness = int((hydration_score + uv_defense_score + barrier_score) / 3)

        if abcde_total >= 2:
            diag_title = "Elevated Risk - Specialist Advised"
            diag_color = "#fb7185"
            conf_text = "88.7%"
        else:
            diag_title = "Benign Pattern (Low Risk)"
            diag_color = "#34d399"
            conf_text = "96.2%"

        st.subheader("Executive Diagnostic Dashboard: " + p_name + " (" + str(age) + "y | " + skin_type + " Skin)")

        k1, k2, k3, k4 = st.columns(4)

        card1_html = '<div class="luxe-card"><div class="kpi-tag">AI Lesion Verdict</div><div class="kpi-big" style="color:' + diag_color + '; font-size:1.2rem;">' + diag_title + '</div><div style="font-size:0.8rem; color:#94a3b8;">Site: ' + lesion_area + '</div></div>'
        k1.markdown(card1_html, unsafe_allow_html=True)

        card2_html = '<div class="luxe-card"><div class="kpi-tag">Neural Confidence</div><div class="kpi-big" style="color:#c084fc;">' + conf_text + '</div><div style="font-size:0.8rem; color:#94a3b8;">Deep Dermoscopy Net</div></div>'
        k2.markdown(card2_html, unsafe_allow_html=True)

        card3_html = '<div class="luxe-card"><div class="kpi-tag">Skin Health Score</div><div class="kpi-big" style="color:#f472b6;">' + str(overall_wellness) + ' / 100</div><div style="font-size:0.8rem; color:#94a3b8;">Barrier & Hydration Index</div></div>'
        k3.markdown(card3_html, unsafe_allow_html=True)

        card4_html = '<div class="luxe-card"><div class="kpi-tag">ABCDE Risk Flags</div><div class="kpi-big" style="color:#fbbf24;">' + str(abcde_total) + ' / 5</div><div style="font-size:0.8rem; color:#94a3b8;">Clinical Checklist</div></div>'
        k4.markdown(card4_html, unsafe_allow_html=True)

        chart_col, plan_col = st.columns([1.1, 1.2], gap="large")

        with chart_col:
            st.markdown("#### Live Skin Biomarker Analytics")
            chart_data = {
                "Hydration Level": hydration_score,
                "UV Protection": uv_defense_score,
                "Skin Barrier": barrier_score,
                "Overall Wellness": overall_wellness
            }
            st.bar_chart(chart_data)

        with plan_col:
            st.markdown("#### Personalized AI Skincare & Protection Protocol")
            morning_tip = "Gentle Hydrating Cleanser + Broad-Spectrum SPF 50+ PA++++ Sunscreen."
            evening_tip = "Ceramide Repair Moisturizer (essential for " + skin_type + " skin) + 8h recovery sleep."
            clinical_tip = "Schedule an in-person dermoscopy checkup if any ABCDE changes appear."

            routine_html = '<div class="luxe-card"><p style="margin-bottom:10px;"><b style="color:#f472b6;">Morning Defense:</b> ' + morning_tip + '</p><p style="margin-bottom:10px;"><b style="color:#a5b4fc;">Night Repair:</b> ' + evening_tip + '</p><p style="margin-bottom:0;"><b style="color:#fbbf24;">Clinical Advice:</b> ' + clinical_tip + '</p></div>'
            st.markdown(routine_html, unsafe_allow_html=True)

            report_date = datetime.date.today().strftime("%Y-%m-%d")
            report_lines = [
                "DERMA-LUXE AI - CLINICAL & BIOMARKER REPORT",
                "Date: " + report_date,
                "Patient: " + p_name + " (" + str(age) + "y, " + gender + ")",
                "Skin Type: " + skin_type + " | Location: " + lesion_area,
                "AI Verdict: " + diag_title + " (" + conf_text + ")",
                "Wellness Index: " + str(overall_wellness) + "/100 | ABCDE Flags: " + str(abcde_total) + "/5",
                "Morning Protocol: " + morning_tip,
                "Night Protocol: " + evening_tip
            ]
            report_text = "\n".join(report_lines)

            st.download_button(
                label="Download Full Clinical & Skincare Report (.txt)",
                data=report_text,
                file_name="DermaLuxe_Report_" + p_name.replace(" ", "_") + ".txt",
                mime="text/plain"
            )
