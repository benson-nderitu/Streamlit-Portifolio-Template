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
        query = "SELECT id, label, icon, color, href FROM social_links"
        df = pd.read_sql_query(query, conn)
    return df


def update_social_link(df):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM social_links")
        for _, row in df.iterrows():
            cursor.execute(
                """
                INSERT INTO social_links (id, label, icon, color, href) 
                VALUES (?, ?, ?, ?, ?)
                """,
                (row["id"], row["label"], row["icon"], row["color"], row["href"]),
            )
        conn.commit()


# ==============================================================================
#     GET PROJECT CARDS
# ==============================================================================
@st.cache_data()
def get_projects():
    with sqlite3.connect(db_path) as conn:
        query = "SELECT projectId, projectTitle, images, projectDescription, publishDate, updateDate, tags, markdownContent FROM projects"
        df = pd.read_sql_query(query, conn)
    return df


def update_projects(
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
