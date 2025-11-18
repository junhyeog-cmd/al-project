import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go

# -------------------------
# Streamlit 기본 세팅
# -------------------------
st.set_page_config(page_title="서울 지하철 분석", layout="wide")
st.title("🚇 2025년 10월 서울 지하철 이용 분석")

# -------------------------
# CSV 로드 함수 (100% 안정)
# -------------------------
@st.cache_data
def load_data():
    # pages 폴더 기준 → 상위 subway.csv
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.abspath(os.path.join(base_dir, "..", "subway.csv"))

    if not os.path.exists(csv_path):
        st.error(f"❌ CSV 파일을 찾을 수 없습니다:\n{csv_path}")
        return None

    df = pd.read_csv(csv_path, encoding="cp949")
    df["사용일자"] = df["사용일자"].astype(str)
    return df

df = load_data()
if df is None:
    st.stop()

# -------------------------
# UI 선택 요소
# -------------------------
dates = sorted(df[df["사용일자"].str.startswith("202510")]["사용일자"].unique())
lines = sorted(df["노선명"].unique())

col1, col2 = st.columns(2)
with col1:
    selected_date = st.selectbox("📅 날짜 선택", dates)
with col2:
    selected_line = st.selectbox("🚈 호선 선택", lines)

# -------------------------
# 데이터 필터링
# -------------------------
filtered = df[(df["사용일자"] == selected_date) & (df["노선명"] == selected_line)].copy()
filtered["총이용객수"] = filtered["승차총승객수"] + filtered["하차총승객수"]
filtered = filtered.sort_values("총이용객수", ascending=False)

# -------------------------
# 색상 설정 (그라데이션)
# -------------------------
colors = []
total_rows = len(filtered)
for i in range(total_rows):
    if i == 0:
        colors.append("red")
    else:
        opacity = 1 - (i / total_rows) * 0.7
        colors.append(f"rgba(30, 90, 200, {opacity})")

# -------------------------
# Plotly 막대그래프
# -------------------------
fig = go.Figure()
fig.add_trace(go.Bar(
    x=filtered["역명"],
    y=filtered["총이용객수"],
    marker=dict(color=colors),
    hovertemplate="역명: %{x}<br>총 이용객수: %{y}<extra></extra>",
))

fig.update_layout(
    title=f"📊 {selected_date} / {selected_line} 승하차 총 이용객수 TOP 역",
    xaxis_title="역명",
    yaxis_title="총 이용객수",
    template="plotly_white",
    height=600
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# 데이터 테이블
# -------------------------
with st.expander("📄 데이터 보기"):
    st.dataframe(filtered)
