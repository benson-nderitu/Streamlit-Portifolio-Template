import streamlit as st
import streamlit_authenticator as stauth

set_page_config = st.set_page_config(
    page_title="Admin Page",
    page_icon=":material/admin_panel_settings:",
    layout="wide",
    initial_sidebar_state="auto",
)


@st.fragment()
def adminpage():
    authenticator = stauth.Authenticate(
        st.secrets["credentials"].to_dict(),
        st.secrets["cookie"]["name"],
        st.secrets["cookie"]["key"],
        st.secrets["cookie"]["expiry_days"],
    )
    try:
        authenticator.login()
    except Exception as e:
        st.error(e)
    if st.session_state["authentication_status"]:
        authenticator.logout()
        st.title("Welcome to the admin page")
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.title("Some content")

    elif st.session_state["authentication_status"] is False:
        st.error("Username/password is incorrect")
    elif st.session_state["authentication_status"] is None:
        st.warning("Please enter your username and password")


if __name__ == "__main__":
    adminpage()
