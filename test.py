import base64
import os
import sqlite3
import uuid
from io import BytesIO
from pathlib import Path

import html2text
import pandas as pd
import streamlit as st
import streamlit_antd_components as sac
import streamlit_shadcn_ui as ui
from PIL import Image, ImageDraw
from streamlit_quill import st_quill  # Assuming you have the st_quill package

from data.database import create_database

set_page_config = st.set_page_config(initial_sidebar_state="collapsed", layout="wide")


# Define the path to the local image folder
IMAGE_FOLDER = "static/images"

# Ensure the image folder exists
os.makedirs(IMAGE_FOLDER, exist_ok=True)


# Helper function to create a sample image if no images exist
def create_sample_image():
    image_path = os.path.join(IMAGE_FOLDER, "example.png")
    if not os.path.exists(image_path):
        img = Image.new("RGB", (200, 100), color="blue")
        draw = ImageDraw.Draw(img)
        draw.text((10, 40), "Sample Image", fill="white")
        img.save(image_path)


# Helper function to fetch images sorted by modification time
def get_images():
    return sorted(Path(IMAGE_FOLDER).glob("*.*"), key=os.path.getmtime, reverse=True)


# Function to save uploaded images
def save_uploaded_file(uploaded_file):
    file_path = Path(IMAGE_FOLDER) / uploaded_file.name
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path


# Streamlit App
@st.fragment()
def main():
    # st.title("Quill Editor with Local Image Integration")

    # Ensure at least one sample image exists
    create_sample_image()
    # BTNCTNS = st.empty()
    # Create two columns
    col1, col2 = st.columns([3, 1])

    # Column 1: Quill Editor
    with col1:
        st.markdown(
            """
            <style>
            .element-container:has(> iframe) {
            height: 500px;
            max-height: 500px;
            overflow-y: auto;
            overflow-x: hidden;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        content = st_quill(
            placeholder="Write your text here...",
            html=True,
            key="quill_editor",
        )

    # Column 2: Image List
    with col2:
        with st.container(border=True, height=500):
            # Image upload feature
            uploaded_file = st.file_uploader(
                "Choose an image", type=["png", "jpg", "jpeg", "gif"]
            )
            if uploaded_file is not None:
                file_path = save_uploaded_file(uploaded_file)
                st.success(f"Uploaded: {uploaded_file.name}")

            st.markdown("Drag and Drop Image in the editor")
            images = get_images()

            if images:
                for image_path in images:
                    st.image(image_path, caption=image_path.name)
            else:
                st.write("No images available.")

    svcolbtn, prvcol, htmlcolprev, _ = st.columns([1, 1, 1, 7])

    if svcolbtn.button(label="Save", icon=":material/save:", type="primary"):
        st.toast("Saving...", icon=":material/save:")

    @st.dialog("Preview", width="large")
    def preview():
        if content:
            st.markdown(content, unsafe_allow_html=True)

    @st.dialog("HTML Preview", width="large")
    def html_preview():
        content

    if prvcol.button(
        "Preview",
        icon=":material/visibility:",
        type="tertiary",
    ):
        preview()
    if htmlcolprev.button(label="HTML", icon=":material/html:", type="tertiary"):
        html_preview()


if __name__ == "__main__":
    main()
