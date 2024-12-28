from datetime import datetime
from pathlib import Path

import streamlit as st
import streamlit_antd_components as sac
from streamlit_float import *
from streamlit_option_menu import option_menu

from about import resume_about
from contact import contact
from data.alldata import get_social_links
from data.database import create_database
from portifolio_cards import portifolio_projects

st.set_page_config(
    page_title="Benson Nderitu",
    page_icon=":material/bar_chart:",
    layout="wide",
    initial_sidebar_state="collapsed",
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
            border-bottom: 1px solid transparent;
            border-image: linear-gradient(to right, #3498db, #2ecc71, #e74c3c, #f1c40f, #34495e, #f39c12);
            border-image-slice: 1;
        }
        @media (max-width: 820px) {
            header.stAppHeader {
                height: 100px;
            }
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
    create_database()  # Create databases
    # ==================================================
    #   NAVIGATION 1: NAVBAR from Streamlit Option Menu
    # ==================================================
    float_init()
    menu_container = st.container(key="TopMenuContainer")
    with menu_container:
        locol, navcol, _ = st.columns([1, 3, 1], vertical_alignment="center")
        with locol:
            with st.container(key="LOGOContainer"):

                # 1. DYNAMIC COLORS
                # st.markdown(
                #     f'<h3 style="color:{primaryColor};">My <span style="color:orange;">Logo</span></h3>',
                #     unsafe_allow_html=True,
                # )

                # 2.FIXED COLORS
                # st.subheader(":green[MY] :rainbow[LOGO]")

                # 3.LOGO IMAG
                # st.image("static/logo1.png")
                st.image("static/logo.png")

        with navcol:
            with st.container(key="MenuContainer"):
                menu_selection = option_menu(
                    None,
                    ["About Me", "My Portfolio", "Contact"],
                    icons=["person-circle", "laptop", "telephone"],
                    menu_icon="cast",
                    default_index=0,
                    orientation="horizontal",
                    manual_select=st.session_state.get("menusel", 0),
                    styles={
                        "container": {
                            "background-color": "transparent",
                            "padding": "0.2rem 0 !important",
                        },
                        # "icon": {"color": "orange"},
                        # "nav-link": {
                        #     #     # "text-align": "left",
                        #     # "--hover-color": "#eee",
                        # },
                        "nav-link-selected": {
                            "font-weight": "bold",
                            "font-size": "16px",
                            "color": primaryColor,
                            "background-color": "transparent",
                        },
                    },
                )
    st.spinner()
    # Handle menu selection
    if menu_selection == "About Me":
        resume_about()

    elif menu_selection == "My Portfolio":
        portifolio_projects()

    elif menu_selection == "Contact":
        contact()

    menu_container.float(
        "top: 0.5rem; z-index: 999990;background: transparent; max-height:3.25rem; "
    )

    # ----------------------------------------------------------------
    #    FOOTER
    # ----------------------------------------------------------------
    @st.fragment
    def Footer():
        with st.container(key="FooterContainer"):
            _, centrecol, _ = st.columns(
                [
                    1,
                    2,
                    1,
                ],
                gap="large",
            )
            with centrecol:
                with st.container(key="FooterTitle"):
                    nameextract = st.secrets["credentials"]["usernames"]
                    for username, details in nameextract.items():
                        full_name = details["name"]
                        st.markdown(
                            f"""
                            <h2 style="text-align:center;">{full_name}</h2>
                            """,
                            unsafe_allow_html=True,
                        )

                socialLinks = get_social_links()
                footer_socialLinks = socialLinks.to_dict(orient="records")
                buttons_list = [
                    sac.ButtonsItem(
                        icon=id["icon"],
                        # color=id["color"],
                        href=id["href"],
                    )
                    for id in footer_socialLinks
                ]
                sac.buttons(
                    buttons_list,
                    index=None,
                    use_container_width=False,
                    align="center",
                    variant="outline",
                )

                st.divider()
                now = datetime.now()
                current_year = now.year
                st.markdown(
                    f"""
                    <div style="text-align: center;">
                        <p>Copyright &copy; {current_year} - {full_name}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    Footer()


if __name__ == "__main__":
    main()
