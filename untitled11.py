import numpy as np
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="Skin ML App", layout="centered")

st.title("🩺 Skin Health & Condition Predictor")
st.write("Enter patient/skin parameters below or upload a CSV dataset to train and test the model.")

# Sample dataset for quick testing if no CSV is uploaded
@st.cache_data
def load_sample_data():
    rng = np.random.default_rng(42)
    df = pd.DataFrame({
        "age": rng.integers(15, 75, 200),
        "hydration_score": rng.uniform(10.0, 95.0, 200).round(1),
        "uv_exposure_hours": rng.uniform(0.5, 10.0, 200).round(1),
        "oiliness_level": rng.uniform(1.0, 10.0, 200).round(1),
        "condition": rng.choice(["Normal", "Dry", "Oily", "Sensitive"], 200)
    })
    return df

uploaded_file = st.file_uploader("Upload CSV dataset (optional)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Custom dataset loaded successfully!")
else:
    df = load_sample_data()
    st.info("Using sample demo dataset. Upload your own CSV to train on real data.")

st.subheader("Dataset Preview")
st.dataframe(df.head())

numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
all_cols = df.columns.tolist()

if len(numeric_cols) >= 2 and len(all_cols) >= 2:
    target_col = st.selectbox(
        "Select Target Column",
        options=all_cols,
        index=len(all_cols) - 1
    )
    feature_cols = [c for c in numeric_cols if c != target_col]

    if len(feature_cols) > 0:
        X = df[feature_cols].dropna()
        y = df.loc[X.index, target_col]

        test_size = st.slider("Test Split Ratio", min_value=0.1, max_value=0.4, value=0.2, step=0.05)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )

        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        st.metric("Model Accuracy", f"{acc * 100:.2f}%")

        st.subheader("Make a Prediction")
        input_data = {}
        for col in feature_cols:
            col_min = float(X[col].min())
            col_max = float(X[col].max())
            col_mean = float(X[col].mean())
            input_data[col] = st.number_input(
                label=f"{col}",
                min_value=col_min,
                max_value=col_max,
                value=col_mean
            )

        if st.button("Predict"):
            input_df = pd.DataFrame([input_data])
            prediction = model.predict(input_df)[0]
            st.success(f"Predicted **{target_col}**: **{prediction}**")
    else:
        st.warning("Please make sure there is at least one numeric feature column.")
else:
    st.warning("Dataset needs at least two numeric columns and a target column.")
