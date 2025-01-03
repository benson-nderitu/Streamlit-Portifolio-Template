import streamlit as st
from streamlit_float import *
from streamlit_option_menu import option_menu

from components.footer import Footer
from Data.database import create_database
from HomePages.about import resume_about
from HomePages.contact import contact
from HomePages.portifolio_cards import portifolio_projects


st.write("Hello World")

# @st.fragment()
# def main():
#     create_database()  # Create databases if it does not exist

#     # ==================================================
#     #   NAVIGATION - NAVBAR from Streamlit Option Menu
#     # ==================================================
#     float_init()
#     NavBar_Container = st.container(key="TopMenuContainer")
#     with NavBar_Container:
#         locol, navcol, _ = st.columns([1, 3, 1], vertical_alignment="center")
#         with locol:
#             with st.container(key="LOGOContainer"):

#                 # 1. DYNAMIC COLORS
#                 # st.markdown(
#                 #     f'<h3 style="color:{primaryColor};">My <span style="color:orange;">Logo</span></h3>',
#                 #     unsafe_allow_html=True,
#                 # )

#                 # 2.FIXED COLORS
#                 # st.subheader(":green[MY] :rainbow[LOGO]")

#                 # 3.LOGO IMAG
#                 # st.image("static/logo1.png")
#                 st.image("static/logo.png")

#         with navcol:
#             with st.container(key="MenuContainer"):
#                 menu_selection = option_menu(
#                     None,
#                     ["About Me", "My Portfolio", "Contact"],
#                     icons=["person-circle", "laptop", "telephone"],
#                     menu_icon="cast",
#                     default_index=0,
#                     orientation="horizontal",
#                     manual_select=st.session_state.get("menusel", 0),
#                     styles={
#                         "container": {
#                             "background-color": "transparent",
#                             "padding": "0.2rem 0 !important",
#                         },
#                         # "icon": {"color": "orange"},
#                         # "nav-link": {
#                         #     #     # "text-align": "left",
#                         #     # "--hover-color": "#eee",
#                         # },
#                         "nav-link-selected": {
#                             "font-weight": "bold",
#                             "font-size": "16px",
#                             "color": primaryColor,
#                             "background-color": "transparent",
#                         },
#                     },
#                 )
#     st.spinner()
#     # Handle menu selection
#     if menu_selection == "About Me":
#         resume_about()

#     elif menu_selection == "My Portfolio":
#         portifolio_projects()

#     elif menu_selection == "Contact":
#         contact()

#     NavBar_Container.float(
#         "top: 0.5rem; z-index: 999990;background: transparent; max-height:3.25rem; "
#     )

#     Footer()


# if __name__ == "__main__":
#     main()
