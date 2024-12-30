import os
import time
from datetime import datetime

import streamlit as st
import streamlit_antd_components as sac

from Data.alldata import (
    get_experiences,
    get_profile,
    get_projects,
    get_services,
    get_skillDescription,
    get_skills,
    get_social_links,
    get_testimonials,
)
# from portifolio_cards import carousel_with_autoslide

primary_color = st.get_option("theme.primaryColor")


# ----------------------------------------------------------------
#       REUSABLE HEADER STYLE
# ----------------------------------------------------------------
def styled_title(normal_text, styled_text, styled_color="blue"):
    st.markdown(
        f"""
        <h1 style="font-size:2.5em; line-height: 0; ">{normal_text}</h1>
        <h1 style="font-size:2.5em; color: {styled_color}; line-height: 0; ">{styled_text}</h1>
        """,
        unsafe_allow_html=True,
    )


# Applying the  function
# styled_title("Welcome to", "Streamlit", "red")
# styled_title("Powered by", "Python", "purple")

# ----------------------------------------------------------------
#             Fetch current profile data
# ----------------------------------------------------------------
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


@st.fragment()
def resume_about():
    # --------------------------------------
    #          HERO SECTION
    # --------------------------------------
    @st.fragment
    def heroprofile():
        with st.container(key="heroContainer"):
            col1, col2 = st.columns(2, gap="small")
            with col1:
                with st.container(key="CTAContainer"):
                    st.title(name)
                    st.write(description)
                    st.markdown(f"""<hr style = "border: 1px solid transparent;">""",unsafe_allow_html=True)
                    ctacol, cta2col, cta3col = st.columns(3)
                    if ctacol.button(
                            label="Services",
                            icon=":material/support_agent:",
                            type="primary",
                            use_container_width=True,
                        ):
                            st.write("View WORK")

                    if cta2col.button(
                        label="Skills",
                        icon=":material/business_center:",
                        use_container_width=True,
                    ):
                        st.write("View SERVICES")
                    
                    if cta3col.button(
                            label="Work Experience", 
                            icon=":material/person_play:",
                            use_container_width=True,
                        ):
                            st.write("Contacting...")

            with col2:
                with st.container(key="profileImageContainer"):
                    st.image(profile_image, use_container_width=True)

    heroprofile()

    # ---------------------------------
    #     ABOUT ME SECTION
    # --------------------------------
    @st.fragment
    def AboutMe():
        with st.container(key="AboutMeContainer"):
            abttle, abtdesc, abtvideo = st.columns([1, 2, 2])
            with abttle:
                with st.container(key="AboutMeTitleContainer"):
                    styled_title("About", "ME", primary_color)

            with abtdesc:
                with st.container(key="AboutMeDescriptionContainer"):
                    st.markdown(f"**{introduction}**")
                    st.write(f"{about_me_description}")
                    st.markdown(f"**{about_me_closingTag}**")
                    viewcol, downloadcol = st.columns(2, gap="large")
                    with viewcol:
                        if st.button(
                            label="Read CV",
                            icon=":material/open_in_new:",
                            type="primary",
                            use_container_width=True,
                        ):
                            st.write("View CV")
                    with downloadcol:
                        if st.button(
                            label="Download CV",
                            icon=":material/download:",
                            key="download_resume",
                            use_container_width=True,
                        ):
                            st.write("Downloading...")
                        # st.download_button(
                        #     label=" 📄 Download CV",
                        #     data=PDFbyte,
                        #     file_name=resume_file.name,
                        #     mime="application/octet-stream",
                        # )

                    # --------------
                    #   SOCIAL LINKS
                    # ---------------
                    st.divider()

                    socialLinks = get_social_links()
                    socialLinks_dict = socialLinks.to_dict(orient="records")

                    buttons_list = [
                        sac.ButtonsItem(
                            label=id["label"],
                            icon=id["icon"],
                            color=id["color"],
                            href=id["href"],
                        )
                        for id in socialLinks_dict
                    ]

                    # Render the buttons
                    sac.buttons(
                        buttons_list,
                        index=None,
                        use_container_width=True,
                        align="center",
                        variant="filled",
                    )

            with abtvideo:
                with st.container(key="AboutMeVideoContainer"):
                    VIDEO_URL = "https://www.youtube.com/watch?v=7BUoSIVNW_U&t=0s"
                    st.video(VIDEO_URL)
                    # st.video("static/video.mp4")

    AboutMe()

    # ----------------------------------------------------------------
    #      MY SERVICES SECTION
    # ----------------------------------------------------------------
    @st.fragment
    def MyServices():
        with st.container(key="MyServicesContainer"):
            msrttl, servscol = st.columns([1, 4])
            with msrttl:
                styled_title("My", "SERVICES", primary_color)
            with servscol:

                def render_components(services):
                    with st.container(key="MyServiceslistContainer"):
                        col1, col2, col3 = st.columns(3)
                        # Loop through the list and render each item
                        for idx, service in enumerate(services):
                            title = service.get("title", "Untitled")
                            description = service.get(
                                "description", "No description available."
                            )
                            icon_name = service.get(  # icons from Bootstrap Icons
                                "icon", "house"
                            )  # Default icon is 'house'

                            # Assign columns to each
                            if idx % 3 == 0:
                                col = col1
                            elif idx % 3 == 1:
                                col = col2
                            else:
                                col = col3

                            # Render the title, description, and button with icon
                            with col:
                                with st.container(border=True):
                                    sac.buttons(
                                        [
                                            sac.ButtonsItem(
                                                icon=sac.BsIcon(
                                                    name=icon_name,
                                                    size=50,
                                                    color=primary_color,
                                                )
                                            )
                                        ],
                                        align="center",
                                        variant="text",
                                        index=None,
                                    )
                                    st.subheader(title)
                                    st.markdown(
                                        f"""
                                            <div style="text-align: center;">
                                                <p>{description}</p>
                                            </div>
                                            """,
                                        unsafe_allow_html=True,
                                    )

                # services list
                services_data = get_services()
                services_data = services_data.to_dict(orient="records")
                render_components(services_data)

    MyServices()

    # ----------------------------------------------------------------
    #           MY SKILLS SECTION
    # ----------------------------------------------------------------
    @st.fragment
    def MySkills():
        with st.container(key="SkillsContainer"):
            sklttl, skillscol = st.columns([1, 4])
            with sklttl:
                styled_title("My", "SKILLS", primary_color)
            with skillscol:
                with st.container(key="SkillsListContainer"):
                    descrcol, progcol = st.columns(2, gap="large")
                    with descrcol:
                        skillzdescrption = get_skillDescription()
                        (title, header, body, closingtag) = skillzdescrption
                        st.markdown(f"### {title}")
                        st.markdown(f"###### {header}")
                        st.markdown(f"{body}")
                        st.markdown(f"###### {closingtag}")
                    with progcol:

                        def render_skills(skills):
                            for skill in skills:
                                name = skill.get("name", "Unknown Skill")
                                percentage = skill.get("percentage", 0)

                                with st.container():
                                    # Render the skill name and percentage
                                    st.markdown(
                                        f"###### {name.upper()} - {percentage}%"
                                    )
                                    # Create a progress bar
                                    progressbar = st.progress(0)
                                    for percent_complete in range(percentage):
                                        # time.sleep(0.001)  # Adjust sleep time for speed
                                        progressbar.progress(percent_complete + 1)

                        skills = get_skills()
                        skills = skills.to_dict(orient="records")
                        render_skills(skills)

    MySkills()

    # ----------------------------------------------------------------
    #       MY EXPERIENCE SECTION
    # ----------------------------------------------------------------
    @st.fragment
    def MyStory():
        with st.container(key="ExperienceContainer"):
            expttl, expscol = st.columns([1, 4])
            with expttl:
                styled_title("My", "STORY", primary_color)
            with expscol:
                with st.container(key="ExperienceListContainer"):

                    def render_timeline(timeline_data):
                        for entry in timeline_data:
                            year = entry.get("year", "Unknown Year")
                            title = entry.get("title", "Untitled")
                            role = entry.get("role", "No Role")
                            description = entry.get(
                                "description", "No description available."
                            )

                            with st.container():
                                yrcol, expcol = st.columns([1, 5])
                                with yrcol:
                                    st.write(f"#### {year}")
                                with expcol:
                                    st.markdown(f"### {title}")
                                    st.markdown(f"**{role}**")
                                    st.write(description)

                    experience = get_experiences()
                    experience_entries = experience.to_dict(orient="records")
                    render_timeline(experience_entries)

    MyStory()

    # ----------------------------------------------------------------
    #    PORTFOLIO PREVIEW SECTION
    # ----------------------------------------------------------------

    # @st.fragment
    # def portfolio_section():
    #     with st.container(key="PortfolioContainer"):
    #         styled_title("My", "PORTFOLIO", primary_color)
    #         ttlcol, rdtbtncol = st.columns([3, 1])
    #         with rdtbtncol:
    #             if st.button(
    #                 label="View All",
    #                 key="portfolio_read_more",
    #                 type="primary",
    #                 icon=":material/open_in_new:",
    #                 use_container_width=True,
    #             ):
    #                 st.write("Redirecting to portfolio page...")

    #         def get_latest_projects(projects, n=3):
    #             # Sort the projects by publishDate in descending order and get the top n projects
    #             sorted_projects = sorted(
    #                 projects,
    #                 key=lambda x: datetime.strptime(x["publishDate"], "%Y-%m-%d"),
    #                 reverse=True,
    #             )
    #             return sorted_projects[:n]

    #         project_cards = get_projects()
    #         latest_projects = get_latest_projects(project_cards)

    #         cols = st.columns(3)
    #         for i, project in enumerate(latest_projects):
    #             with cols[i % 3]:
    #                 carousel_with_autoslide(project)

    # portfolio_section()

    # ----------------------------------------------------------------
    #      TESTIMONIAL SECTION
    # ----------------------------------------------------------------
    @st.fragment
    def Testimonials():
        with st.container(key="TestimonialContainer"):
            st.markdown(
                f"""
                            <h3 style="text-align:center; line-height: 5;">WHAT PEOPLE ARE SAYING</h3>
                            """,
                unsafe_allow_html=True,
            )

            def testimonials(reviews):
                if "review_index" not in st.session_state:
                    st.session_state.review_index = 0

                current_review = reviews[st.session_state.review_index]

                with st.container():
                    _, imgcol, desccol, _ = st.columns([1, 2, 2, 1])

                    with imgcol:
                        st.image(
                            current_review["image"],
                            width=200,
                            #  use_container_width=True)
                        )

                    # Review text and details
                    with desccol:
                        st.markdown(
                            f"""
                            ⭐ **{current_review['rating']}/5**

                            **"{current_review['text']}"**

                            — {current_review['author']}   — 
                            """
                        )

                    # Navigation buttons for switching reviews
                    _, leftcol, rightcol, _ = st.columns([2, 1, 1, 2], gap="medium")

                    with leftcol:
                        if st.button(
                            "",
                            key="prev_review",
                            help="View previous",
                            type="tertiary",
                            icon=":material/arrow_back_ios:",
                        ):
                            st.session_state.review_index = (
                                st.session_state.review_index - 1
                            ) % len(reviews)

                    with rightcol:
                        if st.button(
                            "",
                            key="next_review",
                            help="View next",
                            type="tertiary",
                            icon=":material/arrow_forward_ios:",
                        ):
                            st.session_state.review_index = (
                                st.session_state.review_index + 1
                            ) % len(reviews)

            testimonials_data = get_testimonials()
            testimonials_data = testimonials_data.to_dict(orient="records")
            testimonials(testimonials_data)

    Testimonials()

    # ----------------------------------------------------------------
    #        CLIENTS SECTION
    # ----------------------------------------------------------------
    @st.fragment
    def Clients():
        with st.container(key="ClientsContainer"):
            st.title("Clients")

    Clients()
