import streamlit as st

def apply_style():

    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(
            135deg,
            #E8F5E9,
            #C8E6C9,
            #A5D6A7
        );
    }

    .main-title {
        text-align: center;
        font-size: 5rem;
        font-weight: 900;
        color: #1B5E20;
    }

    .subtitle {
        text-align: center;
        font-size: 1.5rem;
        color: #2E7D32;
    }

    </style>
    """,
    unsafe_allow_html=True)