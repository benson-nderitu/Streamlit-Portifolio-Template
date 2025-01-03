import streamlit as st
from streamlit_elements import dashboard, editor, elements, lazy, media, mui, nivo, sync

st.set_page_config(layout="wide")

markdownContent = """
# Project Four
**Graphics** | **Illustration** | **Creative**

### Description
A creative journey into graphic design and illustration:
- Vector art
- Photo editing
- Storyboarding

#### Published On
October 5, 2023

#### Last Updated
October 10, 2023
            """
layout = [
    dashboard.Item("editor", 0, 0, 12, 4),
]

with elements("demo"):
    with dashboard.Grid(layout, draggableHandle=".draggable"):
        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Editor", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                editor.Monaco(
                    defaultValue=markdownContent,
                    language="markdown",
                    onChange=lazy(sync("data")),
                )

            with mui.CardActions:
                mui.Button("Apply changes", onClick=sync())


# import streamlit as st
# from streamlit_float import float_css_helper, float_init

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

# # Step 5: Add a button to trigger the scroll to top action. Both ways work... personal preference
# button_container.button(
#     on_click=scroll, label="", icon=":material/arrow_upward:", type="primary"
# )
