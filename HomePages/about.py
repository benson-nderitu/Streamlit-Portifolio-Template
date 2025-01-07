import os
import time
from datetime import datetime

import streamlit as st
import streamlit_antd_components as sac
import streamlit_shadcn_ui as ui

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
    def heroprofile():
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
                    styled_title(
                        normal_text="About",
                        styled_text="ME",
                        styled_color=primary_color,
                    )

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
    #      STATISTICS SECTION
    # ----------------------------------------------------------------
    @st.fragment
    def Statistics():
        with st.container(key="StatisticsContainer"):
            styled_title(
                normal_text=None,
                styled_text=None,
                styled_color=primary_color,
            )

            get_projects().shape[0]
            from components.horizontal import st_horizontal
            from components.streamlit_donut import st_donut

            progress1 = st.slider("Progress", -100, 100, 10)
            # size = 72
            size = 200
            text_size = 24
            with st_horizontal():
                st_donut(
                    label="Site Completion",
                    value=progress1,
                    outOf=100,
                    units="%",
                    size=size,
                    value_text_color="purple",
                    text_size=text_size,
                    background_stroke_width=30,
                    arc_stroke_width=40,
                    # direction="anticlockwise",
                    delta="-10%",
                    rounded=True,
                    label_visibility=False,
                    hide_background=True,
                )
                st_donut(
                    label="Site Completion",
                    value=progress1,
                    outOf=100,
                    units="$",
                    background_stroke_width=20,
                    arc_stroke_width=50,
                    size=size,
                    text_size=text_size,
                    direction="anticlockwise",
                    rounded=False,
                    label_visibility=False,
                    hide_background=True,
                )

        with st_horizontal():
            st_donut(
                label="Site Completion",
                value=progress1,
                units="%",
                delta="10%",
                direction="clockwise",
                hide_background=True,
                label_visibility=False,
            )
            st_donut(
                label="Site Completion",
                value=progress1,
                units="%",
                delta="10%",
                direction="anticlockwise",
                hide_background=True,
                rounded=False,
                label_visibility=False,
            )
            # st_donut(
            #         label="Site Completion",
            #         value=progress1,
            #         outOf=100,
            #         units="%",
            #         size=size,
            #         value_text_color="purple",
            #         text_size=text_size,
            #         background_stroke_width=50,
            #         # direction="anticlockwise",
            #         rounded=True,
            #         delta="-10%",
            #         # label_visibility=False,
            #     )

    Statistics()

    # ----------------------------------------------------------------
    #      MY SERVICES SECTION
    # ----------------------------------------------------------------
    @st.fragment
    def MyServices():
        with st.container(key="MyServicesContainer"):
            msrttl, servscol = st.columns([1, 4])
            with msrttl:
                styled_title(
                    normal_text="My", styled_text="SERVICES", styled_color=primary_color
                )
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
                styled_title(
                    normal_text="My", styled_text="SKILLS", styled_color=primary_color
                )
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

    MyStory()

    # ----------------------------------------------------------------
    #    PORTFOLIO PREVIEW SECTION
    # ----------------------------------------------------------------

    # @st.fragment
    # def portfolio_section():
    #     with st.container(key="PortfolioContainer"):
    # styled_title(normal_text="My", styled_text="PORTFOLIO", styled_color=primary_color)
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
    #      RECOGNITION SECTION
    # ----------------------------------------------------------------
    @st.fragment
    def Recognition():
        with st.container(key="RecognitionContainer"):
            recgttl, recgscol = st.columns([1, 4])
            with recgttl:
                styled_title(styled_text="Recognition", styled_color=primary_color)
            with recgscol.container(key="RecognitionListContainer"):

                # Function to display items in the desired format
                def display_section(
                    title, items, icon=":material/check_circle:", color=":primary"
                ):
                    """
                    Displays a section with a subheader and formatted items using Streamlit.

                    Args:
                        title (str): Title of the section (e.g., "Awards Received").
                        items (list): List of items to display under the section.
                        icon (str): Icon to use before each item. Default is ":material/check_circle:".
                        color (str): Color styling for the icon. Default is ":primary:".
                    """
                    st.subheader(title, divider=True)
                    formatted_items = "\n\n".join(
                        [f"{color}[{icon}] {item}" for item in items]
                    )
                    st.markdown(formatted_items)

                certifications = [
                    "Certified Data Scientist (Google)",
                    "AWS Cloud Practitioner",
                    "UX Design Bootcamp Certification",
                ]

                awards = [
                    "Innovator Award 2023",
                    "Best Data Visualization, XYZ Hackathon",
                    "Client Excellence Award",
                ]
                col1, col2 = st.columns(2, gap="large")
                with col1:
                    display_section("Certifications", certifications)

                with col2:
                    display_section("Awards Received", awards)

    Recognition()

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
                            help="Previous",
                            type="tertiary",
                            icon=":material/arrow_back_ios:",
                        ):
                            st.session_state.review_index = (
                                st.session_state.review_index - 1
                            ) % len(reviews)
                            st.rerun()

                    with rightcol:
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
    # @st.fragment
    # def Clients():
    #     with st.container(key="ClientsContainer"):
    #         # styled_title(styled_text="Clients", styled_color=primary_color)

    #         # SOURCE: https://codepen.io/kevinwitkowski/pen/MWbxNGe
    #         carousel_html = """
    #         <style>
    #         body {
    #             margin: 0;
    #             padding: 0;
    #             font-family: sans-serif;
    #             display: flex;
    #             justify-content: center;
    #             align-items: center;
    #             height: 100vh;
    #             background-color: transparent;
    #         }
    #         .slider {
    #             height: 100px;
    #             margin: auto;
    #             overflow: hidden;
    #             position: relative;
    #             width: 100%;
    #             background: red !important;
    #         }
    #         .slide-track {
    #             animation: scroll 40s linear infinite;
    #             display: flex;
    #             width: calc(250px * 14);

    #         }
    #         .slide {
    #             height: 100px;
    #             width: 250px;
    #         }
    #         .slide img {
    #             width: 100%;
    #             height: 100%;
    #             object-fit: cover;
    #         }
    #         @keyframes scroll {
    #             0% { transform: translateX(0); }
    #             100% { transform: translateX(calc(-250px * 7)); }
    #         }
    #         </style>

    #         <div class="slider">
    #             <div class="slide-track">
    #                 <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/2.png" alt="Logo 1"></div>
    #                 <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/3.png" alt="Logo 2"></div>
    #                 <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/4.png" alt="Logo 3"></div>
    #                 <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/5.png" alt="Logo 4"></div>
    #                 <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/6.png" alt="Logo 5"></div>
    #                 <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/7.png" alt="Logo 6"></div>
    #                 <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/1.png" alt="Logo 7"></div>
    #                 <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/2.png" alt="Logo 1"></div>
    #                 <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/3.png" alt="Logo 2"></div>
    #                 <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/4.png" alt="Logo 3"></div>
    #                 <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/5.png" alt="Logo 4"></div>
    #                 <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/6.png" alt="Logo 5"></div>
    #                 <div class="slide"><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/7.png" alt="Logo 6"></div>

    #             </div>
    #         </div>
    #         """

    #         # Render the carousel in Streamlit
    #         st.components.v1.html(carousel_html, height=150)

    # Clients()


# TODO: Add a section for statistics

# 1. Number of blog posts or portfolio items.
# 2. Number of followers or subscribers.
