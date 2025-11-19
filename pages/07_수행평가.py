import streamlit as st
import pandas as pd
import os
import plotly.express as px
import chardet

st.set_page_config(page_title="서울 관광 음식 분석", layout="wide")

@st.cache_data
def load_data():
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.abspath(os.path.join(base_dir, "..", "서울시 관광 음식.csv"))

    with open(csv_path, "rb") as f:
        raw = f.read()
        enc = chardet.detect(raw)["encoding"]

    try:
        df = pd.read_csv(csv_path, encoding=enc)
    except:
        df = pd.read_csv(csv_path, encoding="cp949")

    return df

df = load_data()

st.title("🍽️ 서울시 관광 음식 데이터 분석")
st.write("📝 CSV 컬럼 목록:", df.columns.tolist())

# -----------------------------
# ⛳ 자동 컬럼 탐색
# -----------------------------
text_cols = df.select_dtypes(include="object").columns.tolist()
num_cols = df.select_dtypes(include="number").columns.tolist()

if not text_cols or not num_cols:
    st.error("⚠️ 텍스트 또는 숫자 컬럼이 부족합니다. CSV 파일 구조를 확인해주세요!")
    st.stop()

# 자동 후보 찾기 (가게명, 장소 등)
name_candidates = [c for c in text_cols if "가" in c or "업" in c or "명" in c or "소" in c]
name_col = name_candidates[0] if name_candidates else text_cols[0]

# 자동 숫자 컬럼 (방문수 관련 컬럼인지 찾기)
visit_candidates = [c for c in num_cols if "방문" in c or "수" in c or "건" in c]
num_col = visit_candidates[0] if visit_candidates else num_cols[0]

st.subheader("📌 사용할 컬럼 선택")
name_col = st.selectbox("이름(장소) 컬럼", text_cols, index=text_cols.index(name_col))
num_col = st.selectbox("숫자(방문 관련) 컬럼", num_cols, index=num_cols.index(num_col))

# -----------------------------
# 📊 데이터 정렬
# -----------------------------
df_sorted = df.sort_values(by=num_col, ascending=False).reset_index(drop=True)

# -----------------------------
# 🎨 색상 그라데이션
# -----------------------------
colors = ["red"] + [
    f"rgba(0, 0, 255, {1 - i/len(df_sorted)})"
    for i in range(1, len(df_sorted))
]

# -----------------------------
# 📈 Plotly 그래프
# -----------------------------
fig = px.bar(
    df_sorted,
    x=name_col,
    y=num_col,
    title=f"📊 {name_col} 기준 인기 순위"
)

fig.update_traces(marker=dict(color=colors))
fig.update_layout(
    xaxis_title=name_col,
    yaxis_title=num_col,
    template="plotly_white",
    title_font_size=22
)

st.plotly_chart(fig, use_container_width=True)
