import streamlit as st


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
