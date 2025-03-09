import streamlit as st
import time

# 初回実行時に session_state を初期化
if "startshow" not in st.session_state:
    st.session_state.startshow = True  # スタートボタンを表示する状態

if "starttxtshow" not in st.session_state:
    st.session_state.starttxtshow = False  # 問題1が表示されていない状態

if "mondaibuttonshow" not in st.session_state:
    st.session_state.mondaibuttonshow = False

if "IQpoint1" not in st.session_state:
    st.session_state.IQpoint1 = 0


# スタートボタンを押したら "starttxtshow" を True にする
if st.session_state.startshow:
    if st.button("スタート!"):
        st.session_state.startshow = False  # スタートボタンを消す
        st.session_state.starttxtshow = True  # 問題1を表示する

        image_placeholder = st.empty()
        image_placeholder.image("1.png", caption="問題1の画像", use_column_width=True)

        time.sleep(1)
        image_placeholder.empty()

        st.session_state.mondaibuttonshow = True
        #print("c")
        if st.session_state.mondaibuttonshow:
            if st.button("バナナ"):
                st.session_state.IQpoint += 1
                st.session_state.mondaibuttonshow = False
            if st.button("桃"):
                st.session_state.IQpoint += 0
                st.session_state.mondaibuttonshow = False
            if st.button("ぶどう"):
                st.session_state.IQpoint += 0
                st.session_state.mondaibuttonshow = False

        # "問題1" を表示して3秒後に消す
        placeholder = st.empty()
        if st.session_state.starttxtshow:
            placeholder.write("問題1")
    
            time.sleep(3)  # 3秒待つ
    
            # 非表示にして状態をリセット
            st.session_state.starttxtshow = False
            st.rerun
        