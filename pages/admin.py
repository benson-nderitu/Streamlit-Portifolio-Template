import time
from pathlib import Path

import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth

from components.footer import Footer
from Data.alldata import (
    get_experiences,
    get_profile,
    get_services,
    get_skillDescription,
    get_skills,
    get_social_links,
    get_testimonials,
    update_experiences,
    update_profile,
    update_services,
    update_skillDescription,
    update_skills,
    update_social_link,
    update_testimonials,
)

st.set_page_config(
    page_title="Admin Page",
    page_icon=":material/admin_panel_settings:",
    layout="wide",
)

# --------------------------------------
#     SIDEBAR WIDTH
# --------------------------------------
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
# ----------------------------------------------
#     REMOVE PADDING - MAIN BLOCK
# ----------------------------------------------
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

# --------------------------------------
#     PATH SETTINGS &  LOAD CSS
# --------------------------------------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir.parent / "styles" / "style.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --------------------------------------
#     GET THEME COLOR
primary_color = st.get_option("theme.primaryColor")

# --------------------------------------
#     AUTHENTICATE
# --------------------------------------
authenticator = stauth.Authenticate(
    st.secrets["credentials"].to_dict(),
    st.secrets["cookie"]["name"],
    st.secrets["cookie"]["key"],
    st.secrets["cookie"]["expiry_days"],
)

_, logincol, _ = st.columns([1, 5, 1])
with logincol:
    info_container = st.empty()
    try:
        # --------------------------------------
        #     LOGIN PAGE
        # --------------------------------------
        authenticator.login(
            fields={
                "Form name": ":material/admin_panel_settings: &nbsp;Admin Page Login ",
                "Login": "Log Me In &nbsp;&nbsp;:material/login:",
                "Username": ":material/person: &nbsp;Admin Username",
                "Password": ":material/lock: &nbsp;Admin Password",
            },
            # single_session=True,
            # clear_on_submit=True,
        )
    except Exception as e:
        logincol.error(e)
