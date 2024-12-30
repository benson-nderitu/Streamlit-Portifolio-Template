import streamlit as st


# ================================================================
#   CONTACT PAGE
# ================================================================
def contact():
    primary_color = st.get_option("theme.primaryColor")
    # with st.container(key="ContactMeHeaderContainer"):
    st.markdown(
            f"""
            <h1 style="font-size:2.5em; padding-left:50px; line-height:0;">Contact <span style="color: {primary_color}; ">ME</span></h1>
            <hr style = "width:16%; margin-left:35px;">
            """,
            unsafe_allow_html=True,
        )
    # st.divider()
    with st.container(key="ContactContainer"):
        cntinfo, cntform = st.columns(2, gap="large")
        with cntinfo:
            with st.container(key="contactinfoContainer"):
                st.markdown(
                    f"""
                    <h3 style="color: {primary_color}; text-align: center;">Contact Info</span></h3>
                    """,
                    unsafe_allow_html=True,
                )
                st.write(
                    "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
                )
                st.divider()
                st.write("+262 695 2601")
                st.write("121 King Street, Australia")
                st.write("youmail@gmail.com")
                st.write("www.yourWebside.com")

        with cntform:
            with st.container(key="contactformContainer"):
                with st.form(key="contactMeForm", clear_on_submit=True, border=False):
                    objective = st.text_input(
                        label="Name",
                        key="jkl",
                        placeholder="Your Name",
                    )
                    email = st.text_input(label="Your Name")

                    message_placeholder = st.empty()
                    submitted = st.form_submit_button(
                        "Send Message",
                        help="Send Me Your Message",
                        type="primary",
                        icon=":material/forward_to_inbox:",
                        use_container_width=True,
                    )
                    if submitted:
                        if not (
                            objective
                            and email
                            # and selected_workplace
                        ):
                            message_placeholder.warning(
                                "Ensure all mandatory fields are filled."
                            )
                            st.stop()
                        else:
                            with st.spinner("Submitting your details"):
                                st.write("Collecting and submitting data")
