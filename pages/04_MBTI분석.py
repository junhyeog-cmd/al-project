import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# --- 페이지 설정 ---
st.set_page_config(page_title="🌍 세계 MBTI 비율 시각화", page_icon="🌏", layout="wide")

# --- 데이터 불러오기 ---
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# --- 제목 ---
st.title("🌍 나라별 MBTI 유형 비율 시각화")
st.markdown("국가를 선택하면 MBTI 유형별 비율을 인터랙티브 막대 그래프로 보여줍니다.")

# --- 국가 선택 ---
countries = df["Country"].sort_values().unique()
selected_country = st.selectbox("🌏 국가를 선택하세요", countries)

# --- 선택된 국가의 데이터 추출 ---
country_row = df[df["Country"] == selected_country].iloc[0, 1:]
country_df = pd.DataFrame({
    "MBTI 유형": country_row.index,
    "비율": country_row.values * 100  # 퍼센트로 변환
}).sort_values("비율", ascending=False)

# --- 색상 설정: 1등은 빨강, 나머지는 파랑 그라데이션 ---
colors = ["#FF4B4B"] + list(px.colors.sequential.Blues[len(country_df) - 1:0:-1])

# --- 그래프 생성 ---
fig = go.Figure()

fig.add_trace(go.Bar(
    x=country_df["MBTI 유형"],
    y=country_df["비율"],
    text=[f"{v:.2f}%" for v in country_df["비율"]],
    textposition="outside",
    marker_color=colors,
))

# --- 그래프 스타일 ---
fig.update_layout(
    title=f"🌎 {selected_country}의 MBTI 유형 비율",
    title_font_size=24,
    xaxis_title="MBTI 유형",
    yaxis_title="비율 (%)",
    plot_bgcolor="white",
    showlegend=False,
    margin=dict(l=40, r=40, t=80, b=40),
)
fig.update_yaxes(gridcolor="#EAEAEA")

# --- 시각화 출력 ---
st.plotly_chart(fig, use_container_width=True)

# --- 데이터 미리보기 ---
with st.expander("📋 원본 데이터 보기"):
    st.dataframe(df.head(), use_container_width=True)

# --- 푸터 ---
st.caption("데이터 출처: countriesMBTI_16types.csv | 제작: ChatGPT 💡")
