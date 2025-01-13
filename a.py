# import streamlit as st
# from streamlit_elements import dashboard, editor, elements, lazy, media, mui, nivo, sync

# st.set_page_config(layout="wide")

# markdownContent = """
# # Project Four
# **Graphics** | **Illustration** | **Creative**

# ### Description
# A creative journey into graphic design and illustration:
# - Vector art
# - Photo editing
# - Storyboarding

# #### Published On
# October 5, 2023

# #### Last Updated
# October 10, 2023
#             """
# layout = [
#     dashboard.Item("editor", 0, 0, 12, 4),
# ]

# with elements("demo"):
#     with dashboard.Grid(layout, draggableHandle=".draggable"):
#         with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):
#             mui.CardHeader(title="Editor", className="draggable")
#             with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
#                 editor.Monaco(
#                     defaultValue=markdownContent,
#                     language="markdown",
#                     onChange=lazy(sync("data")),
#                 )

#             with mui.CardActions:
#                 mui.Button("Apply changes", onClick=sync())


# ==============================================================================
# import streamlit as st
# from streamlit_float import float_css_helper,

# # Initialize the float feature
# float_init()

# # Create a container for the button
# button_container = st.container()

# # Define custom CSS for positioning
# custom_css = float_css_helper(
#     bottom="5% ",
#     width="50px ",
#     height="50px",
#     right="2%",
#     background="transparent",
#     border_radius="50% ",
#     cursor="pointer",
# )

# # Apply the floating effect with custom CSS
# button_container.float(custom_css)

# from streamlit_scroll_to_top import scroll_to_here

# # Step 1: Initialize scroll state in session_state
# if "scroll_to_top" not in st.session_state:
#     st.session_state.scroll_to_top = False

# if "scroll_to_header" not in st.session_state:
#     st.session_state.scroll_to_header = False

# # Step 2: Handle the scroll-to-top action
# if st.session_state.scroll_to_top:
#     scroll_to_here(0, key="top")  # Scroll to the top of the page
#     st.session_state.scroll_to_top = False  # Reset the state after scrolling


# # Step 3: Define a scroll function to trigger the state change
# def scroll():
#     st.session_state.scroll_to_top = True


# def scrollheader():
#     st.session_state.scroll_to_header = True


# # Step 4: Add some dummy content to simulate a long page
# st.title("Dummy Content")
# st.write("Scroll down to see the 'Scroll to Top' button.")
# for i in range(50):  # Generate dummy content
#     if i == 25:
#         if st.session_state.scroll_to_header:
#             scroll_to_here(0, key="header")  # Scroll to the top of the page
#             st.session_state.scroll_to_header = False  # Reset the state after scrolling
#         st.header("Or scroll here")
#     st.text(f"Line {i + 1}: This is some dummy content.")


from datetime import datetime
from pathlib import Path

# ------------------------------------------------------------------------------
import streamlit as st
from streamlit_comments import st_comments
from streamlit_donut import st_donut
from streamlit_float import *
from streamlit_option_menu import option_menu
from streamlit_scroll_navigation import scroll_navbar

from components.footer import Footer
from data.database import create_database
from homePages.about import resume_about
from homePages.contact import contact
from homePages.portfolio import portifolio_projects

# st_donut(
#     label="Site Completion",
#     value=progress1,
#     outOf=100,
#     units="%",
#     size=size,
#     value_text_color="purple",
#     text_size=text_size,
#     background_stroke_width=50,
#     # direction="anticlockwise",
#     rounded=True,
#     delta="-10%",
#     # label_visibility=False,
# )


# ------------------------------------------------------------------------------


nameextract = st.secrets["credentials"]["usernames"]
for username, details in nameextract.items():
    full_name = details["name"]
st.set_page_config(
    page_title=full_name,
    page_icon=":material/rocket_launch:",
    layout="wide",
    initial_sidebar_state="expanded",
)
# -------------------------
#    Get THEME COLORS
# -------------------------
backgroundColor = st.get_option("theme.backgroundColor")
secondaryBackgroundColor = st.get_option("theme.secondaryBackgroundColor")
primaryColor = st.get_option("theme.primaryColor")

navBgColor = backgroundColor
border_color = "#e0e0e0"
shadowColor = "#e0e0e0"


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
    f"""
    <style>
        header.stAppHeader {{
            # border-image: linear-gradient(to right, #3498db, #2ecc71, #e74c3c, #f1c40f, #34495e, #f39c12);
            # border-image-slice: 1;
            border-bottom: 1px solid {border_color};
            background-color: navBgColor;
            box-shadow: 4px 4px 10px {shadowColor};
        }}
        @media (max-width: 820px) {{
            header.stAppHeader {{
                height: 100px;
            }}}}
    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------
#     PATH SETTINGS &  LOAD CSS
# --------------------------------------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "style.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


@st.fragment()
def main():
    create_database()  # Create databases if it does not exist

    # ==================================================
    #   NAVIGATION - NAVBAR from Streamlit Option Menu
    # ==================================================
    float_init()
    NavBar_Container = st.container(key="TopMenuContainer")
    with NavBar_Container:
        locol, navcol, _ = st.columns([1, 3, 1], vertical_alignment="center")
        with locol:
            with st.container(key="LOGOContainer"):

                # 1. DYNAMIC COLORS
                # st.subheader(":primary[MY] :orange[LOGO]")

                # 2.FIXED COLORS
                # st.subheader(":green[MY] :rainbow[LOGO]")

                # 3.LOGO IMAG
                # st.image("static/logo1.png")
                st.image("static/logo.png")

        with navcol:
            with st.container(key="MenuContainer"):
                # Anchor IDs and icons
                anchor_ids = ["About", "Portfolio", "Contact"]
                anchor_icons = [
                    "info-circle",
                    "lightbulb",
                    "gear",
                ]

                scroll_navbar(
                    anchor_ids=anchor_ids,
                    # anchor_icons=anchor_icons,
                    key="navbar4",
                    orientation="horizontal",
                    override_styles={
                        "navigationBarBase": {
                            "backgroundColor": "red",
                            "margin": "0 !important",
                            "padding": "0 !important",
                            "max-height": "3rem",
                        },
                        "navigationBarHorizontal": {
                            "backgroundColor": "transparent",
                            "margin": "0 !important",
                            "padding": "0 !important",
                            "max-height": "3rem",
                        },
                        "navbarButtonBase": {
                            "backgroundColor": "transparent",
                            "color": "#000",
                            "font-weight": "bold",
                            "margin": "0% !important",
                            "max-height": "2rem !important",
                        },
                        "navbarButtonHover": {
                            "backgroundColor": primaryColor,
                        },
                        "navbarButtonActive": {
                            "backgroundColor": "red",
                        },
                    },
                )

    NavBar_Container.float("top: 0.5rem; z-index: 999990;max-height:3.2rem; ")

    # Dummy page setup
    for anchor_id in anchor_ids:
        if anchor_id == "About":
            st.subheader(anchor_id, anchor=anchor_id)
            st.write("about " * 100)
        if anchor_id == "Portfolio":
            st.subheader(anchor_id, anchor=anchor_id)
            st.write("Portfolio " * 100)
        if anchor_id == "Contact":
            st.subheader(anchor_id, anchor=anchor_id)
            st.write("Contact " * 100)

    Footer()


if __name__ == "__main__":
    main()
