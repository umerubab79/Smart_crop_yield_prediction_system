# ==========================================
# Imports
# ==========================================

import streamlit as st
import requests

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
        background: linear-gradient(135deg,#1565C0,#1976D2);
        padding:20px;
        border-radius:15px;
        text-align:center;
        color:white;
    ">
        <h1>🔐 User Login</h1>
        <p>Access Smart Crop Yield Prediction System</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ==========================================
# Session State
# ==========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ==========================================
# Login Form
# ==========================================

with st.form("login_form"):

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    submit = st.form_submit_button(
        "Login"
    )

# ==========================================
# Login Logic
# ==========================================

if submit:

    if not username:

        st.error(
            "Username is required"
        )

    elif not password:

        st.error(
            "Password is required"
        )

    else:

        payload = {
            "username": username,
            "password": password
        }

        try:

            response = requests.post(
                "http://127.0.0.1:8000/login",
                json=payload
            )

            if response.status_code == 200:

                data = response.json()

                st.session_state.logged_in = True

                st.session_state.username = data["username"]

                st.success(
                    "✅ Login Successful"
                )
                import time

                time.sleep(1)

                st.switch_page( "pages/04_Prediction.py")

                st.info(
                    f"Welcome {data['username']}"
                )

            else:

                st.error(
                    "Invalid Username or Password"
                )

        except Exception as e:

            st.error(
                f"Server Error: {e}"
            )

# ==========================================
# Logged In User
# ==========================================

if st.session_state.logged_in:

    st.markdown("---")

    st.success(
        f"👤 Logged in as: {st.session_state.username}"
    )

    if st.button("Logout"):

        st.session_state.logged_in = False

        st.session_state.username = ""

        st.rerun()

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