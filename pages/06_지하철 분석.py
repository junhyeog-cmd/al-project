import os
import pandas as pd

@st.cache_data
def load_data():
    base_dir = os.path.dirname(__file__)            # pages 폴더 경로
    csv_path = os.path.abspath(os.path.join(base_dir, "..", "subway.csv"))
    
    df = pd.read_csv(csv_path, encoding="cp949")
    df["사용일자"] = df["사용일자"].astype(str)
    return df
