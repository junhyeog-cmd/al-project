import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🌎 MBTI 유형별 국가 분포 시각화")

# 샘플 데이터 (MBTI별 국가별 비율 예시)
data = {
    "MBTI": ["INTJ", "INTJ", "INTJ", "INTJ", "INTJ", "INTJ"],
    "Country": ["한국", "미국", "일본", "영국", "독일", "프랑스"],
    "Percentage": [12, 25, 20, 18, 10, 15]
}

df = pd.DataFrame(data)

# 사용자 입력
selected_mbti = st.selectbox("🔍 MBTI 유형을 선택하세요:", df["MBTI"].unique())

# 선택한 MBTI에 해당하는 데이터 필터링
filtered = df[df["MBTI"] == selected_mbti].sort_values(by="Percentage", ascending=False)

# 색상 지정
colors = []
max_country = filtered.iloc[0]["Country"]  # 1등 국가
for c in filtered["Country"]:
    if c == "한국":
        colors.append("dodgerblue")  # 파란색
    elif c == max_country:
        colors.append("gold")        # 1등은 노란색
    else:
        colors.append("lightgray")   # 나머지 회색

# 그래프 생성
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(filtered["Country"], filtered["Percentage"], color=colors)
ax.set_title(f"{selected_mbti} 유형이 많은 나라", fontsize=16)
ax.set_xlabel("국가")
ax.set_ylabel("비율(%)")

# 값 표시
for i, v in enumerate(filtered["Percentage"]):
    ax.text(i, v + 0.5, str(v) + "%", ha='center', fontsize=10)

st.pyplot(fig)
