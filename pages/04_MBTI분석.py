import streamlit as st
import pandas as pd
import plotly.express as px

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

# 색상 설정
colors = []
max_country = filtered.iloc[0]["Country"]  # 1등 국가
for c in filtered["Country"]:
    if c == "한국":
        colors.append("dodgerblue")  # 한국은 파란색
    elif c == max_country:
        colors.append("gold")        # 1등은 노란색
    else:
        colors.append("lightgray")   # 나머지는 회색

# Plotly 그래프
fig = px.bar(
    filtered,
    x="Country",
    y="Percentage",
    title=f"{selected_mbti} 유형이 많은 나라",
    color=filtered["Country"],  # 색상 기준 (색상 리스트로 덮어씀)
    text="Percentage"
)

# 색상 수동 지정
fig.update_traces(marker_color=colors, texttemplate="%{text}%", textposition="outside")
fig.update_layout(showlegend=False, yaxis_title="비율(%)", xaxis_title="국가")

st.plotly_chart(fig)
