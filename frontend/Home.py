# ==========================================
# Imports
# ==========================================

import streamlit as st

# ==========================================
# Page Config
# ==========================================

st.set_page_config(
    page_title="Smart Crop Yield Prediction System",
    page_icon="🌾",
    layout="wide"
)

# ==========================================
# Custom CSS
# ==========================================

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(
        135deg,
        #E8F5E9,
        #C8E6C9,
        #A5D6A7
    );
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 5rem;
    font-weight: 900;
    color: #1B5E20;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 1.5rem;
    color: #2E7D32;
    margin-bottom: 30px;
}

/* Feature Box */
.feature-box {
    background-color: rgba(255,255,255,0.7);
    padding: 15px;
    border-radius: 15px;
    margin-top: 10px;
}

/* Footer */
.footer {
    text-align: center;
    color: #1B5E20;
    font-size: 16px;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# Header
# ==========================================

st.markdown(
    '<p class="main-title">🌾 Smart Crop Yield Prediction System</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Machine Learning Based Crop Yield Prediction Platform</p>',
    unsafe_allow_html=True
)

# ==========================================
# Statistics
# ==========================================

st.subheader("📊 Dataset Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="🌍 Countries",
        value="101"
    )

with col2:
    st.metric(
        label="🌾 Crop Types",
        value="10"
    )

with col3:
    st.metric(
        label="📁 Records",
        value="28,242"
    )

# ==========================================
# Features
# ==========================================

st.subheader("🚀 Project Features")

st.success("Crop Yield Prediction using Machine Learning")
st.success("FastAPI Backend Integration")
st.success("Prediction History Management")
st.success("SQLite Database Storage")
st.success("PDF Report Generation")
st.success("Interactive Streamlit Dashboard")

# ==========================================
# Model Information
# ==========================================

st.subheader("🤖 Machine Learning Model")

st.info("""
Model Used: Random Forest Regressor

Input Features:
• Country
• Crop
• Year
• Rainfall
• Pesticides
• Temperature

Output:
• Predicted Crop Yield
""")

# ==========================================
# How To Use
# ==========================================

st.subheader("📖 How To Use")

st.write("1️⃣ Open Prediction Page")
st.write("2️⃣ Enter Crop Information")
st.write("3️⃣ Click Predict Button")
st.write("4️⃣ View Predicted Yield")
st.write("5️⃣ Check Prediction History")

# ==========================================
# Footer
# ==========================================

st.markdown("---")

st.markdown(
    '<p class="footer">🌱 Developed with FastAPI + Streamlit + Random Forest Machine Learning Model</p>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "🔐 Login",
        use_container_width=True
    ):
        st.switch_page(
            "pages/02_Login.py"
        )

with col2:

    if st.button(
        "📝 Register",
        use_container_width=True
    ):
        st.switch_page(
            "pages/03_Register.py"
        )