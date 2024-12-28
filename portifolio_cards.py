from datetime import datetime

import streamlit as st

from data.alldata import get_project_cards


def get_unique_tags(projects):
    """
    Extracts all unique tags from a list of projects.

    Args:
        projects (list of dict): The dataset of project cards.

    Returns:
        list: A sorted list of unique tags with 'All' as the first option.
    """
    unique_tags = set()
    for project in projects:
        tags = project.get("tags", [])
        unique_tags.update(tags)
    # Convert the set to a sorted list and add 'All' at the start
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


def carousel_with_autoslide(project):
    with st.container(border=True):
        slides = [{"image": img} for img in project["images"]]
        description = project["projectDescription"]
        publish_date = project["publishDate"]
        last_updated = project["updateDate"]

        # Initialize session state for carousel index
        carousel_key = f"carousel_index_{project['projectId']}"
        if carousel_key not in st.session_state:
            st.session_state[carousel_key] = 0

        # Image container
        image_container = st.empty()

        # Navigation buttons for the carousel
        col1, col2, col3 = st.columns([1, 6, 1], vertical_alignment="center")
        with col1:
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
        with col2:
            # Display current slide number
            st.markdown(
                f"<div style='text-align: center;'>{st.session_state[carousel_key] + 1}/{len(slides)}</div>",
                unsafe_allow_html=True,
            )
        with col3:
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

        pbldate, lupdte = st.columns(2, vertical_alignment="bottom")
        with pbldate:
            st.write(
                f"Published: <span style='font-weight: bold;'>{publish_date}</span>",
                unsafe_allow_html=True,
            )
        with lupdte:
            st.write(
                f"Last Updated: <span style='font-weight: bold;'>{last_updated}</span>",
                unsafe_allow_html=True,
            )

        detailcol, ratecol, vwrtcol = st.columns(
            [2, 1.5, 1.5], vertical_alignment="center"
        )
        with detailcol:
            if st.button(
                label="Read More",
                key=f"details_{project['projectId']}",
                type="primary",
                icon=":material/open_in_new:",
            ):
                st.write("Redirecting to more details page...")
        with ratecol:
            if st.button(
                label="Rate",
                icon=":material/thumb_up_alt:",
                key=f"rate_{project['projectId']}",
            ):
                st.write("Thank you for rating this project!")
        with vwrtcol:
            stars = "⭐"
            st.write(stars, "4.9/5 (200)")


@st.fragment()
def portifolio_projects():
    project_cards = get_project_cards()
    unique_tags = get_unique_tags(project_cards)
    # Create pills
    selected_tags = st.pills("Filter by Tags", unique_tags, selection_mode="multi")
    # Filter projects based on selected tags
    filtered_projects = filter_projects_by_tags(project_cards, selected_tags)
    # Generate & Display projects cards in columns
    cols = st.columns(3)
    for i, project in enumerate(filtered_projects):
        with cols[i % 3]:  # Cycle through columns for each project
            carousel_with_autoslide(project)
