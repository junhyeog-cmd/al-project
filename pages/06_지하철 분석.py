import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="서울 지하철 분석", layout="wide")

@st.cache_data
def load_data():
    # pages/ 파일 기준
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path_1 = os.path.abspath(os.path.join(base_dir, "..", "subway.csv"))

    # Streamlit Cloud 루트 기준
    csv_path_2 = os.path.abspath("subway.csv")

    # fallback 경로
    csv_path_3 = os.path.abspath("./subway.csv")

    path_list = [csv_path_1, csv_path_2, csv_path_3]

    st.subheader("🔍 CSV 검색 경로")
    for idx, p in enumerate(path_list, start=1):
        st.write(f"{idx}. `{p}`")

    # 파일 존재 여부 체크 + 경로 표시
    for p in path_list:
        if os.path.exists(p):
            st.success(f"📂 **CSV 찾음! → `{p}`**")
            df = pd.read_csv(p, encoding="cp949")
            df["사용일자"] = df["사용일자"].astype(str)
            return df

    # 못 찾으면 안내
    st.error("❌ subway.csv 파일을 찾을 수 없습니다.\n위 경로들을 확인하세요.")
    return None

df = load_data()

if df is None:
    st.stop()
