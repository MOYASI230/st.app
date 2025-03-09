import streamlit as st

if "startshow" not in st.session_state:
    st.session_state.show = False

if not st.session_state.startshow:
    if st.button("スタート!"):
        st.session_state.started = True

if st.session_state.startshow:
    st.write("問題1")
