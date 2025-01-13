import streamlit as st

@st.fragment(run_every="5s")
def button():
    # st.balloons()

    if "clicks" not in st.session_state:
        st.session_state.clicks = 0
    K = st.button("", icon=":material/rocket_launch:")
    l = st.session_state
    st.write(K)
    st.write(l)


button()
