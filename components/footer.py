from datetime import datetime

import streamlit as st
import streamlit_antd_components as sac

from data.allData import get_social_links


# ----------------------------------------------------------------
#    FOOTER
# ----------------------------------------------------------------
@st.fragment
def Footer():
    with st.container(
        key="FooterContainer",
    ):
        st.markdown(f"""<hr style = "padding-bottom:1px">""", unsafe_allow_html=True)
        _, centre_col, _ = st.columns(
            [
                1,
                2,
                1,
            ],
            gap="large",
        )
        with centre_col:
            with st.container(key="FooterTitle"):
                name_extract = st.secrets["credentials"]["usernames"]
                for username, details in name_extract.items():
                    full_name = details["name"]
                    st.markdown(
                        f"""
                        <h2 style="text-align:center;">{full_name}</h2>
                        """,
                        unsafe_allow_html=True,
                    )

            socialLinks = get_social_links()
            footer_socialLinks = socialLinks.to_dict(orient="records")
            buttons_list = [
                sac.ButtonsItem(
                    icon=id["icon"],
                    color=id["color"],
                    href=id["href"],
                )
                for id in footer_socialLinks
            ]
            sac.buttons(
                buttons_list,
                index=None,
                use_container_width=False,
                align="center",
                variant="outline",
            )

            st.divider()
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
        st.markdown(f"""<hr>""", unsafe_allow_html=True)
