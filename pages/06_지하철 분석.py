import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="서울 지하철 분석", layout="wide")

st.title("🚇 2025년 10월 서울 지하철 이용 분석")

# CSV 파일 불러오기 (상위 폴더)
@st.cache_data
def load_data():
    df = pd.read_csv("../subway.csv", encoding="cp949")
    df["사용일자"] = df["사용일자"].astype(str)
    return df

df = load_data()

# 2025년 10월 날짜 리스트 만들기
dates_2025_10 = sorted(df[df["사용일자"].str.startswith("202510")]["사용일자"].unique())

# --- 선택 박스 ---
col1, col2 = st.columns(2)

with col1:
    selected_date = st.selectbox("📅 날짜 선택", dates_2025_10)

with col2:
    selected_line = st.selectbox("🚈 호선 선택", sorted(df["노선명"].unique()))

# 필터링
filtered = df[(df["사용일자"] == selected_date) & (df["노선명"] == selected_line)].copy()

# 승하차 합계 계산
filtered["총이용객수"] = filtered["승차총승객수"] + filtered["하차총승객수"]
filtered = filtered.sort_values(by="총이용객수", ascending=False)

# 색상 설정
colors = []
for i in range(len(filtered)):
    if i == 0:
        colors.append("red")
    else:
        # 파란색 → 밝아지는 그라데이션
        opacity = 1 - (i / len(filtered)) * 0.7
        colors.append(f"rgba(30, 90, 200, {opacity})")

# Plotly bar chart
fig = go.Figure()

fig.add_trace(go.Bar(
    x=filtered["역명"],
    y=filtered["총이용객수"],
    marker=dict(color=colors),
    hovertemplate="역명: %{x}<br>총이용객수: %{y}<extra></extra>"
))

fig.update_layout(
    title=f"📊 {selected_date} / {selected_line} 승하차 총이용객수 순위",
    xaxis_title="역명",
    yaxis_title="총 이용객수",
    template="plotly_white",
    width=1000,
    height=600
)

st.plotly_chart(fig, use_container_width=True)

# 데이터 표 보기
with st.expander("📄 데이터 테이블 보기"):
    st.dataframe(filtered)
