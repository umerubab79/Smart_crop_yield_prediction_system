import streamlit as st
import pandas as pd

from utils.style import apply_style

# ==========================================
# Login Protection
# ==========================================

if not st.session_state.get("logged_in", False):

    st.warning("Please Login First")
    st.stop()

# ==========================================
# Apply Style
# ==========================================

apply_style()

# ==========================================
# Check Result
# ==========================================

if "prediction_result" not in st.session_state:

    st.warning(
        "No Prediction Available"
    )

    st.stop()

# ==========================================
# Data
# ==========================================

country = st.session_state["country"]
crop = st.session_state["crop"]
year = st.session_state["year"]

predicted_yield = st.session_state[
    "prediction_result"
]

# ==========================================
# Header
# ==========================================

st.markdown(
    """
    <h1 style='text-align:center;'>
        🌾 Prediction Result
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ==========================================
# Result Card
# ==========================================

st.metric(
    "Predicted Yield",
    f"{predicted_yield:,.2f} hg/ha"
)

st.info(
    f"""
🌍 Country: {country}

🌾 Crop: {crop}

📅 Year: {year}
"""
)

# ==========================================
# Download Result
# ==========================================

result_df = pd.DataFrame(
    {
        "Country": [country],
        "Crop": [crop],
        "Year": [year],
        "Predicted Yield": [predicted_yield]
    }
)

csv = result_df.to_csv(
    index=False
)

st.download_button(
    label="⬇ Download Result CSV",
    data=csv,
    file_name="crop_prediction.csv",
    mime="text/csv"
)

# ==========================================
# Navigation
# ==========================================

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "🔄 New Prediction"
    ):

        st.switch_page(
            "pages/02_Prediction.py"
        )

with col2:

    if st.button(
        "📜 View History"
    ):
        st.switch_page(
            "pages/06_History.py"
        )
        st.switch_page(
    "pages/04_Prediction.py")

   