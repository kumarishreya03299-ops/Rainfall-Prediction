import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Rainfall Prediction",
    page_icon="🌧️",
    layout="centered"
)

# -----------------------------
# Custom Styling
# -----------------------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    color: #1f4e79;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555555;
    margin-bottom: 30px;
}

.section {
    font-size: 24px;
    font-weight: 600;
    color: #1f4e79;
    margin-top: 15px;
}

.result-box {
    padding: 20px;
    border-radius: 12px;
    background-color: white;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.08);
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.markdown(
    '<div class="title">🌧️ Rainfall Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Machine Learning based Rain Tomorrow Prediction</div>',
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# Load Model
# -----------------------------
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------
# Input Section
# -----------------------------
st.markdown(
    '<div class="section">🌦️ Enter Weather Details</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    temperature = st.number_input(
        "🌡️ Temperature (°C)",
        min_value=-50.0,
        max_value=60.0,
        value=30.0,
        step=0.1
    )

    humidity = st.number_input(
        "💧 Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=1.0
    )

    wind_speed = st.number_input(
        "💨 Wind Speed",
        min_value=0.0,
        max_value=200.0,
        value=10.0,
        step=0.1
    )


with col2:

    precipitation = st.number_input(
        "🌧️ Precipitation (mm)",
        min_value=0.0,
        max_value=1000.0,
        value=5.0,
        step=0.1
    )

    cloud_cover = st.number_input(
        "☁️ Cloud Cover (%)",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=1.0
    )

    pressure = st.number_input(
        "🌀 Pressure (hPa)",
        min_value=800.0,
        max_value=1100.0,
        value=1010.0,
        step=0.1
    )

st.write("")

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔮 Predict Rain", use_container_width=True):

    input_data = pd.DataFrame([{
        "Temperature": temperature,
        "Humidity": humidity,
        "Wind Speed": wind_speed,
        "Precipitation": precipitation,
        "Cloud Cover": cloud_cover,
        "Pressure": pressure
    }])

    prediction = model.predict(input_data)

    probability = model.predict_proba(input_data)[0][1] * 100

    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    if prediction[0] == 1:
        st.success("🌧️ Rain is expected tomorrow.")
    else:
        st.info("☀️ No rain is expected tomorrow.")

    st.write(f"🌧️ **Rain Probability: {probability:.2f}%**")

    st.progress(int(probability))

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "💡 This prediction is generated using a Machine Learning classification model."
)