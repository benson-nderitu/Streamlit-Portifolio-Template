import streamlit as st


# ================================================================
#   CONTACT PAGE
# ================================================================
def contact():
    primary_color = st.get_option("theme.primaryColor")
    with st.container(key="ContactContainer"):
        cnt_info, cnt_form = st.columns(2, gap="large")
        with cnt_info:
            with st.container(key="contactInfoContainer"):
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
                st.markdown(":primary[:material/call:] +2547 *** ***")
                st.markdown(
                    ":primary[:material/location_pin:] 121 Kenyatta Avenue, Nairobi"
                )
                st.markdown(":primary[:material/email:] youmail@gmail.com")

                st.markdown(":primary[:material/globe_uk:] www.yourWebside.com")

        with cnt_form:
            with st.container(key="contactFormContainer"):
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
