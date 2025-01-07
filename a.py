# import streamlit as st
# from streamlit_elements import dashboard, editor, elements, lazy, media, mui, nivo, sync

# st.set_page_config(layout="wide")

# markdownContent = """
# # Project Four
# **Graphics** | **Illustration** | **Creative**

# ### Description
# A creative journey into graphic design and illustration:
# - Vector art
# - Photo editing
# - Storyboarding

# #### Published On
# October 5, 2023

# #### Last Updated
# October 10, 2023
#             """
# layout = [
#     dashboard.Item("editor", 0, 0, 12, 4),
# ]

# with elements("demo"):
#     with dashboard.Grid(layout, draggableHandle=".draggable"):
#         with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):
#             mui.CardHeader(title="Editor", className="draggable")
#             with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
#                 editor.Monaco(
#                     defaultValue=markdownContent,
#                     language="markdown",
#                     onChange=lazy(sync("data")),
#                 )

#             with mui.CardActions:
#                 mui.Button("Apply changes", onClick=sync())


# import streamlit as st
# from streamlit_float import float_css_helper,

# # Initialize the float feature
# float_init()

# # Create a container for the button
# button_container = st.container()

# # Define custom CSS for positioning
# custom_css = float_css_helper(
#     bottom="5% ",
#     width="50px ",
#     height="50px",
#     right="2%",
#     background="transparent",
#     border_radius="50% ",
#     cursor="pointer",
# )

# # Apply the floating effect with custom CSS
# button_container.float(custom_css)

# from streamlit_scroll_to_top import scroll_to_here

# # Step 1: Initialize scroll state in session_state
# if "scroll_to_top" not in st.session_state:
#     st.session_state.scroll_to_top = False

# if "scroll_to_header" not in st.session_state:
#     st.session_state.scroll_to_header = False

# # Step 2: Handle the scroll-to-top action
# if st.session_state.scroll_to_top:
#     scroll_to_here(0, key="top")  # Scroll to the top of the page
#     st.session_state.scroll_to_top = False  # Reset the state after scrolling


# # Step 3: Define a scroll function to trigger the state change
# def scroll():
#     st.session_state.scroll_to_top = True


# def scrollheader():
#     st.session_state.scroll_to_header = True


# # Step 4: Add some dummy content to simulate a long page
# st.title("Dummy Content")
# st.write("Scroll down to see the 'Scroll to Top' button.")
# for i in range(50):  # Generate dummy content
#     if i == 25:
#         if st.session_state.scroll_to_header:
#             scroll_to_here(0, key="header")  # Scroll to the top of the page
#             st.session_state.scroll_to_header = False  # Reset the state after scrolling
#         st.header("Or scroll here")
#     st.text(f"Line {i + 1}: This is some dummy content.")

# ------------------------------------------------------------------------------
# import numpy as np
# import streamlit as st


# def Metric_circle(
#     Label=None,  # string - not styled
#     progress=0,  # int
#     outOf=100,  # int
#     units="%",  # string
#     background_stroke_width=5,  # int
#     progress_stroke_width=None,  # int
#     primary_color=None,  # string
#     text_color=None,  # string
#     size=100,  # int - in px
#     text_size=18,  # int
# ):
#     # Get the primary color from Streamlit theme if not provided
#     if not primary_color:
#         primary_color = st.get_option("theme.primaryColor")

#     # Set progress stroke width same as background stroke width if not provided
#     if progress_stroke_width is None:
#         progress_stroke_width = background_stroke_width

#     # Circle size is 95% of the parent size
#     circle_size = 0.95 * size

#     # Radius calculation
#     radius = (circle_size - max(background_stroke_width, progress_stroke_width)) / 2

#     # Total circumference of the circle
#     circumference = 2 * np.pi * radius

#     # Stroke-dashoffset for anti-clockwise progress (fraction of progress/outOf)
#     progress_fraction = progress / outOf
#     progress_length = progress_fraction * circumference
#     dash_offset = circumference - progress_length

#     # Text color defaults to primary color if not provided
#     if not text_color:
#         text_color = primary_color

#     # SVG structure for the metric circle
#     svg = f"""
#     <svg width="{size}px" height="{size}px" viewBox="0 0 {circle_size} {circle_size}" xmlns="http://www.w3.org/2000/svg">
#         <!-- Background Circle -->
#         <circle cx="{circle_size/2}" cy="{circle_size/2}" r="{radius}" stroke="#ddd" stroke-width="{background_stroke_width}" fill="transparent"/>
#         <!-- Progress Circle -->
#         <circle cx="{circle_size/2}" cy="{circle_size/2}" r="{radius}" stroke="{primary_color}" stroke-width="{progress_stroke_width}" fill="transparent"
#             stroke-dasharray="{circumference}" stroke-dashoffset="{dash_offset}" stroke-linecap="round" transform="rotate(-90, {circle_size/2}, {circle_size/2})"/>
#         <!-- Center Text -->
#         <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="{text_size}" fill="{text_color}">{progress}{units}</text>
#     </svg>
#     """

#     # Display Label if provided
#     if Label:
#         st.markdown(f"**{Label}**")

#     # Render the SVG in Streamlit
#     st.markdown(svg, unsafe_allow_html=True)


# # Example usages in Streamlit

# # Example 1: Simple Metric Circle
# Metric_circle(
#     Label="Site Completion",
#     progress=98,
#     outOf=100,
#     units="%",
#     progress_stroke_width=18,
#     size=350,
#     text_size=24,
# )

# # Example 2: Custom Stroke Widths and Size
# Metric_circle(
#     Label="Task Completion",
#     progress=40,
#     outOf=100,
#     units="%",
#     background_stroke_width=4,
#     progress_stroke_width=6,
#     size=200,
#     text_size=24,
# )


# ------------------------------------------------------------------------------
import streamlit as st
from streamlit_donut import st_donut

st_donut(
    label="Project Completion",
    value=89,
    outOf=100,
    units="days",
    size=150,
    value_text_color="purple",
    text_size=24,
    background_stroke_width=10,
    arc_stroke_width=20,
    direction="clockwise",
    delta="90%",
    rounded=True,
    label_visibility=True,
    hide_background=True,
)

st_donut(
    label="Counterclockwise",
    value=89,
    outOf=100,
    units="days",
    value_text_color="purple",
    text_size=24,
    background_stroke_width=30,
    arc_stroke_width=40,
    direction="counterclockwise",
    delta="90%",
    rounded=True,
    label_visibility=False,
    hide_background=True,
)
