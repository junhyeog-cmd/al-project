import pandas as pd

# 파일 이름
file_name = "(주)강원랜드_카지노게임현황_20241231.csv"

# 데이터프레임 불러오기
try:
    df = pd.read_csv(file_name)
    
    # 데이터 상위 5개 행 출력
    print("--- 데이터프레임 상위 5개 행 ---")
    print(df.head())
    
    # 데이터 정보 요약
    print("\n--- 데이터프레임 정보 요약 ---")
    print(df.info())

except FileNotFoundError:
    print(f"오류: 파일 '{file_name}'을 찾을 수 없습니다. 파일 이름을 확인해주세요.")
except Exception as e:
    print(f"데이터를 불러오는 중 오류 발생: {e}")
