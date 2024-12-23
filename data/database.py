import os
import sqlite3
from datetime import datetime

import streamlit as st


# Function to create SQLite database and insert sample data
def create_database():
    # Ensure the 'data' directory exists
    if not os.path.exists("data"):
        os.makedirs("data")

    # Path to the database in the 'data' directory
    db_path = os.path.join("data", "DATABASE.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table to store HTML content if not exists
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS html_content (
            id INTEGER PRIMARY KEY,
            content TEXT,
            published_date TEXT DEFAULT (DATETIME('now')),
            last_update TEXT DEFAULT (DATETIME('now'))
        )
    """
    )

    # Insert sample HTML content if the table is empty
    cursor.execute("SELECT COUNT(*) FROM html_content")
    if cursor.fetchone()[0] == 0:
        html_sample = "<h3>This is an HTML Header</h3><ul><li>List item 1</li><li>List item 2</li></ul>"
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            """
            INSERT INTO html_content (content, published_date, last_update) 
            VALUES (?, ?, ?)
        """,
            (html_sample, current_time, current_time),
        )
        conn.commit()

    # -------PROFILE DATABASE CREATION----------------
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            profile_image TEXT,
            introduction TEXT,
            about_me_description TEXT,
            about_me_closingTag TEXT,
            about_me_video TEXT
        )
    """
    )

    # Insert a default profile if none exists
    cursor.execute("SELECT * FROM profiles WHERE id = 1")
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO profiles (name, description, profile_image, introduction, about_me_description, about_me_closingTag, about_me_video) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                "Hi, my name is John Doe",
                "The Pain Itself Should Be Painful, The Fatigue Will Be Achieved Did I follow the hard worker here? Praisers are blessed with just gentleness, bearing all the words of the great.",
                "static/profile.png",
                "Hello!, I'm Benson Nderitu, a data analyst based in Nairobi, Kenya.",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                "Proin adipiscing porta tellus, ut feugiat nibh adipiscing sit amet. In eu justo a felis faucibus to decorate or that fear. Vestibulum before him first",
                "https://www.youtube.com/watch?v=7BUoSIVNW_U&t=0s",
            ),
        )
    conn.commit()
    conn.close()
