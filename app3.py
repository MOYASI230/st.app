import streamlit as st
import time

if 'IQpoint' not in st.session_state:
    st.session_state.IQpoint = 0  # 初期化

# 問題とボタンを管理するためのプレースホルダー
mondai1holder = st.empty()
startbuttonholder = st.empty()
mondai1textholder = st.empty()
image_placeholder = st.empty()

# スタートボタンが押されたら問題を表示
if startbuttonholder.button("スタート!"):
    startbuttonholder.empty()  # スタートボタンを消す
    mondai1textholder.text("問題1: 次の画像は何の食べ物かを当てなさい")
    image_placeholder.image("1.png", caption="問題1の画像", use_column_width=True)
    time.sleep(1)
    image_placeholder.empty()  # 画像を消す

    # 選択肢を表示（session_stateを使って選択を保持）
    if 'choice' not in st.session_state:
        st.session_state.choice = "バナナ"  # 初期選択肢はバナナ

    choice = st.radio("選んでください:", ["バナナ", "ぶどう", "桃"], index=["バナナ", "ぶどう", "桃"].index(st.session_state.choice))

    # 決定ボタンを表示
    if st.button("決定"):
        st.session_state.choice = choice  # 選択された選択肢をsession_stateに保存
        if choice == "バナナ":
            st.session_state.IQpoint += 1
            st.write("バナナが選ばれました")
        elif choice == "ぶどう":
            st.session_state.IQpoint += 0
            st.write("ぶどうが選ばれました")
        elif choice == "桃":
            st.session_state.IQpoint += 0
            st.write("桃が選ばれました")

        # 最後に現在のIQポイントを表示
        st.write(f"現在のIQポイント: {st.session_state.IQpoint}")
