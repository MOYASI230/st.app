import streamlit as st
import time

st.title("memory.quiz.game")

# セッションステートの初期化
if 'answer1' not in st.session_state:
    st.session_state.answer1 = None
if 'answer2' not in st.session_state:
    st.session_state.answer2 = None

start1_button = st.button('第一問')
if start1_button:
    st.write('第一問!')
    image_placeholder = st.empty()
    image_placeholder.image("1.png", caption="指定された画像", use_column_width=True)

    time.sleep(1)
    image_placeholder.empty()

    st.write("以下の選択肢から選んでね")

    if st.button("apple"):
        st.session_state.answer1 = 0
    if st.button("banana"):
        st.session_state.answer1 = 1
    if st.button("grape"):
        st.session_state.answer1 = 0

start2_button = st.button('第二問')
if start2_button:
    st.write('第二問!')
    image_placeholder = st.empty()
    image_placeholder.image("2.png", caption="指定された画像", use_column_width=True)

    time.sleep(1)
    image_placeholder.empty()

    st.write("以下の選択肢から選んでね")

    if st.button("rice"):
        st.session_state.answer2 = 1
    if st.button("gennmai"):
        st.session_state.answer2 = 0
    if st.button("blend"):
        st.session_state.answer2 = 0

# num1とnum2がどちらも設定されていれば結果を表示
if st.session_state.answer1 is not None and st.session_state.answer2 is not None:
    result = st.session_state.answer1 + st.session_state.answer2
    st.write(f"Result: {result}")