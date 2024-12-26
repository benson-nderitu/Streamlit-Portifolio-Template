import os
import sqlite3

import pandas as pd
import streamlit as st

# =================================================================
#                  Get the path to the database
# =================================================================
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "DATABASE.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


# ===============================================================s=
#        PROFILE DATA
# ================================================================
def get_profile():
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


# ================================================================
#   SERVICES
# ================================================================
def get_services():
    # db_path = os.path.join(current_dir, "DATABASE.db")
    # conn = sqlite3.connect(db_path)
    query = "SELECT id, title, description, icon FROM services"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


# Function to update a service table
def update_services(df):
    # Clear the table first to avoid duplicates
    cursor.execute("DELETE FROM services")
    # Insert updated rows
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO services (id, title, description, icon) VALUES (?, ?, ?, ?)",
            (row["id"], row["title"], row["description"], row["icon"]),
        )

    conn.commit()
    conn.close()


# ================================================================
#      SKILLS  DESCRIPTION SECTION
# ================================================================
def get_skillDescription():
    cursor.execute(
        "SELECT title, header, body, closingtag FROM skillsDescription WHERE id = 1"
    )
    skillDescription = cursor.fetchone()
    conn.close()
    return skillDescription


# Function to update skillDescription
def update_skillDescription(title, header, body, closingtag):
    cursor.execute(
        "UPDATE skillsDescription SET title = ?, header = ?, body = ?, closingtag = ? WHERE id = 1",
        (title, header, body, closingtag),
    )
    conn.commit()
    conn.close()


# ================================================================
#   SKILLS
# ================================================================
def get_skills():
    # db_path = os.path.join(current_dir, "DATABASE.db")
    # conn = sqlite3.connect(db_path)
    query = "SELECT id, name, percentage FROM skills"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


# Function to update table
def update_skills(df):
    # Clear the table first to avoid duplicates
    cursor.execute("DELETE FROM skills")

    # Insert updated rows
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO skills (id, name, percentage) VALUES (?, ?, ?)",
            (row["id"], row["name"], row["percentage"]),
        )

    conn.commit()
    conn.close()


# ==============================================================================
#     GET PROJECT CARDS
# ==============================================================================
def get_social_links():
    cursor.execute("SELECT * FROM social_links")
    rows = cursor.fetchall()

    social_links = []
    for row in rows:
        social_links.append(
            {"id": row[0], "icon": row[1], "color": row[2], "href": row[3]}
        )

    conn.close()
    return social_links


def update_social_link(link_id, icon=None, color=None, href=None):
    if icon:
        cursor.execute("UPDATE social_links SET icon = ? WHERE id = ?", (icon, link_id))
    if color:
        cursor.execute(
            "UPDATE social_links SET color = ? WHERE id = ?", (color, link_id)
        )
    if href:
        cursor.execute("UPDATE social_links SET href = ? WHERE id = ?", (href, link_id))

    conn.commit()
    conn.close()


# ==============================================================================
#     GET PROJECT CARDS
# ==============================================================================


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
