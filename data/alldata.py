import os
import sqlite3

import pandas as pd
import streamlit as st

# =================================================================
#                  Get the path to the database
# =================================================================
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "DATABASE.db")


# ================================================================
#        PROFILE DATA
# ================================================================
@st.cache_data()
def get_profile():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT name, description, profile_image, introduction, 
                   about_me_description, about_me_closingTag, about_me_video 
            FROM profiles WHERE id = 1
            """
        )
        profile = cursor.fetchone()
    return profile


def update_profile(
    name,
    description,
    profile_image,
    introduction,
    about_me_description,
    about_me_closingTag,
    about_me_video,
):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE profiles 
            SET name = ?, description = ?, profile_image = ?, introduction = ?, 
                about_me_description = ?, about_me_closingTag = ?, about_me_video = ? 
            WHERE id = 1
            """,
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


# ================================================================
#   SERVICES
# ================================================================
@st.cache_data()
def get_services():
    with sqlite3.connect(db_path) as conn:
        query = "SELECT id, title, description, icon FROM services"
        df = pd.read_sql_query(query, conn)
    return df


def update_services(df):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM services")
        for _, row in df.iterrows():
            cursor.execute(
                """
                INSERT INTO services (id, title, description, icon) 
                VALUES (?, ?, ?, ?)
                """,
                (row["id"], row["title"], row["description"], row["icon"]),
            )
        conn.commit()


# ================================================================
#      SKILLS  DESCRIPTION SECTION
# ================================================================
@st.cache_data()
def get_skillDescription():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT title, header, body, closingtag 
            FROM skillsDescription WHERE id = 1
            """
        )
        skillDescription = cursor.fetchone()
    return skillDescription


def update_skillDescription(title, header, body, closingtag):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE skillsDescription 
            SET title = ?, header = ?, body = ?, closingtag = ? 
            WHERE id = 1
            """,
            (title, header, body, closingtag),
        )
        conn.commit()


# ================================================================
#   SKILLS
# ================================================================
@st.cache_data()
def get_skills():
    with sqlite3.connect(db_path) as conn:
        query = "SELECT id, name, percentage FROM skills"
        df = pd.read_sql_query(query, conn)
    return df


def update_skills(df):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM skills")
        for _, row in df.iterrows():
            cursor.execute(
                """
                INSERT INTO skills (id, name, percentage) 
                VALUES (?, ?, ?)
                """,
                (row["id"], row["name"], row["percentage"]),
            )
        conn.commit()


# ================================================================
#   EXPERIENCE
# ================================================================
@st.cache_data()
def get_experiences():
    with sqlite3.connect(db_path) as conn:
        query = "SELECT id, year, title, role, description FROM experience"
        df = pd.read_sql_query(query, conn)
    return df


def update_experiences(df):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM experience")
        for _, row in df.iterrows():
            cursor.execute(
                """
                INSERT INTO experience (id, year, title, role, description) 
                VALUES (?, ?, ?, ?, ?)
                """,
                (row["id"], row["year"], row["title"], row["role"], row["description"]),
            )
        conn.commit()


# ================================================================
#   TESTIMONIALS
# ================================================================
@st.cache_data()
def get_testimonials():
    with sqlite3.connect(db_path) as conn:
        query = "SELECT id, rating, text, author, image FROM testimonials"
        df = pd.read_sql_query(query, conn)
    return df


def update_testimonials(df):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM testimonials")
        for _, row in df.iterrows():
            cursor.execute(
                """
                INSERT INTO testimonials (id, rating, text, author, image) 
                VALUES (?, ?, ?, ?, ?)
                """,
                (row["id"], row["rating"], row["text"], row["author"], row["image"]),
            )
        conn.commit()


# =================================================================
#     SOCIAL LINKS
# =================================================================
@st.cache_data()
def get_social_links():
    with sqlite3.connect(db_path) as conn:
        query = "SELECT id, icon, color, href FROM social_links"
        df = pd.read_sql_query(query, conn)
    return df


def update_social_link(df):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM social_links")
        for _, row in df.iterrows():
            cursor.execute(
                """
                INSERT INTO social_links (id, icon, color, href) 
                VALUES (?, ?, ?, ?)
                """,
                (row["id"], row["icon"], row["color"], row["href"]),
            )
        conn.commit()


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
