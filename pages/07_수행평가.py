import streamlit as st
import pandas as pd
import os
import chardet

st.set_page_config(page_title="수행평가 분석", layout="wide")


@st.cache_data
def load_data():
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.abspath(os.path.join(base_dir, "..", "서울시 관광 음식.csv"))

    # 1️⃣ 먼저 파일 인코딩 자동 감지
    with open(csv_path, "rb") as f:
        rawdata = f.read()
        result = chardet.detect(rawdata)
        enc = result["encoding"]

    try:
        # 2️⃣ 감지된 인코딩으로 읽기
        return pd.read_csv(csv_path, encoding=enc)
    except:
        # 3️⃣ 실패하면 CP949로 다시 시도
        return pd.read_csv(csv_path, encoding="cp949")


df = load_data()
st.write("✅ 데이터 불러오기 성공!")
st.dataframe(df)
