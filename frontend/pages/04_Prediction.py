
# ==========================================
# Imports
# ==========================================

import streamlit as st
import requests

from utils.style import apply_style
from utils.data import COUNTRIES, CROPS

# ==========================================
# Login Protection
# ==========================================

if not st.session_state.get("logged_in", False):

    st.warning(
        "🔐 Please Login First"
    )

    st.stop()

# ==========================================
# Apply Theme
# ==========================================

apply_style()

# ==========================================
# Page Header
# ==========================================

st.title("🌾 Crop Yield Prediction")
st.write("Enter crop information to predict yield")
st.markdown("---")

# ==========================================
# Input Section
# ==========================================

col1, col2 = st.columns(2)

with col1:

    area = st.selectbox(
        "🌍 Country",
        COUNTRIES
    )

    crop = st.selectbox(
        "🌾 Crop",
        CROPS
    )

    year = st.number_input(
        "📅 Year",
        min_value=1990,
        max_value=2035,
        value=2025
    )

with col2:

    rainfall = st.number_input(
        "🌧 Rainfall (mm/year)",
        min_value=0.0,
        value=1200.0
    )

    pesticides = st.number_input(
        "🧪 Pesticides (tonnes)",
        min_value=0.0,
        value=50.0
    )

    temperature = st.number_input(
        "🌡 Average Temperature (°C)",
        min_value=-50.0,
        max_value=60.0,
        value=25.0
    )

st.markdown("---")

# ==========================================
# Predict Button
# ==========================================

if st.button(
    "🚀 Predict Yield",
    use_container_width=True
):

    payload = {
        "Area": area,
        "Item": crop,
        "Year": int(year),
        "average_rain_fall_mm_per_year": rainfall,
        "pesticides_tonnes": pesticides,
        "avg_temp": temperature
    }

    try:
        response = requests.post(
            "https://smart-crop-yield-prediction-system.onrender.com/predict",
            json=payload)


        if response.status_code == 200:

            result = response.json()

            predicted_yield = result[
                "predicted_yield"
            ]

            # Save Data For Result Page

            st.session_state[
                "prediction_result"
            ] = predicted_yield

            st.session_state[
                "country"
            ] = area

            st.session_state[
                "crop"
            ] = crop

            st.session_state[
                "year"
            ] = year

            st.session_state[
                "rainfall"
            ] = rainfall

            st.session_state[
                "pesticides"
            ] = pesticides

            st.session_state[
                "temperature"
            ] = temperature

            # Redirect To Result Page

            st.switch_page(
                "pages/05_Result.py"
            )

        else:

            st.error(
                "Prediction API Error"
            )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )

