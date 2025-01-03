from datetime import datetime
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Admin Page",
    page_icon=":material/admin_panel_settings:",
    layout="wide",
)
# -------------------------
#    Get THEME COLORS
# -------------------------
backgroundColor = st.get_option("theme.backgroundColor")
secondaryBackgroundColor = st.get_option("theme.secondaryBackgroundColor")
primaryColor = st.get_option("theme.primaryColor")


# --------------------------------------------
#    CUSTOM CSS TO REMOVE Sidebar Icon
# --------------------------------------------

icon_svg = """
<style>
    .st-emotion-cache-qsoh6x {
        display: none;
        }
"""

st.markdown(f"<div style='color: inherit;'>{icon_svg}</div>", unsafe_allow_html=True)

# =================================================================
#     CUSTOM CSS TO REMOVE PADDING
# =================================================================
st.markdown(
    """
        <style>
            .st-emotion-cache-1jicfl2,
            .stMainBlockContainer.block-container {
                width: 100%;
                padding: 0rem 1rem 5rem;
                min-width: auto;
                max-width: initial;
                }
        </style>
            """,
    unsafe_allow_html=True,
)

# ----------------------------------------
#        NAVBAR BACKGROUND
# ----------------------------------------
st.markdown(
    """
    <style>
        header.stAppHeader {
            # border-bottom: 1px solid transparent;
            border-bottom: 0.5px solid #e0e0e0;
            # border-image: linear-gradient(to right, #3498db, #2ecc71, #e74c3c, #f1c40f, #34495e, #f39c12);
            # border-image-slice: 1;
        }
        @media (max-width: 820px) {
            header.stAppHeader {
                height: 100px;
            }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.page_link("streamlit_app.py", label="Home", icon=":material/home:")
    st.page_link(
        "pages/admin.py", label="Admin", icon=":material/admin_panel_settings:"
    )

# create_page = st.Page("home.py", title="Home", icon=":material/home:")
# delete_page = st.Page("admin.py", title="Admin", icon=":material/admin_panel_settings:")

# pg = st.navigation([create_page, delete_page])
# pg.run()
