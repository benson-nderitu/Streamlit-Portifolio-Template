import streamlit as st
import streamlit_antd_components as sac

# Define the dictionary with button details
buttons_dict = {
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

# Create a list of ButtonsItem objects from the dictionary
buttons_list = [
    sac.ButtonsItem(icon=details["icon"], color=details["color"], href=details["href"])
    for details in buttons_dict.values()
]

# Render the buttons
sac.buttons(
    buttons_list,
    index=None,
    use_container_width=True,
    align="center",
    variant="filled",
)

# ...existing code...
