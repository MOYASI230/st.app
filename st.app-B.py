import streamlit as st
import time

# セッションステートの初期化
if 'IQpoint' not in st.session_state:
    st.session_state.IQpoint = 0
if 'question_no' not in st.session_state:
    st.session_state.question_no = 0
if 'state' not in st.session_state:
    st.session_state.state = 'start'  # 'start': スタート待機, 'question': 問題表示, 'answer': 回答待機

# 問題データ
question_images = ["1.png", "2.png"]
question_answers1 = ["バナナ", "ぶどう","桃"]
total_questions = len(question_answers1)
question_answers2 = ["数学", "家庭科","図工"]
total_questions = len(question_answers2)

def show_start():
    """スタート待機状態：スタートボタンを表示し、押下で問題表示に移行"""
    if st.button("スタート!"):
        st.session_state.state = 'question'
        st.rerun()

def show_question():
    """問題表示状態：問題文と画像を表示し、指定秒数後に画像を消去し回答待機へ移行"""
    q_no = st.session_state.question_no
    st.write(f"問題{q_no}: 次の画像は何の食べ物かを覚えなさい")
    image_container = st.empty()
    image_container.image(
        question_images[q_no],
        caption=f"問題{q_no}の画像",
        use_column_width=True
    )
    # 指定秒数（ここでは1秒）待機してから画像を消去
    time.sleep(1)
    image_container.empty()
    # 状態を回答待機に変更
    st.session_state.state = 'answer'
    st.rerun()

def show_question2():
    """問題表示状態：問題文と画像を表示し、指定秒数後に画像を消去し回答待機へ移行"""
    q_no = st.session_state.question_no
    st.write(f"問題{q_no}: 次の画像は何の食べ物かを覚えなさい")
    image_container = st.empty()
    image_container.image(
        question_images[q_no],
        caption=f"問題{q_no}の画像",
        use_column_width=True
    )
    # 指定秒数（ここでは1秒）待機してから画像を消去
    time.sleep(1)
    image_container.empty()
    # 状態を回答待機に変更
    st.session_state.state = 'answer2'
    st.rerun()

def show_answer():
    """回答待機状態：選択肢と決定ボタンを表示し、正誤判定後、次の問題へ"""
    q_no = st.session_state.question_no
    # キーを指定してラジオボタンの状態を固有化
    choice = st.radio("選んでください:", question_answers1, index=0, key=f"radio_{q_no}")
    if st.button("決定"):
        if choice == question_answers1[q_no]:
            st.write("正解!!")
            st.session_state.IQpoint += 1
        else:
            st.write("残念!!!")
        st.session_state.question_no += 1
        # 次の問題がある場合は再びスタート待機状態に戻る
        st.session_state.state = 'question2'
        st.rerun()

def show_answer2():
    """回答待機状態：選択肢と決定ボタンを表示し、正誤判定後、次の問題へ"""
    q_no = st.session_state.question_no
    # キーを指定してラジオボタンの状態を固有化
    choice = st.radio("選んでください:", question_answers2, index=0, key=f"radio_{q_no}")
    if st.button("決定"):
        if choice == question_answers2[q_no]:
            st.write("正解!!")
            st.session_state.IQpoint += 1
        else:
            st.write("残念!!!")
        st.session_state.question_no += 1
        # 次の問題がある場合は再びスタート待機状態に戻る
        st.session_state.state = 'start'
        st.rerun()

# メイン処理
if st.session_state.question_no < total_questions:
    if st.session_state.state == 'start':
        show_start()
    elif st.session_state.state == 'question':
        show_question()
    elif st.session_state.state == 'answer':
        show_answer()
    elif st.session_state.state == 'question2':
        show_question2
    elif st.session_state.state == 'answer2':
        show_answer2()
else:
    st.write("全ての問題が終了しました!")
    st.write(f"最終得点: {st.session_state.IQpoint}")