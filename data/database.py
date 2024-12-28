import os
import sqlite3
import threading
from datetime import datetime


# -----------------------------------------------------------
#     create SQLite database and insert sample data
# -----------------------------------------------------------
def create_database():
    if not os.path.exists("data"):
        os.makedirs("data")

    db_path = os.path.join("data", "DATABASE.db")
    conn = sqlite3.connect(db_path, check_same_thread=False)
    cursor = conn.cursor()

    # -----------------------------------------------------------
    #       Create table to store HTML content if not exists
    # -----------------------------------------------------------
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
    conn.commit()

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

    # --------------------------------------------
    #      PROFILE DATABASE CREATION
    # --------------------------------------------
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
    conn.commit()

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
                "Proin adipiscing porta tellus, ut feugiat nibh adipiscing sit  amet. In eu justo a felis faucibus to decorate or that fear. Vestibulum before him first",
                "https://www.youtube.com/watch?v=7BUoSIVNW_U&t=0s",
            ),
        )
    conn.commit()

    # ----------------------------------------------------------------
    #            SERVICES TABLE
    # ----------------------------------------------------------------
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS services (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        icon TEXT NOT NULL
    )
    """
    )
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM services")
    count = cursor.fetchone()[0]

    if count == 0:
        services_data = [
            {
                "title": "Web Development",
                "description": "Lorem ipsum dolor sit amet.",
                "icon": "laptop",
            },
            {
                "title": "UI / UX Design",
                "description": "Lorem ipsum dolor sit amet.",
                "icon": "pen",
            },
            {
                "title": "App Development",
                "description": "Lorem ipsum dolor sit amet.",
                "icon": "phone",
            },
            {
                "title": "Photography",
                "description": "Lorem ipsum dolor sit amet.",
                "icon": "camera",
            },
            {
                "title": "Rebranding",
                "description": "Lorem ipsum dolor sit amet.",
                "icon": "send",
            },
            {
                "title": "SEO Marketing",
                "description": "Lorem ipsum dolor sit amet.",
                "icon": "globe",
            },
        ]

        for service in services_data:
            cursor.execute(
                """
            INSERT INTO services (title, description, icon) VALUES (?, ?, ?)
            """,
                (service["title"], service["description"], service["icon"]),
            )

        conn.commit()

    # ----------------------------------------------------------------
    #            SKILLS DESCRIPTION TABLE
    # ----------------------------------------------------------------
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS skillsDescription (
            id INTEGER PRIMARY KEY,
            title TEXT,
            header TEXT,
            body TEXT,
            closingtag TEXT
        )
    """
    )
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM skillsDescription")
    if cursor.fetchone()[0] == 0:
        title = "WHAT YOU NEED TO KNOW"
        header = "Hello!, I'm Benson Nderitu, a data analyst based in Nairobi, Kenya."
        body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        closingtag = "The gateway to advanced learning lies ahead, with a focus on achieving the right balance. Move forward with purpose, enriching your approach step by step. At every beginning, the essentials are key."
        cursor.execute(
            """
            INSERT INTO skillsDescription (title, header, body, closingtag) 
            VALUES (?, ?, ?, ?)
        """,
            (title, header, body, closingtag),
        )
        conn.commit()

    # ----------------------------------------------------------------
    #           SKILLS TABLE
    # ----------------------------------------------------------------
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        percentage INTEGER NOT NULL
    )
    """
    )
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM skills")
    count = cursor.fetchone()[0]

    if count == 0:
        skills = [
            {"name": "WordPress", "percentage": 95},
            {"name": "HTML & CSS3", "percentage": 70},
            {"name": "Photoshop", "percentage": 80},
            {"name": "Illustrator", "percentage": 90},
        ]

        for skill in skills:
            cursor.execute(
                """
            INSERT INTO skills (name, percentage) VALUES (?, ?)
            """,
                (skill["name"], skill["percentage"]),
            )

        conn.commit()

    # ----------------------------------------------------------------
    #            EXPERIENCE TABLE
    # ----------------------------------------------------------------
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS experience (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        year TEXT NOT NULL,
        title TEXT NOT NULL,
        role TEXT NOT NULL,
        description TEXT NOT NULL
    )
    """
    )
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM experience")
    count = cursor.fetchone()[0]

    if count == 0:
        timeline_entries = [
            {
                "year": "2015",
                "title": "Envato Studio",
                "role": "Lead Web Designer",
                "description": (
                    "This was the time when we started our company. We had no idea how far we would go, "
                    "we weren’t even sure that we would be able to survive for a few years. What drove us to "
                    "start the company was the understanding that we could provide a service no one else was providing."
                ),
            },
            {
                "year": "2016 - 2018",
                "title": "Envato Studio",
                "role": "Lead Web Designer",
                "description": "This was the time when we started our company. We had no idea how far we would go, we weren’t even sure that we would be able to survive for a few years. What drove us to start the company was the understanding that we could provide a service no one else was providing.",
            },
            {
                "year": "2018 - 2020",
                "title": "Envato Studio",
                "role": "Senior Web Developer",
                "description": "During this time, we expanded our services and built a reputation in the market. Our focus was on providing high-quality solutions tailored to the client’s needs.",
            },
            {
                "year": "2020 - 2022",
                "title": "Envato Studio",
                "role": "Lead Web Developer",
                "description": "This was the time when we started our company. We had no idea how far we would go, we weren’t even sure that we would be able to survive for a few years. What drove us to start the company was the understanding that we could provide a service no one else was providing.",
            },
            {
                "year": "2022 - Present",
                "title": "Envato Studio",
                "role": "Lead Web Developer",
                "description": "This was the time when we started our company. We had no idea how far we would go, we weren’t even sure that we would be able to survive for a few years. What drove us to start the company was the understanding that we could provide a service no one else was providing.",
            },
        ]
        for entry in timeline_entries:
            cursor.execute(
                """
            INSERT INTO experience (year, title, role, description) VALUES (?, ?, ?, ?)
            """,
                (entry["year"], entry["title"], entry["role"], entry["description"]),
            )

        conn.commit()

    # ----------------------------------------------------------------
    #            TESTIMONIALS TABLE
    # ----------------------------------------------------------------
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS testimonials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rating REAL NOT NULL,
        text TEXT NOT NULL,
        author TEXT NOT NULL,
        image TEXT NOT NULL
    )
    """
    )
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM testimonials")
    count = cursor.fetchone()[0]

    if count == 0:
        testimonials_data = [
            {
                "rating": 5,
                "text": "I loved the project. It was a great learning experience.",
                "author": "John Doe",
                "image": "static/profile.png",
            },
            {
                "rating": 4.5,
                "text": "Amazing work! Truly exceeded my expectations.",
                "author": "Jane Smith",
                "image": "static/logo.png",
            },
            {
                "rating": 5,
                "text": "Fantastic job! Highly recommend.",
                "author": "Alex Johnson",
                "image": "static/profile.png",
            },
        ]

        for testimonial in testimonials_data:
            cursor.execute(
                """
            INSERT INTO testimonials (rating, text, author, image) VALUES (?, ?, ?, ?)
            """,
                (
                    testimonial["rating"],
                    testimonial["text"],
                    testimonial["author"],
                    testimonial["image"],
                ),
            )

        conn.commit()

    # ----------------------------------------------------------------
    #            SOCIAL LINKS TABLE
    # ----------------------------------------------------------------
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS social_links (
        id INTEGER PRIMARY KEY,
        icon TEXT NOT NULL,
        color TEXT NOT NULL,
        href TEXT NOT NULL
    )
    """
    )
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM social_links")
    count = cursor.fetchone()[0]

    SocialLinks_dict = {
        "linkedin": {
            "icon": "linkedin",
            "color": "#0077B5",
            "href": "https://www.linkedin.com/in/benson-nderitu-88776215b",
        },
        "youtube": {
            "icon": "youtube",
            "color": "#FF0000",
            "href": "https://youtube.com/@scho_da?si=wr1UcYXz7gcHFAeY",
        },
        "github": {
            "icon": "github",
            "color": "#181717",
            "href": "https://github.com/benson-nderitu",
        },
        "twitter": {
            "icon": "twitter",
            "color": "#1DA1F2",
            "href": "https://twitter.com/BensonN41451654",
        },
    }

    if count == 0:
        for button in SocialLinks_dict.values():
            cursor.execute(
                """
            INSERT INTO social_links (icon, color, href)
            VALUES (?, ?, ?)
            """,
                (button["icon"], button["color"], button["href"]),
            )

        conn.commit()

    conn.close()


# create_database()
