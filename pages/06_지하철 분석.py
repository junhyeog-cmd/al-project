import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="서울 지하철 분석", layout="wide")

# ----------------------------------------------------
# 🔥 절대 오류 안 나는 완전 안정형 로더
# (경로 3단계 체크 + 파일 존재 확인 + 에러 표시)
# ----------------------------------------------------
@st.cache_data
def load_data():
    # 1) 현재 파일 위치 기준
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path_1 = os.path.abspath(os.path.join(base_dir, "..", "subway.csv"))

    # 2) 프로젝트 루트 기준 (Streamlit Cloud에서 흔함)
    csv_path_2 = os.path.abspath("subway.csv")

    # 3) 실행 위치 기준 (fallback)
    csv_path_3 = os.path.abspath("./subway.csv")

    # 파일 존재 확인 (1 → 2 → 3)
    for p in [csv_path_1, csv_path_2, csv_path_3]:
        if os.path.exists(p):
            st.write(f"📂 CSV 로드 경로: `{p}`")
            df = pd.read_csv(p, encoding="cp949")
            df["사용일자"] = df["사용일자"].astype(str)
            return df

    # 만약 3개 경로 모두 실패 → 오류 메시지 출력
    st.error("❌ subway.csv 파일을 찾을 수 없습니다.\n아래 경로들을 확인해 주세요:")
    st.code(f"""
{csv_path_1}
{csv_path_2}
{csv_path_3}
    """)
    return None

df = load_data()

if df is None:
    st.stop()
