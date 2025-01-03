from datetime import datetime

import streamlit as st

from components.horizontal import st_horizontal
from Data.alldata import get_projects

primary_color = st.get_option("theme.primaryColor")


def get_unique_tags(projects):
    unique_tags = set()
    for project in projects:
        tags = project.get("tags", [])
        unique_tags.update(tags)
    return ["All"] + sorted(unique_tags)


# Filtering projects based on selected tags
def filter_projects_by_tags(projects, selected_tags):
    if "All" in selected_tags or not selected_tags:
        return projects
    return [
        project
        for project in projects
        if any(tag in selected_tags for tag in project.get("tags", []))
    ]


def parse_dataframe(df):
    """
    Parses a DataFrame to convert 'tags' and 'images' columns from comma-separated strings to arrays.

    Args:
        df (pd.DataFrame): Input DataFrame with 'tags' and 'images' as comma-separated strings.

    Returns:
        pd.DataFrame: Updated DataFrame with 'tags' and 'images' as arrays.
    """
    # Convert 'images' column to lists
    if "images" in df.columns:
        df["images"] = df["images"].apply(
            lambda x: x.split(",") if isinstance(x, str) else x
        )

    # Convert 'tags' column to lists
    if "tags" in df.columns:
        df["tags"] = df["tags"].apply(
            lambda x: x.split(",") if isinstance(x, str) else x
        )

    return df


# ----------------------------------------------------------------
#       PROJECT-CARDS IMAGE CAROUSEL USING REGULAR BUTTONS
# ----------------------------------------------------------------
def carousel_with_autoslide(project):
    with st.container(border=True):
        slides = [{"image": img} for img in project["images"]]
        description = project["projectDescription"]

        # Initialize session state for carousel index
        carousel_key = f"carousel_index_{project['projectId']}"
        if carousel_key not in st.session_state:
            st.session_state[carousel_key] = 0

        # Image container
        image_container = st.empty()

        with st_horizontal():
            if st.button(
                label="",
                type="tertiary",
                key=f"prev_button_{project['projectId']}",
                icon=":material/arrow_back_ios:",
            ):
                # Navigate to the previous slide
                st.session_state[carousel_key] = (
                    st.session_state[carousel_key] - 1
                ) % len(slides)

            st.markdown(
                f"<div style='text-align: center;'>{st.session_state[carousel_key] + 1}/{len(slides)}</div>",
                unsafe_allow_html=True,
            )

            if st.button(
                label="",
                type="tertiary",
                key=f"next_button_{project['projectId']}",
                icon=":material/arrow_forward_ios:",
            ):
                # Navigate to the next slide
                st.session_state[carousel_key] = (
                    st.session_state[carousel_key] + 1
                ) % len(slides)

        # Get the current slide based on the index
        current_slide = slides[st.session_state[carousel_key]]
        image_container.image(current_slide["image"], use_container_width=True)
        st.subheader(project["projectTitle"])
        st.write(description)

        with st_horizontal():
            if st.button(
                label="Read More",
                key=f"details_{project['projectId']}",
                type="primary",
                icon=":material/open_in_new:",
            ):
                # st.write("Redirecting to more details page...")
                st.session_state.page = "article"
                st.session_state.current_blog = project["projectId"]
                st.session_state.current_published = project["publishDate"]
                st.session_state.last_updated = project["updateDate"]
                st.session_state.blog_content = project["markdownContent"]
                st.rerun()

            stars = "⭐"
            st.write(stars, "4.9/5 (200)")


# ----------------------------------------------------------------
#       PROJECTS NAVIGATION USING REGULAR BUTTONS
# ----------------------------------------------------------------
@st.fragment()
def portifolio_projects():
    if "page" not in st.session_state:
        st.session_state.page = "projects_Cards"
        st.session_state.current_blog = None

    def Show_Cards():
        project_cards = parse_dataframe(get_projects()).to_dict(orient="records")

        unique_tags = get_unique_tags(project_cards)
        selected_tags = st.pills("Filter by Tags", unique_tags, selection_mode="multi")
        filtered_projects = filter_projects_by_tags(project_cards, selected_tags)
        cols = st.columns(3)
        for i, project in enumerate(filtered_projects):
            with cols[i % 3]:
                carousel_with_autoslide(project)

    def show_project():
        projects = parse_dataframe(get_projects()).to_dict(orient="records")
        project_ids = [project["projectId"] for project in projects]

        if st.session_state.current_blog is None:
            st.session_state.current_blog = project_ids[0]

        # Find the current project
        current_index = project_ids.index(st.session_state.current_blog)
        current_project = projects[current_index]
        project_content = current_project["markdownContent"]
        publish_date = current_project["publishDate"]
        last_updated = current_project["updateDate"]

        with st_horizontal():

            if st.button(
                "Back",
                icon=":material/arrow_back_ios:",
                type="tertiary",
                # help="Go back ALL projects",
                use_container_width=True,
            ):
                st.session_state.page = "projects_Cards"
                st.rerun()
            st.write(
                f"""<div style="font-size:12px; padding: none; margin:none; text-align:end; white-space: nowrap;">
    <p>Published: <span style='font-weight: bold;'>{publish_date}</span> &nbsp; | &nbsp; Last Updated: <span style='font-weight: bold;'>{last_updated}</span></p></div>
    """,
                unsafe_allow_html=True,
            )

        _, ActnBtn, _, content_column, _ = st.columns(
            [0.2, 1, 0.75, 7, 1],
        )

        with content_column:
            st.markdown(project_content)
            st.divider()

            with st_horizontal():
                if st.button(
                    label=":material/view_cozy:  All",
                    type="tertiary",
                    key="lowerbackbutton",
                ):
                    st.session_state.page = "projects_Cards"
                    st.rerun()
                if st.button(
                    label=":material/arrow_back_ios: Previous", type="tertiary"
                ):
                    if current_index > 0:  # Check if it's not the first project
                        st.session_state.current_blog = project_ids[current_index - 1]
                        st.session_state.blog_content = projects[current_index - 1][
                            "markdownContent"
                        ]
                        st.session_state.current_published = projects[
                            current_index - 1
                        ]["publishDate"]
                        st.session_state.last_updated = projects[current_index - 1][
                            "updateDate"
                        ]
                        st.rerun()

                @st.dialog("Cast your vote")
                def vote():
                    st.write(f"Why is your favorite?")

                if st.button(
                    label=":material/thumb_up: Rate this project",
                    type="primary",
                ):
                    vote()

                if st.button(
                    label="Next :material/arrow_forward_ios:", type="tertiary"
                ):
                    if (
                        current_index < len(project_ids) - 1
                    ):  # Check if it's not the last project
                        st.session_state.current_blog = project_ids[current_index + 1]
                        st.session_state.blog_content = projects[current_index + 1][
                            "markdownContent"
                        ]
                        st.session_state.current_published = projects[
                            current_index + 1
                        ]["publishDate"]
                        st.session_state.last_updated = projects[current_index + 1][
                            "updateDate"
                        ]
                        st.rerun()

    # Main render logic
    if st.session_state.page == "projects_Cards":
        Show_Cards()
    elif st.session_state.page == "article":
        show_project()
