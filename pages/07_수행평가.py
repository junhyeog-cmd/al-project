import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="관광 데이터 분석", layout="wide")
st.title("📊 서울 관광 데이터 인터랙티브 분석")

# -----------------------------
# 🔹 CSV 불러오기 (상위 폴더에서)
# -----------------------------
@st.cache_data
def load_data():
    base_dir = os.path.dirname(__file__)            # pages 폴더 경로
    csv_path = os.path.abspath(os.path.join(base_dir, "..", "서울시 관광 음식.csv"))
    return pd.read_csv(csv_path)

df = load_data()

# -----------------------------
# 🔹 데이터 테이블 미리보기
# -----------------------------
st.subheader("📄 데이터 미리보기")
st.dataframe(df, use_container_width=True)

# -----------------------------
# 🔹 분석할 컬럼 선택
# -----------------------------
st.subheader("📌 분석 기준 설정")

# 숫자형 컬럼만 대상으로 선택
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
all_cols = df.columns.tolist()

place_col = st.selectbox("🗺️ 장소 이름이 들어있는 컬럼", all_cols)
value_col = st.selectbox("📈 방문자 수가 들어있는 숫자 컬럼", numeric_cols)

# -----------------------------
# 🔹 데이터 정렬
# -----------------------------
df_sorted = df.sort_values(by=value_col, ascending=False).reset_index(drop=True)

# -----------------------------
# 🔹 색상 지정 (1등=빨강, 나머지 파랑→회색 그라데이션)
# -----------------------------
colors = ["red"]  # 첫 번째 = 1등

# 파란색(blue) → 회색(gray) 그라데이션
import numpy as np

N = len(df_sorted) - 1
if N > 0:
    gradient = [
        f"rgb({int(0 + (180 * (i/N)))}, {int(90 + (90 * (i/N)))}, {255})"
        for i in range(N)
    ]
    colors.extend(gradient)

# -----------------------------
# 🔹 Plotly 그래프 생성
# -----------------------------
st.subheader("📊 인기 장소 순위 (방문자 수 기준)")

fig = px.bar(
    df_sorted,
    x=place_col,
    y=value_col,
    title="방문자 수 기준 인기 장소 순위",
)

# 색상 적용
fig.update_traces(marker_color=colors)

fig.update_layout(
    template="plotly_white",
    xaxis_title="장소",
    yaxis_title="방문자 수",
)

st.plotly_chart(fig, use_container_width=True)
