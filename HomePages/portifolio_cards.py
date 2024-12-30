from datetime import datetime
import streamlit as st
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

#----------------------------------------------------------------
#       PROJECT-CARDS IMAGE CAROUSEL USING SEGMENTED-CONTROL
#----------------------------------------------------------------
def carousel_with_autoslide(project):
    with st.container(border=True):
        slides = [{"image": img} for img in project["images"]]
        description = project["projectDescription"]

        carousel_key = f"carousel_index_{project['projectId']}"
        if carousel_key not in st.session_state:
            st.session_state[carousel_key] = 0
        image_container = st.empty()
        current_slide = slides[st.session_state[carousel_key]]
        image_container.image(current_slide["image"], use_container_width=True)
        # Segmented control for carousel navigation
        Previous = ":material/arrow_back_ios:"
        Next = ":material/arrow_forward_ios:"
        options = [Previous, f"{st.session_state[carousel_key] + 1}/{len(slides)}", Next]
        selected_option = st.segmented_control(label="Navigate Slides", options=options, key=f"segmented_control_{project['projectId']}", label_visibility="collapsed")
        # Handle navigation
        if selected_option == "Previous":
            st.session_state[carousel_key] = (st.session_state[carousel_key] - 1) % len(slides)
        elif selected_option == "Next":
            st.session_state[carousel_key] = (st.session_state[carousel_key] + 1) % len(slides)

        st.subheader(project["projectTitle"])
        st.write(description)
        detailcol, ratecol, vwrtcol = st.columns(
            [2, 1.5, 1.5], vertical_alignment="center")
        with detailcol:
            if st.button(
                label="Read More",
                key=f"details_{project['projectId']}",
                type="primary",
                icon=":material/open_in_new:",
            ):
                st.session_state.page = "article"
                st.session_state.current_blog = project["projectId"]
                st.session_state.current_published = project["publishDate"]
                st.session_state.last_updated = project["updateDate"]
                st.session_state.blog_content = project["markdownContent"]  
                st.rerun()
 
        with vwrtcol:
            stars = "⭐"
            st.write(stars, "4.9/5 (200)")

#----------------------------------------------------------------
#       PROJECTS NAVIGATION USING SEGMENTED - CONTROL
#----------------------------------------------------------------
@st.fragment()
def portifolio_projects():
    if "page" not in st.session_state:
        st.session_state.page = "projects_Cards"
        st.session_state.current_blog = None

    def Show_Cards():
        project_cards = get_projects()
        unique_tags = get_unique_tags(project_cards)
        selected_tags = st.pills("Filter by Tags", unique_tags, selection_mode="multi")
        filtered_projects = filter_projects_by_tags(project_cards, selected_tags)
        cols = st.columns(3)
        for i, project in enumerate(filtered_projects):
            with cols[i % 3]:
                carousel_with_autoslide(project)

    def show_project():
        projects = get_projects()
        project_ids = [project["projectId"] for project in projects]

        if st.session_state.current_blog is None:
            st.session_state.current_blog = project_ids[0]  

        # Find the current project
        current_index = project_ids.index(st.session_state.current_blog)
        current_project = projects[current_index]
        project_content = current_project["markdownContent"]
        publish_date = current_project["publishDate"]
        last_updated = current_project["updateDate"]

        _, ActnBtn, content_column, _ = st.columns([0.5, 1.5, 7, 1], gap="medium")
        with ActnBtn:
            if st.button("Back",
                icon=":material/arrow_back_ios:",
                type="tertiary",
            ):
                st.session_state.page = "projects_Cards"
                st.rerun()

        with content_column:
            st.markdown(project_content)
            st.divider()
            pbldate, lupdte = st.columns(2, vertical_alignment="bottom")
            pbldate.write(
                f"Published: <span style='font-weight: bold;'>{publish_date}</span>",
                unsafe_allow_html=True,
            )
            lupdte.write(
                f"Last Updated: <span style='font-weight: bold;'>{last_updated}</span>",
                unsafe_allow_html=True,
            )

            st.divider()
            _, ActionCol, _ = st.columns([1,2,1])
            with ActionCol:
                PreviousPage = ":material/arrow_back_ios: Previous"
                RateCurrentProject = "**Rate This Project** :material/thumb_up: "
                NextPage = "Next :material/arrow_forward_ios:"
                options = [PreviousPage, RateCurrentProject, NextPage]
                selected_option = st.segmented_control("Navigation", options,label_visibility="collapsed" )

                if selected_option == PreviousPage:
                    if current_index > 0: 
                        previous_project = current_index - 1
                        st.session_state.current_blog = project_ids[previous_project]
                        st.session_state.blog_content = projects[previous_project]["markdownContent"]
                        st.session_state.current_published = projects[previous_project]["publishDate"]
                        st.session_state.last_updated = projects[previous_project]["updateDate"]
                        st.rerun()

                elif selected_option == RateCurrentProject:
                    st.write("Thank you for rating this project!")

                elif selected_option == NextPage:
                    if current_index < len(project_ids) - 1:  
                        next_project = current_index + 1
                        st.session_state.current_blog = project_ids[next_project]
                        st.session_state.blog_content = projects[next_project]["markdownContent"]
                        st.session_state.current_published = projects[next_project]["publishDate"]
                        st.session_state.last_updated = projects[next_project]["updateDate"]
                        st.rerun()

    # Main render logic
    if st.session_state.page == "projects_Cards":
        Show_Cards()
    elif st.session_state.page == "article":
        show_project()

