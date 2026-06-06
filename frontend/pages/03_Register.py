# ==========================================
# Imports
# ==========================================

import streamlit as st
import requests
import time

from utils.style import apply_style

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
        <h1>📝 User Registration</h1>
        <p>Create your account to access Smart Crop Yield Prediction System</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ==========================================
# Registration Form
# ==========================================

with st.form("register_form"):

    full_name = st.text_input(
        "👤 Full Name"
    )

    username = st.text_input(
        "🆔 Username"
    )

    email = st.text_input(
        "📧 Email"
    )

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    confirm_password = st.text_input(
        "🔒 Confirm Password",
        type="password"
    )

    submit = st.form_submit_button(
        "✅ Register"
    )

# ==========================================
# Register Logic
# ==========================================

if submit:

    if not full_name:

        st.error("Full Name is required")

    elif not username:

        st.error("Username is required")

    elif not email:

        st.error("Email is required")

    elif not password:

        st.error("Password is required")

    elif password != confirm_password:

        st.error("Passwords do not match")

    else:

        payload = {
            "full_name": full_name,
            "username": username,
            "email": email,
            "password": password
        }

        try:
            response = requests.post(
                "https://smart-crop-yield-prediction-system-1.onrender.com/register",
                json=payload
            )

            st.write("Status Code:", response.status_code)
            st.write("Response:", response.text)

            if response.status_code == 200:

                st.success(
                    "✅ Registration Successful"
                )

                time.sleep(2)

                st.switch_page(
                    "pages/02_Login.py"
                )

            else:

                try:

                    data = response.json()

                    st.error(
                        data.get(
                            "detail",
                            "Registration Failed"
                        )
                    )

                except:

                    st.error(
                        f"Server Error: {response.text}"
                    )

        except Exception as e:

            st.error(
                f"Server Error: {e}"
            )

# ==========================================
# Footer
# ==========================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;">
        <h4>🌾 Smart Crop Yield Prediction System</h4>
    </div>
    """,
    unsafe_allow_html=True
)