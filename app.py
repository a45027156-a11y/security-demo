import streamlit as st

st.title("🔐 환경 서명 보안 데모")

st.write("사용자의 환경을 비교하여 이상 여부를 판단합니다")

# 기준 환경
st.header("1️⃣ 기준 환경 설정")
location_base = st.selectbox("위치", ["전주", "서울"])
time_base = st.selectbox("시간", ["낮", "밤"])
device_base = st.selectbox("기기", ["모바일", "PC"])

# 현재 환경
st.header("2️⃣ 현재 환경 입력")
location_now = st.selectbox("현재 위치", ["전주", "서울"])
time_now = st.selectbox("현재 시간", ["낮", "밤"])
device_now = st.selectbox("현재 기기", ["모바일", "PC"])

# 비교 버튼
if st.button("🔍 검사하기"):
    score = 0

    if location_base != location_now:
        score += 30
    if time_base != time_now:
        score += 30
    if device_base != device_now:
        score += 40

    st.subheader(f"리스크 점수: {score}")

    if score > 50:
        st.error("⚠️ 이상 탐지!")
    else:
        st.success("✅ 정상입니다")
