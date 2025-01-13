from datetime import datetime

import streamlit as st

NAME = "John Doe"
DESCRIPTION = "Senior Data Analyst, assisting enterprises by supporting data-driven decision-making."


def display_section(title, items, icon=":material/check_circle:", color=":primary"):
    st.subheader(title, divider="gray")
    formatted_items = "\n\n".join([f"{color}[{icon}] {item}" for item in items])
    st.markdown(formatted_items)


def display_list(items, icon=":material/check:", color=":primary"):
    space = 3 * "&nbsp;"
    formatted_items = "\n\n".join([f"{space}{color}[{icon}] {item}" for item in items])
    st.markdown(formatted_items)


# TODO: Fix the vertical space
def vertical_space(number: int):
    lines = number * "\n"
    st.write(lines)


@st.dialog(title=f"{NAME} Resume", width="large")
def my_cv():
    _, col2, _ = st.columns(
        [1, 10, 1],
        gap="small",
    )
    with col2:
        st.markdown(
            f"""
                    <h1 style="text-align: center;">{NAME}</h1>
                    <p style="text-align: center;">{DESCRIPTION}</p>
                    """,
            unsafe_allow_html=True,
        )

    # ----------------------------------------
    #    EXPERIENCE & QUALIFICATIONS
    # ----------------------------------------
    vertical_space(30)
    experience = [
        "7 Years expereince extracting actionable insights from data",
        "Strong hands on experience and knowledge in Python and Excel",
        "Good understanding of statistical principles and their respective applications",
        "Excellent team-player and displaying strong sense of initiative on tasks",
    ]

    # ----------------------------------------
    #        SKILLS
    # ----------------------------------------
    Hard_Skills = [
        "**Programming:** Python (Scikit-learn, Pandas), SQL, VBA",
        "**Data Visualization:** PowerBi, MS Excel, Plotly",
        "**Modeling:** Logistic regression, linear regression, decision trees",
        "**Databases:** Postgres, MongoDB, MySQL",
    ]
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        display_section("Experience & Qulifications", experience)
        st.write("\n")
    with col2:
        display_section("Hard Skills", Hard_Skills)

    # ----------------------------------------
    #        WORK HISTORY
    # ----------------------------------------
    vertical_space(3)
    st.subheader("Work History", divider="gray")
    #  JOB 1
    st.write(
        ":primary[:material/bar_chart:]", "**Senior Data Analyst | Ross Industries**"
    )
    st.write("02/2020 - Present")
    work_hist_1 = [
        "Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%",
        "Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads",
        "Redesigned data model through iterations that improved predictions by 12%",
    ]
    display_list(work_hist_1)

    #  JOB 2
    vertical_space(3)
    st.write(
        ":primary[:material/bar_chart:]", "**Data Analyst | Liberty Mutual Insurance**"
    )
    st.write("01/2018 - 02/2022")
    work_hist_2 = [
        "Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%",
        "Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K",
        "Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing",
    ]
    display_list(work_hist_2)

    #  JOB 3
    st.write("\n")
    st.write("\n")
    st.write(":primary[:material/bar_chart:]", "**Data Analyst | Chegg**")
    st.write("04/2015 - 01/2018")
    work_hist_3 = [
        "Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc",
        "Analyzed, documented, and reported user survey results to improve customer communication processes by 18%",
        "Collaborated with analyst team to oversee end-to-end process surrounding customers' return data",
    ]
    display_list(work_hist_3)

    # ----------------------------------------
    #        PROJECTS & ACCOMPLISHMENTS
    # ----------------------------------------
    vertical_space(3)
    st.subheader("Projects & Accomplishments", divider="gray")
    st.write("Projects Here")

    # ----------------------------------------
    #        CERTIFICATIONS & AWARDS
    # ----------------------------------------
    vertical_space(3)
    certifications = [
        "Certified Data Scientist (Google)",
        "AWS Cloud Practitioner",
        "UX Design Bootcamp Certification",
    ]

    awards = [
        "Innovator Award 2023",
        "Best Data Visualization, XYZ Hackathon",
        "Client Excellence Award",
    ]
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        display_section("Certifications", certifications)

    with col2:
        display_section("Honours & Awards Received", awards)

    # ----------------------------------------
    #        FOOTER
    # ----------------------------------------
    st.divider()
    nameextract = st.secrets["credentials"]["usernames"]
    for username, details in nameextract.items():
        full_name = details["name"]
    now = datetime.now()
    current_year = now.year
    st.markdown(
        f"""
        <div style="text-align: center;">
            <p>Copyright &copy; {current_year} - {full_name}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
