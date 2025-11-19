import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("수행평가 분석 페이지")

st.write("이 페이지는 수행평가 데이터를 분석하기 위한 예시 화면입니다.")

# CSV 파일 불러오기 (루트 폴더)
try:
    df = pd.read_csv("./(주)강원랜드_카지노게임현황_20241231.csv", encoding="cp949")
    st.write("### 원본 데이터")
    st.dataframe(df)
except Exception as e:
    st.error("CSV 파일을 불러오는 중 오류 발생: " + str(e))

# 데이터가 있을 때만 분석
if 'df' in locals():
    grouped = df.groupby("게임명", as_index=False)["대수"].sum()

    # 1등 색상 빨간색
    max_value = grouped["대수"].max()
    grouped = grouped.sort_values("대수", ascending=False)
    colors = ["red" if v == max_value else "rgba(255,150,150,0.6)" for v in grouped["대수"]]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=grouped["게임명"],
        y=grouped["대수"],
        marker=dict(color=colors)
    ))

    fig.update_layout(
        title="게임별 보유 대수 (1등=빨간색)",
        xaxis_title="게임명",
        yaxis_title="대수"
    )

    st.write("### 수행평가 그래프 예시")
    st.plotly_chart(fig)
