import streamlit as st
import random

# セッションステートでスコア管理
if "score" not in st.session_state:
    st.session_state.score = {"勝ち": 0, "負け": 0, "引き分け": 0}
    st.session_state.player_name = "プレイヤー"

# プレイヤー名の設定
st.title("じゃんけんゲーム")
player_name = st.text_input("名前を入力してください", st.session_state.player_name)
st.session_state.player_name = player_name

# じゃんけんの選択肢
choices = ["グー", "チョキ", "パー"]
player_choice = st.radio("手を選んでください", choices)

if st.button("対戦！"):
    cpu_choice = random.choice(choices)
    result = ""
    
    # 勝敗判定
    if player_choice == cpu_choice:
        result = "引き分け"
    elif (player_choice == "グー" and cpu_choice == "チョキ") or (player_choice == "チョキ" and cpu_choice == "パー") or (player_choice == "パー" and cpu_choice == "グー"):
        result = "勝ち"
    else:
        result = "負け"
    
    # スコア更新
    st.session_state.score[result] += 1
    
    # 結果表示
    st.write(f"{player_name}の手: {player_choice}")
    st.write(f"CPUの手: {cpu_choice}")
    st.success(f"結果: {result}！")

# スコア表示
st.subheader("スコア")
st.write(f"勝ち: {st.session_state.score['勝ち']}  負け: {st.session_state.score['負け']}  引き分け: {st.session_state.score['引き分け']}")

# リセットボタン
if st.button("リセット"):
    st.session_state.score = {"勝ち": 0, "負け": 0, "引き分け": 0}
    st.session_state.player_name = "プレイヤー"
    st.experimental_rerun()