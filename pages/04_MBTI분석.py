import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌎 MBTI 유형별 국가 분포 시각화")

# -------------------------------
# 예시 데이터 (MBTI 16유형 × 6개국)
# 실제 분석 데이터로 교체 가능
# -------------------------------
data = []
countries = ["한국", "미국", "일본", "영국", "독일", "프랑스"]
mbti_types = [
    "INTJ","INTP","ENTJ","ENTP",
    "INFJ","INFP","ENFJ","ENFP",
    "ISTJ","ISFJ","ESTJ","ESFJ",
    "ISTP","ISFP","ESTP","ESFP"
]

import random
random.seed(42)
for mbti in mbti_types:
    for country in countries:
        # MBTI와 국가별 임의의 비율 (5~30%)
        data.append({
            "MBTI": mbti,
            "Country": country,
            "Percentage": random.randint(5, 30)
        })

df = pd.DataFrame(data)

# -------------------------------
# 사용자 입력
# -------------------------------
selected_mbti = st.selectbox("🔍 MBTI 유형을 선택하세요:", mbti_types)

# 선택한 MBTI에 해당하는 데이터 필터링
filtered = df[df["MBTI"] == selected_mbti].sort_values(by="Percentage", ascending=False)

# -------------------------------
# 색상 설정
# -------------------------------
colors = []
max_country = filtered.iloc[0]["Country"]  # 1등 국가
for c in filtered["Country"]:
    if c == "한국":
        colors.append("dodgerblue")  # 한국은 파란색
    elif c == max_country:
        colors.append("gold")        # 1등은 노란색
    else:
        colors.append("lightgray")   # 나머지는 회색

# -------------------------------
# Plotly 그래프 생성
# -------------------------------
fig = px.bar(
    filtered,
    x="Country",
    y="Percentage",
    text="Percentage",
    title=f"{selected_mbti} 유형이 많은 나라 순위"
)

# 색상 지정 및 스타일 조정
fig.update_traces(
    marker_color=colors,
    texttemplate="%{text}%",
    textposition="outside"
)
fig.update_layout(
    showlegend=False,
    yaxis_title="비율(%)",
    xaxis_title="국가",
    title_font_size=18,
    plot_bgcolor="white"
)

st.plotly_chart(fig)