if st.session_state["authentication_status"]:
    # ----------------------
    #     SIDEBAR
    # ----------------------
    with st.sidebar:
        st.page_link("streamlit_app.py", label="Home", icon=":material/home:")
        st.page_link(
            "pages/admin.py", label="Admin", icon=":material/admin_panel_settings:"
        )
        st.divider()
        st.markdown(
            f'### Welcome Back <br><span style="color: {primary_color}; line-height: 2;"><strong>{st.session_state["name"]}</strong></span>',
            unsafe_allow_html=True,
        )

        with st.container(key="NewPortfolioContainer"):
            if st.button(
                "New Project",
                key="AddNewPortfolio",
                icon=":material/add:",
                type="primary",
                use_container_width=True,
            ):
                st.write("Adding New Project ...")

            st.markdown(
                f"""<div style= "padding:5px"></div>""",
                unsafe_allow_html=True,
            )

            if st.button(
                "Edit Project",
                key="EditProject",
                icon=":material/edit:",
                type="primary",
                use_container_width=True,
            ):
                st.write("Adding New Project ...")

        st.divider()
        authenticator.logout(
            button_name="Log Out &nbsp;&nbsp;:material/directions_run:"
        )

    # ================================================================
    #        MAIN ADMIN PAGE
    # ================================================================
    # st.subheader("Settings")

    # ----------------------------------------------------------------
    #    PROFILE CONFIG
    # ----------------------------------------------------------------
    @st.fragment()
    def profile():
        with st.expander("PROFILE", icon=":material/account_circle:"):
            # Fetch current profile data
            profile = get_profile()
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
                new_name = st.text_input("Catchy Title", value=name)
                new_description = st.text_area("Catchy Description", value=description)
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
                    "Apply Changes",
                    icon=":material/update:",
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
                    st.cache_data.clear()
                    st.rerun()

    # ----------------------------------------------------------------
    #     SERVICES CONFIG
    # ----------------------------------------------------------------
    @st.fragment()
    def services():
        with st.expander("SERVICES", icon=":material/engineering:"):
            st.markdown(
                ":red[STRICTLY] use [Bootstrap Icons](https://icons.getbootstrap.com)"
            )
            services_df = get_services()
            st.data_editor(
                services_df,
                use_container_width=True,
                num_rows="dynamic",
                hide_index=True,
                key="my_key",
            )

            if st.button(
                label="Apply Changes",
                icon=":material/update:",
                type="primary",
                help="Apply changes and save them to the database",
                key="services_savebutton_key",
            ):
                if "my_key" in st.session_state:
                    changes = st.session_state["my_key"]
                    updated_services_df = services_df.copy()

                    # Apply edits
                    if changes["edited_rows"]:
                        for index, row in changes["edited_rows"].items():
                            for column, value in row.items():
                                if pd.notnull(
                                    value
                                ):  # Update only if the new value is not null
                                    updated_services_df.loc[int(index), column] = value
                    # Apply additions
                    if changes["added_rows"]:
                        new_rows_df = pd.DataFrame(changes["added_rows"])
                        updated_services_df = pd.concat(
                            [updated_services_df, new_rows_df], ignore_index=True
                        )

                    # Apply deletions
                    if changes["deleted_rows"]:
                        deleted_ids = changes["deleted_rows"]
                        updated_services_df = updated_services_df.drop(
                            index=deleted_ids
                        ).reset_index(drop=True)

                    # st.write(updated_services_df)

                # Update the database
                with st.spinner("Applying changes..."):
                    update_services(updated_services_df)
                    st.toast("Changes have been saved to the database.", icon="✅")
                    time.sleep(1)
                    st.cache_data.clear()
                    st.rerun()

    # ----------------------------------------------------------------
    #    SKILL DESCRIPTION CONFIG
    # ----------------------------------------------------------------
    @st.fragment()
    def skills_description():
        with st.expander("SKILL DESCRIPTION", icon=":material/description:"):
            SkillDescription = get_skillDescription()
            (title, header, body, closingtag) = SkillDescription
            with st.form("Skills Section: Description", border=False):
                new_title = st.text_input("Title", value=title)
                new_header = st.text_area("Header", value=header)
                new_body = st.text_area("Body", value=body)
                new_closingtag = st.text_area("Remarks", value=closingtag)
                submitted = st.form_submit_button(
                    "Apply Changes",
                    icon=":material/update:",
                    type="primary",
                )

                if submitted:
                    update_skillDescription(
                        new_title, new_header, new_body, new_closingtag
                    )
                    with st.spinner("Updating..."):
                        time.sleep(1)
                    st.toast("Skills Section updated successfully!", icon="✅")
                    time.sleep(1.5)
                    st.cache_data.clear()
                    st.rerun()

    # ----------------------------------------------------------------
    #    SKILLS CONFIG
    # ----------------------------------------------------------------
    @st.fragment()
    def skills():
        with st.expander("SKILLS", icon=":material/school:"):
            skill_df = get_skills()
            st.data_editor(
                skill_df,
                use_container_width=True,
                num_rows="dynamic",
                hide_index=True,
                key="skills_key",
            )

            if st.button(
                label="Apply Changes",
                icon=":material/update:",
                type="primary",
                help="Apply changes and save them to the database",
                key="skills_savebutton_key",
            ):
                if "skills_key" in st.session_state:
                    skill_df_changes = st.session_state["skills_key"]
                    updated_skills_df = skill_df.copy()

                    # Apply edits
                    if skill_df_changes["edited_rows"]:
                        for index, row in skill_df_changes["edited_rows"].items():
                            for column, value in row.items():
                                if pd.notnull(
                                    value
                                ):  # Update only if the new value is not null
                                    updated_skills_df.loc[int(index), column] = value
                    # Apply additions
                    if skill_df_changes["added_rows"]:
                        new_rows_df = pd.DataFrame(skill_df_changes["added_rows"])
                        updated_skills_df = pd.concat(
                            [updated_skills_df, new_rows_df], ignore_index=True
                        )

                    # Apply deletions
                    if skill_df_changes["deleted_rows"]:
                        deleted_ids = skill_df_changes["deleted_rows"]
                        updated_skills_df = updated_skills_df.drop(
                            index=deleted_ids
                        ).reset_index(drop=True)

                    # st.write(updated_skills_df)

                # Update the database
                with st.spinner("Applying changes..."):
                    update_skills(updated_skills_df)
                    st.toast("Changes have been saved to the database.", icon="✅")
                    time.sleep(1)
                    st.cache_data.clear()
                    st.rerun()

    # ----------------------------------------------------------------
    #       EXPERIENCE CONFIG
    # ----------------------------------------------------------------
    @st.fragment()
    def story():
        with st.expander("EXPERIENCE", icon=":material/person_play:"):
            experiences_df = get_experiences()
            st.data_editor(
                experiences_df,
                use_container_width=True,
                num_rows="dynamic",
                hide_index=True,
                key="experiences_key",
            )

            if st.button(
                label="Apply Changes",
                icon=":material/update:",
                type="primary",
                help="Apply changes and save them to the database",
                key="experiences_savebutton_key",
            ):
                if "experiences_key" in st.session_state:
                    experiences_df_changes = st.session_state["experiences_key"]
                    updated_experiences_df = experiences_df.copy()

                    # Apply edits
                    if experiences_df_changes["edited_rows"]:
                        for index, row in experiences_df_changes["edited_rows"].items():
                            for column, value in row.items():
                                if pd.notnull(
                                    value
                                ):  # Update only if the new value is not null
                                    updated_experiences_df.loc[int(index), column] = (
                                        value
                                    )
                    # Apply additions
                    if experiences_df_changes["added_rows"]:
                        new_rows_df = pd.DataFrame(experiences_df_changes["added_rows"])
                        updated_experiences_df = pd.concat(
                            [updated_experiences_df, new_rows_df], ignore_index=True
                        )

                    # Apply deletions
                    if experiences_df_changes["deleted_rows"]:
                        deleted_ids = experiences_df_changes["deleted_rows"]
                        updated_experiences_df = updated_experiences_df.drop(
                            index=deleted_ids
                        ).reset_index(drop=True)

                    # st.write(updated_experiences_df)

                # Update the database
                with st.spinner("Applying changes..."):
                    update_experiences(updated_experiences_df)
                    st.toast("Changes have been saved to the database.", icon="✅")
                    time.sleep(1)
                    st.cache_data.clear()
                    st.rerun()

    # ----------------------------------------------------------------
    #       TESTIMONIALS CONFIG
    # ----------------------------------------------------------------
    @st.fragment()
    def testimonials():
        with st.expander("TESTIMONIALS", icon=":material/sentiment_satisfied:"):
            testimonials_df = get_testimonials()
            st.data_editor(
                testimonials_df,
                use_container_width=True,
                num_rows="dynamic",
                hide_index=True,
                key="testimonials_key",
            )

            if st.button(
                label="Apply Changes",
                icon=":material/update:",
                type="primary",
                help="Apply changes and save them to the database",
                key="testimonials_savebutton_key",
            ):
                if "testimonials_key" in st.session_state:
                    testimonials_df_changes = st.session_state["testimonials_key"]
                    updated_testimonials_df = testimonials_df.copy()

                    # Apply edits
                    if testimonials_df_changes["edited_rows"]:
                        for index, row in testimonials_df_changes[
                            "edited_rows"
                        ].items():
                            for column, value in row.items():
                                if pd.notnull(
                                    value
                                ):  # Update only if the new value is not null
                                    updated_testimonials_df.loc[int(index), column] = (
                                        value
                                    )
                    # Apply additions
                    if testimonials_df_changes["added_rows"]:
                        new_rows_df = pd.DataFrame(
                            testimonials_df_changes["added_rows"]
                        )
                        updated_testimonials_df = pd.concat(
                            [updated_testimonials_df, new_rows_df], ignore_index=True
                        )

                    # Apply deletions
                    if testimonials_df_changes["deleted_rows"]:
                        deleted_ids = testimonials_df_changes["deleted_rows"]
                        updated_testimonials_df = updated_testimonials_df.drop(
                            index=deleted_ids
                        ).reset_index(drop=True)

                    # st.write(updated_testimonials_df)

                # Update the database
                with st.spinner("Applying changes..."):
                    update_testimonials(updated_testimonials_df)
                    st.toast("Changes have been saved to the database.", icon="✅")
                    time.sleep(1)
                    st.cache_data.clear()
                    st.rerun()

    # ----------------------------------------------------------------
    #       SOCIAL LINKS CONFIG
    # ----------------------------------------------------------------
    @st.fragment()
    def social_links():
        with st.expander("SOCIAL LINKS", icon=":material/public:"):
            st.markdown(
                ":red[STRICTLY] use [Bootstrap Icons](https://icons.getbootstrap.com)"
            )
            socialLinks_df = get_social_links()
            st.data_editor(
                socialLinks_df,
                use_container_width=True,
                num_rows="dynamic",
                hide_index=True,
                key="socialLinks_key",
            )

            if st.button(
                label="Apply Changes",
                icon=":material/update:",
                type="primary",
                help="Apply changes and save them to the database",
                key="socialLinks_savebutton_key",
            ):
                if "socialLinks_key" in st.session_state:
                    socialLinks_df_changes = st.session_state["socialLinks_key"]
                    updated_socialLinks_df = socialLinks_df.copy()

                    # Apply edits
                    if socialLinks_df_changes["edited_rows"]:
                        for index, row in socialLinks_df_changes["edited_rows"].items():
                            for column, value in row.items():
                                if pd.notnull(
                                    value
                                ):  # Update only if the new value is not null
                                    updated_socialLinks_df.loc[int(index), column] = (
                                        value
                                    )
                    # Apply additions
                    if socialLinks_df_changes["added_rows"]:
                        new_rows_df = pd.DataFrame(socialLinks_df_changes["added_rows"])
                        updated_socialLinks_df = pd.concat(
                            [updated_socialLinks_df, new_rows_df], ignore_index=True
                        )

                    # Apply deletions
                    if socialLinks_df_changes["deleted_rows"]:
                        deleted_ids = socialLinks_df_changes["deleted_rows"]
                        updated_socialLinks_df = updated_socialLinks_df.drop(
                            index=deleted_ids
                        ).reset_index(drop=True)

                    # st.write(updated_socialLinks_df)

                # Update the database
                with st.spinner("Applying changes..."):
                    update_social_link(updated_socialLinks_df)
                    st.toast("Changes have been saved to the database.", icon="✅")
                    time.sleep(1)
                    st.cache_data.clear()
                    st.rerun()

    # Render the ADMIN Sections============================
    profile()
    services()
    skills_description()
    skills()
    story()
    testimonials()
    social_links()
    Footer()

elif st.session_state["authentication_status"] is False:
    logincol.error("Username/password is incorrect")
elif st.session_state["authentication_status"] is None:
    info_container.success(
        "Please enter Your Username and Password to access the Admin Page",
        icon=":material/info:",
    )
    Footer()
