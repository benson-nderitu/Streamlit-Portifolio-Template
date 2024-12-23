import sqlite3
import time
from pathlib import Path

import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth

from data.alldata import fetch_profile, get_services, update_profile, update_services
from data.database import create_database

set_page_config = st.set_page_config(
    page_title="Admin Page",
    page_icon=":material/admin_panel_settings:",
    layout="wide",
)

create_database()  # Create databases if it does not exist

st.markdown(
    """
       <style>
       [data-testid="stSidebar"][aria-expanded="true"]{
           min-width: 244px;
           max-width: 244px;
       }
       """,
    unsafe_allow_html=True,
)
# ---CUSTOM CSS TO REMOVE PADDING--------------
st.markdown(
    """
        <style>
            .st-emotion-cache-1jicfl2,
            .stMainBlockContainer.block-container {
                width: 100%;
                padding: 0rem 1rem 10rem;
                min-width: auto;
                max-width: initial;
                }
        </style>
            """,
    unsafe_allow_html=True,
)

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir.parent / "styles" / "style.css"

# --- LOAD CSS,   ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

primary_color = st.get_option("theme.primaryColor")

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
    with st.sidebar:
        st.markdown(
            f'### Welcome Back <br><span style="color: {primary_color};"><strong>{st.session_state["name"]}</strong></span>',
            unsafe_allow_html=True,
        )

        with st.container(key="NewPortfolioContainer"):
            if st.button(
                "Add New Portfolio",
                key="AddNewPortfolio",
                icon=":material/add:",
                type="primary",
                use_container_width=True,
            ):
                st.write("Add New Portfolio")

        st.divider()
        authenticator.logout()

    def profile():
        with st.expander("PROFILE", icon=":material/account_circle:"):
            # Fetch current profile data
            profile = fetch_profile()
            (
                name,
                description,
                profile_image,
                introduction,
                about_me_description,
                about_me_closingTag,
                about_me_video,
            ) = profile

            # Form to edit profile
            with st.form("edit_profile", border=False):
                new_name = st.text_input("Name", value=name)
                new_description = st.text_area("Description", value=description)
                new_profile_image = st.text_input(
                    "Profile Image Url", value=profile_image
                )
                new_introduction = st.text_area("Introduction", value=introduction)
                new_about_me_description = st.text_area(
                    "About Me Description", value=about_me_description
                )
                new_about_me_closingTag = st.text_input(
                    "About Me Closing Tag", value=about_me_closingTag
                )
                new_about_me_video = st.text_input(
                    "About Me Video Url", value=about_me_video
                )
                submitted = st.form_submit_button(
                    "Update Profile",
                    icon=":material/save:",
                    type="primary",
                )

                if submitted:
                    update_profile(
                        new_name,
                        new_description,
                        new_profile_image,
                        new_introduction,
                        new_about_me_description,
                        new_about_me_closingTag,
                        new_about_me_video,
                    )
                    with st.spinner("Updating..."):
                        time.sleep(1)
                    st.toast("Profile updated successfully!", icon="✅")
                    time.sleep(1.5)
                    st.cache_data.clear(fetch_profile)
                    st.rerun()

    def services():
        with st.expander("Services Section", icon=":material/palette:"):
            df = get_services()
            st.write("Edit the table below:")
            edited_data = st.data_editor(
                df,
                use_container_width=True,
                num_rows="dynamic",
                hide_index=True,
                key="my_key",
            )

            if st.button("Apply Changes"):
                if "my_key" in st.session_state:
                    changes = st.session_state["my_key"]
                    updated_df = df.copy()

                    # Apply edits
                    if changes["edited_rows"]:
                        for index, row in changes["edited_rows"].items():
                            for column, value in row.items():
                                if pd.notnull(
                                    value
                                ):  # Update only if the new value is not null
                                    updated_df.loc[int(index), column] = value
                    # Apply additions
                    if changes["added_rows"]:
                        new_rows_df = pd.DataFrame(changes["added_rows"])
                        updated_df = pd.concat(
                            [updated_df, new_rows_df], ignore_index=True
                        )

                    # Apply deletions
                    if changes["deleted_rows"]:
                        deleted_ids = changes["deleted_rows"]
                        updated_df = updated_df.drop(index=deleted_ids).reset_index(
                            drop=True
                        )

                    st.write(updated_df)

                # Update the database with the new data
                st.spinner()
                time.sleep(1)
                update_services(updated_df)
                st.success("Changes have been saved to the database.")
                st.cache_data.clear()
                st.rerun()

    # Render the ADMIN Sections============================
    profile()
    services()

elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")
