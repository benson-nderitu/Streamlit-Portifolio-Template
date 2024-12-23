import os
import sqlite3

import pandas as pd
import streamlit as st

# Get the path to the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))


# Function to fetch profile
def fetch_profile():
    db_path = os.path.join(current_dir, "DATABASE.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, description, profile_image, introduction, about_me_description, about_me_closingTag, about_me_video FROM profiles WHERE id = 1"
    )
    profile = cursor.fetchone()
    conn.close()
    return profile


# Function to update profile
def update_profile(
    name,
    description,
    profile_image,
    introduction,
    about_me_description,
    about_me_closingTag,
    about_me_video,
):
    db_path = os.path.join(current_dir, "DATABASE.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE profiles SET name = ?, description = ?, profile_image = ?, introduction = ?, about_me_description = ?, about_me_closingTag = ?, about_me_video = ? WHERE id = 1",
        (
            name,
            description,
            profile_image,
            introduction,
            about_me_description,
            about_me_closingTag,
            about_me_video,
        ),
    )
    conn.commit()
    conn.close()


# Function to fetch all components from the database
def get_services():
    db_path = os.path.join(current_dir, "DATABASE.db")
    conn = sqlite3.connect(db_path)
    query = "SELECT id, title, description, icon FROM components"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


# Function to update a component
def update_services(df):
    db_path = os.path.join(current_dir, "DATABASE.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # Clear the table first to avoid duplicates
    cursor.execute("DELETE FROM components")

    # Insert updated rows
    for _, row in df.iterrows():
        cursor.execute(
            """
        INSERT INTO components (id, title, description, icon)
        VALUES (?, ?, ?, ?)
        """,
            (row["id"], row["title"], row["description"], row["icon"]),
        )

    conn.commit()
    conn.close()


@st.cache_data()
def get_project_cards():
    return [
        {
            "projectId": 1,
            "projectTitle": "Ultimate Personal Budgeting",
            "images": [
                "static/images/1.png",
                "static/images/2.png",
                "static/images/3.png",
            ],
            "projectDescription": "This is the description for Project One.",
            "publishDate": "2023-12-10",
            "updateDate": "2023-12-12",
            "tags": ["Finance", "Budgeting", "Personal"],
        },
        {
            "projectId": 2,
            "projectTitle": "Project Two",
            "images": [
                "static/images/1.png",
                "static/images/2.png",
                "static/images/3.png",
            ],
            "projectDescription": "This is the description for Project Two.",
            "publishDate": "2023-11-20",
            "updateDate": "2023-11-25",
            "tags": ["Design", "UI/UX", "Creative"],
        },
        {
            "projectId": 3,
            "projectTitle": "Project Three",
            "images": [
                "static/images/1.png",
                "static/images/2.png",
                "static/images/3.png",
            ],
            "projectDescription": "This is the description for Project Three.",
            "publishDate": "2023-10-05",
            "updateDate": "2023-10-10",
            "tags": ["Development", "Web", "Technology"],
        },
        {
            "projectId": 4,
            "projectTitle": "Project Four",
            "images": [
                "static/images/6.svg",
                "static/images/7.svg",
            ],
            "projectDescription": "This is the description for Project Four.",
            "publishDate": "2023-10-05",
            "updateDate": "2023-10-10",
            "tags": ["Graphics", "Illustration", "Creative"],
        },
        {
            "projectId": 5,
            "projectTitle": "Project Five",
            "images": [
                "static/images/1.png",
                "static/images/2.png",
                "static/images/3.png",
            ],
            "projectDescription": "This is the description for Project Five.",
            "publishDate": "2023-10-05",
            "updateDate": "2023-10-10",
            "tags": ["Education", "E-Learning", "Platform"],
        },
        {
            "projectId": 6,
            "projectTitle": "Project Six",
            "images": [
                "static/images/1.png",
                "static/images/2.png",
                "static/images/3.png",
            ],
            "projectDescription": "This is the description for Project Six.",
            "publishDate": "2023-10-05",
            "updateDate": "2023-10-10",
            "tags": ["Data", "Analytics", "Machine Learning"],
        },
    ]
