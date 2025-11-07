# 서울 주요 관광지 TOP10을 폴리움으로 표시하는 스트림릿 앱
# 마커를 눈에 띄게 표시하고, 각 명소의 설명과 가장 가까운 지하철역 정보를 제공합니다.
# Streamlit Cloud에서도 바로 작동하도록 구성되었습니다.

import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="서울 관광지도", page_icon="🗺️", layout="wide")

st.title("🇰🇷 외국인이 사랑하는 서울의 명소 Top 10 🏙️")
st.write("서울의 인기 관광 명소를 한눈에 보고, 각 장소의 특징과 가장 가까운 지하철역을 확인해보세요!")

# 관광지 데이터
places = [
    {"name": "경복궁", "lat": 37.579617, "lon": 126.977041, "desc": "조선시대의 대표 궁궐로 아름다운 전통 건축미와 역사적 가치로 유명합니다.", "station": "경복궁역 (3호선)"},
    {"name": "명동거리", "lat": 37.563757, "lon": 126.982685, "desc": "서울의 대표 쇼핑 거리로 패션, 화장품, 길거리 음식이 풍부합니다.", "station": "명동역 (4호선)"},
    {"name": "남산타워 (N서울타워)", "lat": 37.551169, "lon": 126.988227, "desc": "서울의 전경을 한눈에 볼 수 있는 전망 명소로, 사랑의 자물쇠로도 유명합니다.", "station": "명동역 (4호선)"},
    {"name": "동대문디자인플라자 (DDP)", "lat": 37.566295, "lon": 127.009230, "desc": "자하 하디드가 설계한 독특한 디자인의 랜드마크로 패션과 전시의 중심지입니다.", "station": "동대문역사문화공원역 (2,4,5호선)"},
    {"name": "북촌한옥마을", "lat": 37.582604, "lon": 126.983998, "desc": "조선시대 전통 가옥들이 모여 있는 서울의 대표적인 한옥 마을입니다.", "station": "안국역 (3호선)"},
    {"name": "홍대거리", "lat": 37.557192, "lon": 126.923926, "desc": "젊음과 예술, 인디음악의 거리로 밤문화와 거리공연으로 유명합니다.", "station": "홍대입구역 (2호선, 공항철도)"},
    {"name": "이태원", "lat": 37.534545, "lon": 126.994519, "desc": "다양한 문화와 음식이 공존하는 서울의 대표적인 글로벌 거리입니다.", "station": "이태원역 (6호선)"},
    {"name": "청계천", "lat": 37.569128, "lon": 126.978640, "desc": "도심 속을 흐르는 복원된 하천으로, 야경이 아름답고 산책로로 인기입니다.", "station": "광화문역 (5호선)"},
    {"name": "롯데월드타워", "lat": 37.513068, "lon": 127.102497, "desc": "123층 초고층 타워로 쇼핑, 전망대, 호텔이 한곳에 모인 복합문화공간입니다.", "station": "잠실역 (2,8호선)"},
    {"name": "코엑스몰", "lat": 37.512527, "lon": 127.058819, "desc": "대형 쇼핑몰과 수족관, 도서관이 있는 서울 강남의 대표 명소입니다.", "station": "삼성역 (2호선)"}
]

# 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12, tiles='CartoDB positron')

# 마커 추가
for p in places:
    popup_html = f"""
    <b>{p['name']}</b><br>
    🏛️ {p['desc']}<br>
    🚇 <b>가까운 지하철역:</b> {p['station']}
    """
    folium.Marker(
        location=[p['lat'], p['lon']],
        popup=popup_html,
        tooltip=p['name'],
        icon=folium.Icon(color='red', icon='star', prefix='fa')
    ).add_to(m)

# 지도 표시
st_data = st_folium(m, width=900, height=600)

# 관광지 정보 섹션
st.subheader("📍 관광지 정보")
for p in places:
    with st.expander(f"{p['name']} - 🚇 {p['station']}"):
        st.write(p['desc'])

st.success("지도를 클릭하면 관광지 이름과 설명을 확인할 수 있습니다!")

# requirements.txt 표시
st.divider()
st.markdown("### 📦 requirements.txt")
st.code("""streamlit
folium
streamlit-folium
""", language="text")
