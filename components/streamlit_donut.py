from typing import Literal, Optional

import numpy as np
import streamlit as st


# Inspired by: https://codepen.io/benjaminlry/pen/xQydro?anon=true&view=pen
def st_donut(
    label: str,
    value: float,
    outOf: float = 100,
    units: str = "",
    delta: Optional[str] = None,
    space: int = 30,
    size: int = 180,
    direction: Literal["clockwise", "anticlockwise"] = "clockwise",
    text_size: int = 50,
    delta_text_size: int = 18,
    value_text_color: Optional[str] = None,
    arc_bg_color: Optional[str] = None,
    background_stroke_width: int = 19,
    arc_stroke_width: Optional[int] = None,
    rounded: bool = True,
    label_visibility: bool = True,
    hide_background: bool = False,
):
    primary_color = st.get_option("theme.primaryColor") or "#FF4B4B"
    if value_text_color is None:
        base_theme = st.get_option("theme.base")
        base_theme = str(base_theme)
        if base_theme == "dark":
            value_text_color = "#FFFFFF"
        else:
            value_text_color = "#4a4c5a"

    if arc_stroke_width is None:
        arc_stroke_width = background_stroke_width

    # Circle % of the parent size
    circle_size = 0.98 * size
    radius = (circle_size - max(background_stroke_width, arc_stroke_width)) / 2
    circumference = 2 * np.pi * radius

    # Stroke-dashoffset for value (fraction of value/outOf)
    value_fraction = value / outOf
    value_length = value_fraction * circumference

    # Arc color defaults to primary color
    if not arc_bg_color:
        arc_bg_color = primary_color

    delta_color = None
    if delta is not None:
        delta = str(delta)
        if delta.startswith("-"):
            delta_color = "red"
            delta = f"↓ {delta[1:]}" # down arrow(unicode chr)&remove -ve sign
        elif delta.startswith("0"):
            # elif delta == "0":
            delta_color = "blue"
        else:
            delta_color = "green"
            delta = f"↑ {delta}"  # up arrow(unicode chr)

    dash_offset = circumference - value_length
    linecap = "round" if rounded else "butt"
    background_color = "transparent" if hide_background else "#ddd"

    if direction == "clockwise":  # STARTS FROM TOP AND GOES CLOCKWISE
        if arc_stroke_width < background_stroke_width:
            arc_stroke_width = background_stroke_width

        svg = f"""
        <svg width="{size}px" height="{size}px" viewBox="0 0 {circle_size} {circle_size}" xmlns="http://www.w3.org/2000/svg">
            <!-- Background Circle -->
            <circle cx="{circle_size/2}" cy="{circle_size/2}" r="{radius}" stroke="{background_color}" stroke-width="{background_stroke_width}" fill="transparent"/>
            <!-- Progress Circle -->
            <circle cx="{circle_size/2}" cy="{circle_size/2}" r="{radius}" stroke="{arc_bg_color}" stroke-width="{arc_stroke_width}" fill="transparent" 
                stroke-dasharray="{circumference}" stroke-dashoffset="{dash_offset}" stroke-linecap="{linecap}" transform="rotate(-90, {circle_size/2}, {circle_size/2})"/>
            <!-- Center Text -->
            <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="{text_size}" fill="{value_text_color}">{value}{units}<tspan x="50%" dy="{space}" font-size="{delta_text_size}" fill="{delta_color}">{delta}</tspan></text>
        </svg>
        """
    else:  # STARTS FROM TOP AND GOES ANTICLOCKWISE
        # ---------------------------------------------------------------------
        # TODO: Fix this Version 1 - DIFFERENT LOGIC - using the background as the active arc
        # --------------------------------------------------------------------

        # dash_offset = value_length
        # linecap = "butt"
        # arc_stroke_width = background_stroke_width
        # if arc_stroke_width > background_stroke_width:
        #     arc_stroke_width = background_stroke_width
        # if arc_stroke_width < background_stroke_width:
        #     arc_stroke_width = background_stroke_width

        # svg = f"""
        # <svg width="{size}px" height="{size}px" viewBox="0 0 {circle_size} {circle_size} "xmlns="http://www.w3.org/2000/svg">
        #     <!-- Background Circle -->
        #     <circle cx="{circle_size/2}" cy="{circle_size/2}" r="{radius}" stroke="{arc_bg_color}" stroke-width="{background_stroke_width}" fill="transparent"
        #         stroke-dasharray="{circumference}" stroke-dashoffset="0"/>
        #     <!-- Progress Circle -->
        #     <circle cx="{circle_size/2}" cy="{circle_size/2}" r="{radius}" stroke="{background_color}" stroke-width="{arc_stroke_width}" fill="transparent"
        #         stroke-dasharray="{circumference}" stroke-dashoffset="{dash_offset}" stroke-linecap="{linecap}" transform="rotate(-90, {circle_size/2}, {circle_size/2})"/>
        #     <!-- Center Text -->
        #     <text x="50%" y="45%" dominant-baseline="middle" text-anchor="middle" font-size="{text_size}" fill="{value_text_color}">{value}{units}<tspan x="50%" dy="{space}" font-size="{delta_text_size}" fill="{delta_color}">{delta}</tspan></text>
        # </svg>
        # """

        # ----------------------------------------------------------------------
        #       VERSION 2 - Introduces -ve sign to the stroke-dashoffset
        # ----------------------------------------------------------------------

        if arc_stroke_width < background_stroke_width:
            arc_stroke_width = background_stroke_width

        svg = f"""
        <svg width="{size}px" height="{size}px" viewBox="0 0 {circle_size} {circle_size}" xmlns="http://www.w3.org/2000/svg">
            <!-- Background Circle -->
            <circle cx="{circle_size/2}" cy="{circle_size/2}" r="{radius}" stroke="{background_color}" stroke-width="{background_stroke_width}" fill="transparent"/>
            <!-- Progress Circle -->
            <circle cx="{circle_size/2}" cy="{circle_size/2}" r="{radius}" stroke="{arc_bg_color}" stroke-width="{arc_stroke_width}" fill="transparent" 
                stroke-dasharray="{circumference}" stroke-dashoffset="-{dash_offset}" stroke-linecap="{linecap}" transform="rotate(-90, {circle_size/2}, {circle_size/2})"/>
            <!-- Center Text -->
            <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="{text_size}" fill="{value_text_color}">{value}{units}<tspan x="50%" dy="{space}" font-size="{delta_text_size}" fill="{delta_color}">{delta}</tspan></text>
        </svg>
        """
    if label and label_visibility:
        st.markdown(f"{label}")
    st.markdown(
        f'<div style="margin-bottom: 20px;">{svg}</div>',
        unsafe_allow_html=True,
    )
