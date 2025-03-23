import streamlit as st
import time

# 初期化
if 'IQpoint' not in st.session_state:
    st.session_state.IQpoint = 0  

if 'is_started' not in st.session_state:
    st.session_state.is_started = False

if 'tugibutton1' not in st.session_state:
    st.session_state.tugibutton1 = False  # ここを修正

if 'choice' not in st.session_state:
    st.session_state.choice = None  # 最初は選択肢を非表示にする

if 'choice2' not in st.session_state:
    st.session_state.choice2 = None  # 最初は選択肢を非表示にする

# UIのプレースホルダー
mondai1textholder = st.empty()
mondai2textholder = st.empty()
image_placeholder = st.empty()
image2_placeholder = st.empty()
choice_placeholder = st.empty()
choice2_placeholder = st.empty()

# スタートボタン
if not st.session_state.is_started:
    if st.button("スタート!"):  
        st.session_state.is_started = True
        mondai1textholder.text("問題1: 次の画像は何の食べ物かを覚えなさい")
        image_placeholder.image("1.png", caption="問題1の画像", use_column_width=True)
        time.sleep(1)
        image_placeholder.empty()  

# スタート後に選択肢を表示
if st.session_state.is_started:
    choice = choice_placeholder.radio("選んでください:", ["バナナ", "ぶどう", "桃"])

    # 決定ボタン
    if st.button("決定"):
        st.session_state.choice = choice  # 選択された選択肢を保存
        if choice == "バナナ":
            st.session_state.IQpoint += 1
            st.write(f"正解!IQpoint:{st.session_state.IQpoint}")
        else:
            st.write("不正解...IQpoint:0")

# 「次へ」ボタンの処理
if st.session_state.tugibutton1:
    if st.button("次→"):
        st.session_state.tugibutton = True
        mondai1textholder.text("問題2: 次の画像は何の授業に使う物かを覚えなさい")
        image2_placeholder.image("2.png", caption="問題2の画像", use_column_width=True)
        time.sleep(1)
        image2_placeholder.empty()

if st.session_state.tugibutton1:
    choice = choice2_placeholder.radio("選んでください:", ["数学", "家庭科", "図工"])

    if st.button("決定"):
        st.session_state.choice2_placeholder = choice2
        if choice2 == "図工":
            st.session_state.IQpoint += 1
            st.write(f"正解!IQpoint:{st.session_state.IQpoint}")
        else:
            st.write(f"不正解...IQpoint:{st.session_state.IQPoint}")
