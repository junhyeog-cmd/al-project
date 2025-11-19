# requirements.txt
# ------------------
# Streamlit & Plotly dependencies
streamlit
pandas
plotly


# pages/game_analysis.py
# -----------------------
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# CSV 파일 불러오기 (루트 폴더)
df = pd.read_csv("./(주)강원랜드_카지노게임현황_20241231.csv", encoding="cp949")

st.title("강원랜드 카지노 게임 현황 분석")

st.write("### 원본 데이터")
st.dataframe(df)

# 게임별 대수 합산
grouped = df.groupby("게임명", as_index=False)["대수"].sum()

# 1등(대수가 가장 높은 게임) 색 빨간색 처리
max_value = grouped["대수"].max()
grouped = grouped.sort_values("대수", ascending=False)

colors = ["red" if v == max_value else "rgba(255,150,150,0.6)" for v in grouped["대수"]]

# Plotly 그래프 생성
fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=grouped["게임명"],
        y=grouped["대수"],
        marker=dict(color=colors)
    )
)

fig.update_layout(
    title="게임별 보유 대수 (1등=빨간색, 나머지=그라데이션)",
    xaxis_title="게임명",
    yaxis_title="대수",
)

st.write("### 게임별 대수 시각화")
st.plotly_chart(fig)
