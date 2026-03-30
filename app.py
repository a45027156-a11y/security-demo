import streamlit as st
import numpy as np

st.title("🤖 환경 서명 AI (학습형 보안 데모)")

# 저장공간
if "data" not in st.session_state:
    st.session_state.data = []

# 입력값
st.header("📥 환경 입력")

location = st.selectbox("위치", ["전주", "서울"])
time = st.selectbox("시간대", ["아침", "점심", "저녁", "밤"])
device = st.selectbox("기기", ["모바일", "PC"])
day = st.selectbox("요일", ["월", "화", "수", "목", "금", "토", "일"])
action = st.selectbox("행동", ["로그인", "결제", "검색", "메시지"])

# 숫자로 변환 (AI용)
def encode():
    return np.array([
        ["전주","서울"].index(location),
        ["아침","점심","저녁","밤"].index(time),
        ["모바일","PC"].index(device),
        ["월","화","수","목","금","토","일"].index(day),
        ["로그인","결제","검색","메시지"].index(action)
    ])

# 1️⃣ 학습
if st.button("🧠 학습하기"):
    st.session_state.data.append(encode())
    st.success(f"학습 데이터 저장됨! (총 {len(st.session_state.data)}개)")

# 2️⃣ 검사
if st.button("🔍 AI 검사하기"):

    if len(st.session_state.data) < 3:
        st.warning("데이터를 최소 3번 이상 학습해주세요!")
    else:
        data = np.array(st.session_state.data)
        current = encode()

        # 평균 패턴
        mean = np.mean(data, axis=0)

        # 거리 계산 (유사도)
        distance = np.linalg.norm(current - mean)

        # 학습 많을수록 기준 엄격해짐
        threshold = 2.5 - (len(data) * 0.1)
        if threshold < 1:
            threshold = 1

        risk_score = min(int(distance * 40), 100)

        st.subheader(f"📊 리스크 점수: {risk_score}")
        st.write(f"📈 학습량: {len(data)}개")
        st.progress(risk_score / 100)

        if distance > threshold:
            st.error("⚠️ 이상 행동 탐지!")
        else:
            st.success("✅ 정상 행동")

# 초기화
if st.button("🔄 데이터 초기화"):
    st.session_state.data = []
