
# ==========================================
# Imports
# ==========================================

import streamlit as st
import pandas as pd
import requests

if not st.session_state.get("logged_in", False):
    st.warning("Please Login First")
    st.stop()

from utils.style import apply_style

# ==========================================
# Apply Theme
# ==========================================

apply_style()

# ==========================================
# Title
# ==========================================

st.markdown(
    """
    <h1 style='text-align:center; color:#1B5E20;'>
    📜 Prediction History
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ==========================================
# Fetch Data
# ==========================================

try:

    response = requests.get(
        "http://127.0.0.1:8000/history"
    )

    data = response.json()

    df = pd.DataFrame(data)

except Exception as e:

    st.error(f"Error: {e}")

    df = pd.DataFrame()

# ==========================================
# Display Data
# ==========================================

if not df.empty:

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "📈 Total Predictions",
            len(df)
        )

    with col2:
        st.metric(
            "🌾 Records Found",
            len(df)
        )

    st.markdown("---")

    # Search Box
    search = st.text_input(
        "🔍 Search Country or Crop"
    )

    if search:

        df = df[
            df.astype(str)
            .apply(
                lambda row:
                row.str.contains(
                    search,
                    case=False
                ).any(),
                axis=1
            )
        ]

    st.dataframe(
        df,
        use_container_width=True
    )

    # CSV Download
    csv = df.to_csv(
        index=False
    )

    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="prediction_history.csv",
        mime="text/csv"
    )
    if st.button("🚀 New Prediction"):

       st.switch_page(
        "pages/04_Prediction.py"
    )


else:

    st.warning(
        "No Prediction History Available"
    )

# ==========================================
# Footer
# ==========================================

st.markdown("---")

st.caption(
    "🌾 Smart Crop Yield Prediction System"
)