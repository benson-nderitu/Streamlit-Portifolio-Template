import os
import time
from datetime import datetime

import streamlit as st
import streamlit_antd_components as sac
import streamlit_shadcn_ui as ui
from streamlit_donut import st_donut

from components.horizontal import st_horizontal
from data.allData import (
    get_experiences,
    get_profile,
    get_projects,
    get_services,
    get_skillDescription,
    get_skills,
    get_social_links,
    get_testimonials,
)
from utils.cv import my_cv

primary_color = st.get_option("theme.primaryColor")


# Anchor IDs and icons
anchor_ids = ["About", "Portfolio", "Contact"]
anchor_icons = [
    "info-circle",
    "lightbulb",
    "gear",
]


# @st.fragment
# def example5():
#     from streamlit_scroll_navigation import ForceAnchor

#     force_settings = ForceAnchor()
#     if st.button("Go to Settings", icon=":material/settings:", type="primary"):
#         force_settings.push("Contact")


# example5()
# for anchor_id in anchor_ids:
#     if anchor_id == "About":
#         # st.subheader(anchor_id, anchor=anchor_id)
#         st.write("about " * 100)
#     if anchor_id == "Portfolio":
#         st.subheader(anchor_id, anchor=anchor_id)
#         st.write("Portfolio " * 100)
#     if anchor_id == "Contact":
#         st.subheader(anchor_id, anchor=anchor_id)
#         st.write("Contact " * 100)


