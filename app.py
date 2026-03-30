import streamlit as st

st.title("🤖 환경 서명 AI 보안 데모")

# 저장 공간 (AI 기억 역할)
if "baseline" not in st.session_state:
    st.session_state.baseline = None

# 입력
st.header("환경 입력")
location = st.selectbox("위치", ["전주", "서울"])
time = st.selectbox("시간", ["낮", "밤"])
device = st.selectbox("기기", ["모바일", "PC"])

# 1️⃣ 학습 버튼
if st.button("🧠 AI 학습하기"):
    st.session_state.baseline = {
        "location": location,
        "time": time,
        "device": device
    }
    st.success("AI가 당신의 환경을 학습했습니다!")

# 2️⃣ 검사 버튼
if st.button("🔍 AI 검사하기"):

    if st.session_state.baseline is None:
        st.warning("먼저 학습을 해주세요!")
    else:
        base = st.session_state.baseline

        score = 0

        if base["location"] != location:
            score += 30
        if base["time"] != time:
            score += 30
        if base["device"] != device:
            score += 40

        st.subheader(f"AI 리스크 점수: {score}")

        if score > 50:
            st.error("⚠️ AI 판단: 이상 행동!")
        else:
            st.success("✅ AI 판단: 정상")
