import streamlit as st

def apply_style():

    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(
            135deg,
            #F8FAFC,
            #EEF2F7,
            #E2E8F0
        );
    }

    .main-title {
        text-align: center;
        font-size: 5rem;
        font-weight: 900;
        color: #1E293B;
    }

    .subtitle {
        text-align: center;
        font-size: 1.5rem;
        color: #475569;
    }

    h1, h2, h3 {
        color: #1E293B !important;
    }

    .stButton > button {
        background-color: #334155;
        color: white;
        border-radius: 10px;
        border: none;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #1E293B;
        color: white;
    }

    .stTextInput input,
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True)