#----------------------------------------------------------------
#       PROJECT-CARDS IMAGE CAROUSEL USING REGULAR BUTTONS
#----------------------------------------------------------------
# def carousel_with_autoslide(project):
#     with st.container(border=True):
#         slides = [{"image": img} for img in project["images"]]
#         description = project["projectDescription"]
#         publish_date = project["publishDate"]
#         last_updated = project["updateDate"]

#         # Initialize session state for carousel index
#         carousel_key = f"carousel_index_{project['projectId']}"
#         if carousel_key not in st.session_state:
#             st.session_state[carousel_key] = 0

#         # Image container
#         image_container = st.empty()

#         # Navigation buttons for the carousel
#         col1, col2, col3 = st.columns([1, 6, 1], vertical_alignment="center")
#         with col1:
#             if st.button(
#                 label="",
#                 type="tertiary",
#                 key=f"prev_button_{project['projectId']}",
#                 icon=":material/arrow_back_ios:",
#             ):
#                 # Navigate to the previous slide
#                 st.session_state[carousel_key] = (
#                     st.session_state[carousel_key] - 1
#                 ) % len(slides)
#         with col2:
#             # Display current slide number
#             st.markdown(
#                 f"<div style='text-align: center;'>{st.session_state[carousel_key] + 1}/{len(slides)}</div>",
#                 unsafe_allow_html=True,
#             )
#         with col3:
#             if st.button(
#                 label="",
#                 type="tertiary",
#                 key=f"next_button_{project['projectId']}",
#                 icon=":material/arrow_forward_ios:",
#             ):
#                 # Navigate to the next slide
#                 st.session_state[carousel_key] = (
#                     st.session_state[carousel_key] + 1
#                 ) % len(slides)

#         # Get the current slide based on the index
#         current_slide = slides[st.session_state[carousel_key]]
#         image_container.image(current_slide["image"], use_container_width=True)
#         st.subheader(project["projectTitle"])
#         st.write(description)

#         detailcol, ratecol, vwrtcol = st.columns(
#             [2, 1.5, 1.5], vertical_alignment="center"
#         )
#         with detailcol:
#             if st.button(
#                 label="Read More",
#                 key=f"details_{project['projectId']}",
#                 type="primary",
#                 icon=":material/open_in_new:",
#             ):
#                 # st.write("Redirecting to more details page...")
#                 st.session_state.page = "article"
#                 st.session_state.current_blog = project["projectId"]
#                 st.session_state.current_published = project["publishDate"]
#                 st.session_state.last_updated = project["updateDate"]
#                 st.session_state.blog_content = project["markdownContent"]  
#                 st.rerun()
 
