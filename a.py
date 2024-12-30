import streamlit as st
from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

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
                    onChange=lazy(sync("data"))
                )

            with mui.CardActions:
                mui.Button("Apply changes", onClick=sync())


