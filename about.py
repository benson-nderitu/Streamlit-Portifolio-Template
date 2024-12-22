import time
from datetime import datetime

import streamlit as st
import streamlit_antd_components as sac

from data.alldata import get_project_cards
from portifolio import carousel_with_autoslide

primary_color = st.get_option("theme.primaryColor")

# Define a reusable functions
def styled_title(normal_text, styled_text, styled_color="blue"):
    """
    Creates a styled title with two parts: normal text and a colored styled text.

    Parameters:
        normal_text (str): The normal text part of the title.
        styled_text (str): The styled text part of the title.
        styled_color (str): The color of the styled text (default is blue).
    """
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


@st.fragment()
def resume_about():
    # --- HERO SECTION ---
    @st.fragment
    def heroprofile():
        with st.container(key="heroContainer"):
            NAME = "John Doe"
            DESCRIPTION = """
            Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
            """
            col1, col2 = st.columns(2, gap="small")
            with col1:
                with st.container(key="CTAContainer"):
                    st.title(NAME)
                    st.write(DESCRIPTION)
                    ctacol, cta2col = st.columns([2, 3])
                    with ctacol:
                        if st.button(
                            label="View Work",
                            icon=":material/business_center:",
                            type="primary",
                        ):
                            st.write("View WORK")

                    with cta2col:
                        # if st.button(
                        #     label="Services",
                        #     icon=":material/support_agent:",
                        # ):
                        if st.button(
                            label="Contact Me",
                            icon=":material/call:",
                        ):
                            st.write("Contacting...")

            with col2:
                with st.container(key="profileImageContainer"):
                    st.image("static/profile.png", use_container_width=True)

    heroprofile()

    @st.fragment
    def AboutMe():
        with st.container(key="AboutMeContainer"):
            abttle, abtdesc, abtvideo = st.columns([1, 3, 2])
            with abttle:
                with st.container(key="AboutMeTitleContainer"):
                    styled_title("About", "ME", primary_color)

            with abtdesc:
                with st.container(key="AboutMeDescriptionContainer"):
                    st.markdown(
                        "**Hello!, I'm Benson Nderitu, a data analyst based in Nairobi, Kenya.**"
                    )
                    st.write(
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
                    )
                    st.markdown(
                        "**The gateway to advanced learning lies ahead, with a focus on achieving the right balance. Move forward with purpose, enriching your approach step by step. At every beginning, the essentials are key.**"
                    )
                    viewcol, downloadcol = st.columns(2)
                    with viewcol:
                        if st.button(
                            label="Read CV",
                            icon=":material/open_in_new:",
                            type="primary",
                        ):
                            st.write("View CV")
                    with downloadcol:
                        if st.button(
                            label="Download CV",
                            icon=":material/download:",
                            key="download_resume",
                            type="primary",
                        ):
                            st.write("Downloading...")
                        # st.download_button(
                        #     label=" 📄 Download CV",
                        #     data=PDFbyte,
                        #     file_name=resume_file.name,
                        #     mime="application/octet-stream",
                        # )
                    # --- SOCIAL LINKS ---
                    st.divider()
                    sac.buttons(
                        [
                            sac.ButtonsItem(
                                icon="linkedin",
                                color="#0077B5",
                                href="https://www.linkedin.com/in/benson-nderitu-88776215b",
                            ),
                            sac.ButtonsItem(
                                icon="youtube",
                                color="#FF0000",
                                href="https://youtube.com/@scho_da?si=wr1UcYXz7gcHFAeY",
                            ),
                            sac.ButtonsItem(
                                icon="github",
                                color="#181717",
                                href="https://github.com/benson-nderitu",
                            ),
                            sac.ButtonsItem(
                                icon="twitter",
                                color="#1DA1F2",
                                href="https://twitter.com/BensonN41451654",
                            ),
                        ],
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

    @st.fragment
    def MyServices():
        with st.container(key="MyServicesContainer"):
            msrttl, servscol = st.columns([1, 4])
            with msrttl:
                styled_title("My", "SERVICES", primary_color)
            with servscol:
                # Define a function to render the components dynamically
                def render_components(components):
                    col1, col2, col3 = st.columns(3)
                    # Loop through the list and render each item
                    for idx, component in enumerate(components):
                        title = component.get("title", "Untitled")
                        description = component.get(
                            "description", "No description available."
                        )
                        icon_name = component.get(  # icons from Bootstrap Icons
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
                            st.markdown(
                                """
                                <style>
                                .container-with-border { padding: 20px;margin: 20px;}
                                </style>
                                <div class="container-with-border">
                                """,
                                unsafe_allow_html=True,
                            )

                            # iconcol, titlecol = st.columns([1, 3])
                            # with iconcol:
                            with st.container(border=True):
                                # Render the button with icon
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
                                # with titlecol:
                                st.subheader(title)
                                st.markdown(
                                    f"""
                                        <div style="text-align: center;">
                                            <p>{description}</p>
                                        </div>
                                        """,
                                    unsafe_allow_html=True,
                                )

                # Example service component list
                components_data = [
                    {
                        "title": "Web Development",
                        "description": "Lorem ipsum dolor sit amet.",
                        "icon": "laptop",
                    },
                    {
                        "title": "UI / UX Design",
                        "description": "Lorem ipsum dolor sit amet.",
                        "icon": "pen",
                    },
                    {
                        "title": "App Development",
                        "description": "Lorem ipsum dolor sit amet.",
                        "icon": "phone",
                    },
                    {
                        "title": "Photography",
                        "description": "Lorem ipsum dolor sit amet.",
                        "icon": "camera",
                    },
                    {
                        "title": "Rebranding",
                        "description": "Lorem ipsum dolor sit amet.",
                        "icon": "send",
                    },
                    {
                        "title": "SEO Marketing",
                        "description": "Lorem ipsum dolor sit amet.",
                        "icon": "globe",
                    },
                ]

                # Call the render function
                render_components(components_data)

    MyServices()

    @st.fragment
    def MySkills():
        with st.container(key="SkillsContainer"):
            sklttl, skillscol = st.columns([1, 3])
            with sklttl:
                styled_title("My", "SKILLS", primary_color)
            with skillscol:
                with st.container(key="SkillsListContainer"):
                    descrcol, progcol = st.columns(2)
                    with descrcol:
                        st.markdown("### WHAT YOU NEED TO KNOW")
                        st.markdown(
                            "**Hello!, I'm Benson Nderitu, a data analyst based in Nairobi, Kenya.**"
                        )
                        st.write(
                            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
                        )
                        st.markdown(
                            "**The gateway to advanced learning lies ahead, with a focus on achieving the right balance. Move forward with purpose, enriching your approach step by step. At every beginning, the essentials are key.**"
                        )
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
                                        # time.sleep(0.01)  # Adjust sleep time for speed
                                        progressbar.progress(percent_complete + 1)

                        skills = [
                            {"name": "WordPress", "percentage": 95},
                            {"name": "HTML & CSS3", "percentage": 70},
                            {"name": "Photoshop", "percentage": 80},
                            {"name": "Illustrator", "percentage": 90},
                        ]
                        render_skills(skills)

    MySkills()

    @st.fragment
    def MyStory():
        with st.container(key="ExperienceContainer"):
            expttl, expscol = st.columns([1, 3])
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
                                yrcol, expcol = st.columns(
                                    [1, 5]
                                )  # Define columns for year and details
                                with yrcol:
                                    st.write(f"#### {year}")
                                with expcol:
                                    st.markdown(f"### {title}")
                                    st.markdown(f"**{role}**")
                                    st.write(description)

                    # Example Data for Timeline
                    timeline_entries = [
                        {
                            "year": "2016",
                            "title": "Envato Studio",
                            "role": "Lead Web Designer",
                            "description": (
                                "This was the time when we started our company. We had no idea how far we would go, "
                                "we weren’t even sure that we would be able to survive for a few years. What drove us to "
                                "start the company was the understanding that we could provide a service no one else was providing."
                            ),
                        },
                        {
                            "year": "2018",
                            "title": "Envato Studio",
                            "role": "Senior Web Developer",
                            "description": (
                                "During this time, we expanded our services and built a reputation in the market. Our focus "
                                "was on providing high-quality solutions tailored to the client’s needs."
                            ),
                        },
                        {
                            "year": "2020 - Present",
                            "title": "Envato Studio",
                            "role": "Lead Web Developer",
                            "description": (
                                "This was the time when we started our company. We had no idea how far we would go, we weren’t even sure "
                                "that we would be able to survive for a few years. What drove us to start the company was the understanding "
                                "that we could provide a service no one else was providing."
                            ),
                        },
                    ]

                    # Render the timeline
                    render_timeline(timeline_entries)

    MyStory()

    @st.fragment
    def portfolio_section():
        with st.container(key="PortfolioContainer"):
            styled_title("My", "PORTFOLIO", primary_color)
            ttlcol, rdtbtncol = st.columns([3, 1])
            with rdtbtncol:
                if st.button(
                    label="View All",
                    key="portfolio_read_more",
                    type="primary",
                    icon=":material/open_in_new:",
                    use_container_width=True,
                ):
                    st.write("Redirecting to portfolio page...")

            def get_latest_projects(projects, n=3):
                # Sort the projects by publishDate in descending order and get the top n projects
                sorted_projects = sorted(
                    projects,
                    key=lambda x: datetime.strptime(x["publishDate"], "%Y-%m-%d"),
                    reverse=True,
                )
                return sorted_projects[:n]

            project_cards = get_project_cards()
            latest_projects = get_latest_projects(project_cards)

            cols = st.columns(3)
            for i, project in enumerate(latest_projects):
                with cols[i % 3]:
                    carousel_with_autoslide(project)

    portfolio_section()

    @st.fragment
    def Reviews():
        with st.container(key="ReviewsContainer"):
            st.markdown("### WHAT PEOPLE ARE SAYING")

            def review_section_with_navigation(reviews):
                """
                Displays a review section with left and right navigation buttons.

                Args:
                    reviews (list): A list of dictionaries, where each dictionary contains keys 'rating', 'text', and 'author'.
                """
                if "review_index" not in st.session_state:
                    st.session_state.review_index = 0

                # Get the current review based on the index
                current_review = reviews[st.session_state.review_index]

                with st.container():
                    imgcol, desccol = st.columns([1, 3], gap="medium")

                    # Profile image or placeholder
                    with imgcol:
                        # st.image("static/profile.png", use_container_width=True)
                        st.image(current_review["image"], use_container_width=True)

                    # Review text and details
                    with desccol:
                        st.markdown(
                            f"""
                            ⭐ {current_review['rating']}/5

                            **"{current_review['text']}"**

                            — {current_review['author']}
                            """
                        )

                    # Navigation buttons for switching reviews
                    _, leftcol, rightcol, _ = st.columns([2, 1, 1, 2], gap="medium")

                    with leftcol:
                        if st.button(
                            "",
                            key="prev_review",
                            help="View the previous review",
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
                            help="View the next review",
                            type="tertiary",
                            icon=":material/arrow_forward_ios:",
                        ):
                            st.session_state.review_index = (
                                st.session_state.review_index + 1
                            ) % len(reviews)

            # Example reviews data
            reviews_data = [
                {
                    "rating": 5,
                    "text": "I loved the project. It was a great learning experience.",
                    "author": "John Doe",
                    "image": "static/profile.png",
                },
                {
                    "rating": 4.5,
                    "text": "Amazing work! Truly exceeded my expectations.",
                    "author": "Jane Smith",
                    "image": "static/logo.png",
                },
                {
                    "rating": 5,
                    "text": "Fantastic job! Highly recommend.",
                    "author": "Alex Johnson",
                    "image": "static/profile.png",
                },
            ]

            # Display the review section
            review_section_with_navigation(reviews_data)

    Reviews()

    @st.fragment
    def Blog():
        with st.container(border=True, key="BlogContainer"):

            st.write("Blog")

    Blog()

    @st.fragment
    def Contact():
        with st.container(border=True, key="ContactContainer"):
            st.write("Contact")

    Contact()

    @st.fragment
    def Clients():
        with st.container(border=True, key="ClientsContainer"):
            st.write("Clients")

    Clients()

    @st.fragment
    def Social():
        with st.container(border=True, key="SocialContainer"):
            st.write("Social")

    Social()

    @st.fragment
    def Footer():
        with st.container(border=True, key="FooterContainer"):
            st.write("Footer")

    Footer()

    # st.markdown(
    #     """
    # <style>
    # hr {
    #     background-image: linear-gradient(to right, #3498db, #2ecc71, #e74c3c, #f1c40f, #34495e, #f39c12);
    #     padding: 1px;
    # }
    # </style>
    # <hr/>
    # """,
    #     unsafe_allow_html=True,
    # )
