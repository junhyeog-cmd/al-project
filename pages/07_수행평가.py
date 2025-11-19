import streamlit as st
import pandas as pd
import os
import plotly.express as px
import chardet

st.set_page_config(page_title="서울 관광 음식 분석", layout="wide")

# ------------------------------
# 데이터 로드 함수
# ------------------------------
@st.cache_data
def load_data():
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.abspath(os.path.join(base_dir, "..", "서울시 관광 음식.csv"))

    # 인코딩 자동 감지
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

st.subheader("데이터 미리보기")
st.dataframe(df, use_container_width=True)

# ------------------------------
# 🔍 가장 인기 있는 음식점 분석
# ------------------------------

# 방문 수(또는 해당 CSV에서 사람들이 많이 간 정도를 나타내는 컬럼명 파악 필요)
# 방문자 관련 컬럼 찾기
numeric_cols = df.select_dtypes(include="number").columns.tolist()

if len(numeric_cols) == 0:
    st.error("⚠️ 숫자 타입의 방문자 또는 점수 데이터가 없습니다. CSV 컬럼명을 알려주세요!")
else:
    num_col = st.selectbox("어떤 값(숫자)을 기준으로 인기 순위를 볼까요?", numeric_cols)

    # 인기순으로 정렬
    df_sorted = df.sort_values(by=num_col, ascending=False).reset_index(drop=True)

    # 색상 설정 (1등은 빨강, 나머지는 파랑-회색 그라데이션)
    colors = ["red"] + [
        f"rgba(0, 0, 255, {1 - i/len(df_sorted)})" for i in range(1, len(df_sorted))
    ]

    # 막대그래프 생성
    fig = px.bar(
        df_sorted,
        x="업소명",     # 음식점 이름 컬럼(필요하면 실제 컬럼명에 맞게 수정 가능!)
        y=num_col,
        title="📊 인기 음식점 순위",
    )

    fig.update_traces(marker=dict(color=colors))

    fig.update_layout(
        xaxis_title="음식점",
        yaxis_title=num_col,
        template="plotly_white",
        title_font_size=22
    )

    st.plotly_chart(fig, use_container_width=True)
