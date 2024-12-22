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
    db_path = os.path.join("data", "example.db")

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

    # Close the connection
    conn.close()
