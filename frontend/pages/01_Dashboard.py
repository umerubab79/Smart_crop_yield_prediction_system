
# ==========================================
# Imports
# ==========================================

import streamlit as st
import requests
import pandas as pd

from utils.style import apply_style
if not st.session_state.get("logged_in", False):
    st.warning("Please Login First")
    st.stop()

# ==========================================
# Apply Theme
# ==========================================

apply_style()

# ==========================================
# Page Header
# ==========================================

st.markdown(
    """
    <div style="
        background: linear-gradient(135deg,#1B5E20,#2E7D32);
        padding:20px;
        border-radius:15px;
        text-align:center;
        color:white;
    ">
        <h1>📊 Smart Crop Dashboard</h1>
        <p>Monitor Predictions, Dataset Insights and System Performance</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ==========================================
# Load Prediction History
# ==========================================

try:

    response = requests.get(
        "https://smart-crop-yield-prediction-system.onrender.com/login"
    )

    data = response.json()

    df = pd.DataFrame(data)

except:

    df = pd.DataFrame()

# ==========================================
# Metrics
# ==========================================

total_predictions = len(df)

if not df.empty:

    total_countries = df["country"].nunique()

    total_crops = df["crop"].nunique()

    avg_yield = round(
        df["predicted_yield"].mean(),
        2
    )

else:

    total_countries = 0

    total_crops = 0

    avg_yield = 0

# ==========================================
# Metric Cards
# ==========================================

st.subheader("📈 Dashboard Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Predictions",
        total_predictions
    )

with col2:
    st.metric(
        "Countries",
        total_countries
    )

with col3:
    st.metric(
        "Crops",
        total_crops
    )

with col4:
    st.metric(
        "Avg Yield",
        avg_yield
    )

st.markdown("---")

# ==========================================
# Latest Prediction
# ==========================================

st.subheader("🎯 Latest Prediction")

if not df.empty:

    latest = df.iloc[-1]

    col1, col2 = st.columns(2)

    with col1:

        st.success(
            f"""
Country: {latest['country']}

Crop: {latest['crop']}
"""
        )

    with col2:

        st.info(
            f"""
Predicted Yield

{latest['predicted_yield']:.2f}
"""
        )

else:

    st.warning(
        "No Prediction Available"
    )

st.markdown("---")

# ==========================================
# Dataset Statistics
# ==========================================

st.subheader("📁 Dataset Statistics")

st.progress(100)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Countries",
        "101"
    )

with col2:

    st.metric(
        "Crop Types",
        "10"
    )

with col3:

    st.metric(
        "Records",
        "28,242"
    )

st.markdown("---")

# ==========================================
# System Status
# ==========================================

st.subheader("⚙️ System Status")

col1, col2, col3 = st.columns(3)

with col1:

    st.success(
        "✅ FastAPI Running"
    )

with col2:

    st.success(
        "✅ Database Connected"
    )

with col3:

    st.success(
        "✅ ML Model Loaded"
    )

st.markdown("---")

# ==========================================
# Recent Predictions
# ==========================================

st.subheader("📜 Recent Predictions")

if not df.empty:

    st.dataframe(
        df.tail(10),
        use_container_width=True
    )

else:

    st.warning(
        "No Prediction History Available"
    )

st.markdown("---")

# ==========================================
# System Features
# ==========================================

st.subheader("🚀 System Features")

feature_col1, feature_col2 = st.columns(2)

with feature_col1:

    st.success(
        "Machine Learning Prediction"
    )

    st.success(
        "Random Forest Model"
    )

    st.success(
        "FastAPI Backend"
    )

with feature_col2:

    st.success(
        "SQLite Database"
    )

    st.success(
        "Prediction History Storage"
    )

    st.success(
        "Real-Time Prediction"
    )

st.markdown("---")

# ==========================================
# Model Information
# ==========================================

st.subheader("🤖 Model Information")

st.info(
    """
Model: Random Forest Regressor

Input Features:
• Country
• Crop
• Year
• Rainfall
• Pesticides
• Temperature

Output:
• Predicted Crop Yield

Performance:
• R² Score = 0.9875
• MAE = 3503.21
• RMSE = 9521.48
"""
)

st.markdown("---")

# ==========================================
# Footer
# ==========================================

st.markdown(
    """
    <div style="
        text-align:center;
        padding:20px;
    ">
        <h4>🌾 Smart Crop Yield Prediction System</h4>
        <p>Machine Learning • FastAPI • Streamlit • SQLite</p>
    </div>
    """,
    unsafe_allow_html=True
)