# ----------------------------------------------------------------
#       REUSABLE HEADER STYLE
# ----------------------------------------------------------------
def styled_title(normal_text=None, styled_text=None, styled_color="blue"):
    normal_text = normal_text or ""
    styled_text = styled_text or ""
    st.markdown(
        f"""
        <h1 style="font-size:2.5em; line-height: 0; ">{normal_text}</h1>
        <h1 style="font-size:2.5em; color: {styled_color}; line-height: 0; ">{styled_text}</h1>
        """,
        unsafe_allow_html=True,
    )


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
    def heroProfile():
        with st.container(key="heroContainer"):
            col1, col2 = st.columns(2, gap="small")
            with col1:
                with st.container(key="CTAContainer"):
                    st.title(name)
                    st.write(description)
                    st.markdown(
                        f"""<hr style = "border: 1px solid transparent;">""",
                        unsafe_allow_html=True,
                    )
                    cta_col, cta_2_col, cta_3_col = st.columns(3)
                    if cta_col.button(
                        label="Services",
                        icon=":material/support_agent:",
                        type="primary",
                        use_container_width=True,
                    ):
                        st.write("View WORK")

                    if cta_2_col.button(
                        label="Skills",
                        icon=":material/business_center:",
                        use_container_width=True,
                    ):
                        st.write("View SERVICES")

                    if cta_3_col.button(
                        label="Work Experience",
                        icon=":material/person_play:",
                        use_container_width=True,
                    ):
                        st.write("Contacting...")

            with col2:
                with st.container(key="profileImageContainer"):
                    st.image(profile_image, use_container_width=True)

    heroProfile()

    # ---------------------------------
    #     ABOUT ME SECTION
    # --------------------------------
    @st.fragment
    def aboutMe():
        with st.container(key="AboutMeContainer"):
            abt_tle, abt_desc, abt_video = st.columns([1, 2, 2])
            with abt_tle:
                with st.container(key="AboutMeTitleContainer"):
                    styled_title(
                        normal_text="About",
                        styled_text="ME",
                        styled_color=primary_color,
                    )

            with abt_desc:
                with st.container(key="AboutMeDescriptionContainer"):
                    st.markdown(f"**{introduction}**")
                    st.write(f"{about_me_description}")
                    st.markdown(f"**{about_me_closingTag}**")
                    view_col, download_col = st.columns(2, gap="large")
                    with view_col:
                        if st.button(
                            label="Read CV",
                            icon=":material/open_in_new:",
                            type="primary",
                            use_container_width=True,
                        ):
                            my_cv()

                    with download_col:
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

            with abt_video:
                with st.container(key="AboutMeVideoContainer"):
                    VIDEO_URL = "https://www.youtube.com/watch?v=7BUoSIVNW_U&t=0s"
                    st.video(VIDEO_URL)
                    # st.video("static/video.mp4")

    aboutMe()

    # ----------------------------------------------------------------
    #      STATISTICS SECTION
    # ----------------------------------------------------------------
    @st.fragment
    def Statistics():
        _, metrics_col = st.columns([1, 8])
        with metrics_col.container(key="StatisticsContainer"):
            styled_title(
                normal_text=None,
                styled_text=None,
                styled_color=primary_color,
            )

            total_projects = get_projects().shape[0]

            size = 120
            bg_stroke = 5
            arc_stroke = 7
            rounded = True
            hide_bg = False
            direction = ("anticlockwise",)

            # from components.horizontal import st_horizontal
            # with st_horizontal()
            col1, col2, col3, col4 = st.columns(4)
            with col1:

                st_donut(
                    label=":material/laptop: Portfolio Projects",
                    value=total_projects,
                    outOf=8,
                    size=size,
                    text_size=45,
                    background_stroke_width=bg_stroke,
                    arc_stroke_width=arc_stroke,
                    direction=direction,
                    rounded=rounded,
                    hide_background=hide_bg,
                )
            with col2:
                st_donut(
                    label=":material/rocket_launch: Experience",
                    value=8,
                    outOf=10,
                    units=" yrs",
                    text_size=40,
                    background_stroke_width=bg_stroke,
                    arc_stroke_width=arc_stroke,
                    size=size,
                    direction=direction,
                    rounded=rounded,
                    hide_background=hide_bg,
                )
            with col3:
                rating = 4.8
                delta = f"{round((rating / 5) * 100)}%"
                st_donut(
                    label=":material/star: Rating",
                    value=rating,
                    outOf=5,
                    units="/5",
                    delta=delta,
                    delta_text_size=14,
                    text_size=40,
                    background_stroke_width=bg_stroke,
                    arc_stroke_width=arc_stroke,
                    size=size,
                    direction=direction,
                    rounded=rounded,
                    hide_background=hide_bg,
                )
            with col4:
                st_donut(
                    label=":material/check_circle: Metric 4",
                    value=24,
                    outOf=100,
                    units="%",
                    delta="5.6%",
                    delta_text_size=14,
                    text_size=40,
                    background_stroke_width=bg_stroke,
                    arc_stroke_width=arc_stroke,
                    size=size,
                    direction=direction,
                    rounded=rounded,
                    hide_background=hide_bg,
                )

    Statistics()

    # ----------------------------------------------------------------
    #      MY SERVICES SECTION
    # ----------------------------------------------------------------
    @st.fragment
    def myServices():
        with st.container(key="MyServicesContainer"):
            msr_ttl, service_col = st.columns([1, 4])
            with msr_ttl:
                styled_title(
                    normal_text="My", styled_text="SERVICES", styled_color=primary_color
                )
            with service_col:

                def my_services(services):
                    with st.container(key="MyServicesListContainer"):
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
                                                    size=75,
                                                    color=primary_color,
                                                )
                                            )
                                        ],
                                        align="center",
                                        variant="text",
                                        index=None,
                                    )
                                    st.markdown(
                                        f"""
                                    <h3 style="text-align: center;">
{title}</h3>""",
                                        unsafe_allow_html=True,
                                    )
                                    st.markdown(
                                        f"""
                                    <p style="text-align: center;">
{description}</p>""",
                                        unsafe_allow_html=True,
                                    )

                # services list
                services_data = get_services()
                services_data = services_data.to_dict(orient="records")
                my_services(services_data)

    myServices()

    # ----------------------------------------------------------------
    #           MY SKILLS SECTION
    # ----------------------------------------------------------------
    @st.fragment
    def mySkills():
        with st.container(key="SkillsContainer"):
            skl_ttl, skills_col = st.columns([1, 4])
            with skl_ttl:
                styled_title(
                    normal_text="My", styled_text="SKILLS", styled_color=primary_color
                )
            with skills_col:
                with st.container(key="SkillsListContainer"):
                    description_col, prog_col = st.columns(2, gap="large")
                    with description_col:
                        skills_description = get_skillDescription()
                        (title, header, body, closingtag) = skills_description
                        st.markdown(f"### {title}")
                        st.markdown(f"###### {header}")
                        st.markdown(f"{body}")
                        st.markdown(f"###### {closingtag}")
                    with prog_col:

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
                        
                        # TODO : SORT skills by % from l to s
                        skills.sort
                        st.write(skills)

                        render_skills(skills)

    mySkills()

    # ----------------------------------------------------------------
    #       MY EXPERIENCE SECTION
    # ----------------------------------------------------------------
    @st.fragment
    def MyStory():
        with st.container(key="ExperienceContainer"):
            expttl, expscol = st.columns([1, 4])
            with expttl:
                styled_title(
                    normal_text="My", styled_text="STORY", styled_color=primary_color
                )
            with expscol.container(key="ExperienceListContainer"):

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

    # MyStory()

    # ----------------------------------------------------------------
    #      TESTIMONIAL SECTION
    # ----------------------------------------------------------------
    @st.fragment()
    def Testimonials():
        with st.container(key="TestimonialContainer"):
            st.markdown(
                f"""
                            <h4 style="text-align:start; line-height: 5; margin-left:20px">WHAT PEOPLE ARE SAYING</h4>
                            """,
                unsafe_allow_html=True,
            )

            def testimonials(reviews):
                if "review_index" not in st.session_state:
                    st.session_state.review_index = 0

                current_review = reviews[st.session_state.review_index]

                (
                    img_col,
                    description_col,
                ) = st.columns([1, 3])

                with img_col:
                    st.image(
                        current_review["image"],
                        width=200,
                    )

                st.write("\n")
                # Review text and details
                with description_col:
                    st.markdown(
                        f"""
                        <p style = "text-align:center; font-weight:bold;">⭐ {current_review['rating']}/5</p>
                        <p style = "text-align:center; font-weight:bold;">"{current_review['text']}"<p/>
                        <p style = "padding:0.5rem;"></p>
                        <p style = "text-align:center;">— {current_review['author']}   —</p> 
                        """,
                        unsafe_allow_html=True,
                    )

                # Navigation buttons for switching reviews
                with st.container(key="TestimonialBtnContainer"):
                    with st_horizontal():
                        if st.button(
                            "",
                            key="prev_review",
                            help="Previous",
                            type="tertiary",
                            icon=":material/arrow_back_ios:",
                        ):
                            st.session_state.review_index = (
                                st.session_state.review_index - 1
                            ) % len(reviews)
                            st.rerun()

                        st.markdown(
                            f"<div style='text-align: center;'>{st.session_state.review_index + 1}/{len(reviews)}</div>",
                            unsafe_allow_html=True,
                        )

                        if st.button(
                            "",
                            key="next_review",
                            help="Next",
                            type="tertiary",
                            icon=":material/arrow_forward_ios:",
                        ):
                            st.session_state.review_index = (
                                st.session_state.review_index + 1
                            ) % len(reviews)
                            st.rerun()

            testimonials_data = get_testimonials().to_dict(orient="records")
            testimonials(testimonials_data)

    Testimonials()

    # ----------------------------------------------------------------
    #        CLIENTS SECTION
    # ----------------------------------------------------------------
    @st.fragment
    def Clients():
        with st.container(key="ClientsContainer"):
            # styled_title(styled_text="Clients", styled_color=primary_color)

            # SOURCE: https://codepen.io/kevinwitkowski/pen/MWbxNGe
            carousel_html = """
            <style>
            body {
                margin: 0;
                padding: 0;
                font-family: sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: transparent;
            }
            .slider {
                height: 100px;
                margin: auto;
                overflow: hidden;
                position: relative;
                width: 100%;
                background: transparent !important;
            }
            .slide-track {
                animation: scroll 40s linear infinite;
                display: flex;
                width: calc(250px * 14);

            }
            .slide {
                height: 100px;
                width: 250px;
            }
            .slide img {
                width: 100%;
                height: 100%;
                object-fit: cover;
            }
            @keyframes scroll {
                0% { transform: translateX(0); }
                100% { transform: translateX(calc(-250px * 7)); }
            }
            </style>

            <div class="slider">
                <div class="slide-track">
                    <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/2.png" alt="Logo 1"></div>
                    <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/3.png" alt="Logo 2"></div>
                    <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/4.png" alt="Logo 3"></div>
                    <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/5.png" alt="Logo 4"></div>
                    <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/6.png" alt="Logo 5"></div>
                    <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/7.png" alt="Logo 6"></div>
                    <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/1.png" alt="Logo 7"></div>
                    <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/2.png" alt="Logo 1"></div>
                    <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/3.png" alt="Logo 2"></div>
                    <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/4.png" alt="Logo 3"></div>
                    <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/5.png" alt="Logo 4"></div>
                    <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/6.png" alt="Logo 5"></div>
                    <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/7.png" alt="Logo 6"></div>

                </div>
            </div>
            """

            # Render the carousel in Streamlit
            st.components.v1.html(carousel_html, height=150)

    Clients()