#         with vwrtcol:
#             stars = "⭐"
#             st.write(stars, "4.9/5 (200)")

#----------------------------------------------------------------
#       PROJECTS NAVIGATION USING REGULAR BUTTONS
#----------------------------------------------------------------
# @st.fragment()
# def portifolio_projects():
#     if "page" not in st.session_state:
#         st.session_state.page = "projects_Cards"
#         st.session_state.current_blog = None

#     def Show_Cards():
#         project_cards = get_projects()
#         unique_tags = get_unique_tags(project_cards)
#         selected_tags = st.pills("Filter by Tags", unique_tags, selection_mode="multi")
#         filtered_projects = filter_projects_by_tags(project_cards, selected_tags)
#         cols = st.columns(3)
#         for i, project in enumerate(filtered_projects):
#             with cols[i % 3]:
#                 carousel_with_autoslide(project)

#     def show_project():
#         # Fetch project details
#         projects = get_projects()
#         project_ids = [project["projectId"] for project in projects]
        
#         if st.session_state.current_blog is None:
#             st.session_state.current_blog = project_ids[0]  # Default to the first project

#         # Find the current project
#         current_index = project_ids.index(st.session_state.current_blog)
#         current_project = projects[current_index]
#         project_content = current_project["markdownContent"]
#         publish_date = current_project["publishDate"]
#         last_updated = current_project["updateDate"]

#         _, ActnBtn, content_column, _ = st.columns([0.5, 1.5, 7, 1], gap="medium")
#         with ActnBtn:
#             if st.button(
#                 label=":material/view_cozy:  All Projects",
#                 icon=":material/arrow_back_ios:",
#                 type="tertiary",
#             ):
#                 st.session_state.page = "projects_Cards"
#                 st.rerun()

#         with content_column:
#             st.markdown(project_content)
#             st.divider()
#             pbldate, lupdte = st.columns(2, vertical_alignment="bottom")
#             pbldate.write(
#                 f"Published: <span style='font-weight: bold;'>{publish_date}</span>",
#                 unsafe_allow_html=True,
#             )
#             lupdte.write(
#                 f"Last Updated: <span style='font-weight: bold;'>{last_updated}</span>",
#                 unsafe_allow_html=True,
#             )

#             st.divider()

#         # Navigation buttons for "Previous" and "Next"
#         _, previous, rate, next, _ = st.columns([1, 2, 2.7, 1, 0.5])
#         with previous:
#             if st.button(label="Previous", icon=":material/arrow_back_ios:", type="tertiary"):
#                 if current_index > 0:  # Check if it's not the first project
#                     st.session_state.current_blog = project_ids[current_index - 1]
#                     st.session_state.blog_content = projects[current_index - 1]["markdownContent"]
#                     st.session_state.current_published = projects[current_index - 1]["publishDate"]
#                     st.session_state.last_updated = projects[current_index - 1]["updateDate"]
#                     st.rerun()

#         with rate:
#             st.button(label="Rate this project", icon=":material/thumb_up:", type="primary")

#         with next:
#             if st.button(label="Next", icon=":material/arrow_forward_ios:", type="tertiary"):
#                 if current_index < len(project_ids) - 1:  # Check if it's not the last project
#                     st.session_state.current_blog = project_ids[current_index + 1]
#                     st.session_state.blog_content = projects[current_index + 1]["markdownContent"]
#                     st.session_state.current_published = projects[current_index + 1]["publishDate"]
#                     st.session_state.last_updated = projects[current_index + 1]["updateDate"]
#                     st.rerun()

#     # Main render logic
#     if st.session_state.page == "projects_Cards":
#         Show_Cards()
#     elif st.session_state.page == "article":
#         show_project()
