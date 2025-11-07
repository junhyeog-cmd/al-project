import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="서울 관광지도 🌆", layout="wide")

st.title("🌍 외국인이 좋아하는 서울 관광지 Top 10")
st.markdown("서울의 인기 명소들을 지도에서 한눈에 확인해보세요!")

# 관광지 데이터
places = [
    {"name": "경복궁", "lat": 37.579617, "lon": 126.977041, "desc": "조선의 대표 궁궐 🇰🇷"},
    {"name": "명동", "lat": 37.563757, "lon": 126.982669, "desc": "쇼핑과 거리음식의 천국 🛍️"},
    {"name": "남산타워 (N서울타워)", "lat": 37.551169, "lon": 126.988227, "desc": "서울의 전망 명소 🌃"},
    {"name": "홍대거리", "lat": 37.556335, "lon": 126.922651, "desc": "젊음과 예술의 거리 🎶"},
    {"name": "북촌한옥마을", "lat": 37.582604, "lon": 126.983998, "desc": "전통 한옥의 아름다움 🏡"},
    {"name": "청계천", "lat": 37.570227, "lon": 126.989511, "desc": "도심 속 힐링 산책로 🌿"},
    {"name": "이태원", "lat": 37.534502, "lon": 126.994396, "desc": "다문화의 거리 🌎"},
    {"name": "롯데월드", "lat": 37.511000, "lon": 127.098000, "desc": "서울의 대표 테마파크 🎢"},
    {"name": "잠실 롯데타워", "lat": 37.513068, "lon": 127.102527, "desc": "대한민국의 랜드마크 🏙️"},
    {"name": "광장시장", "lat": 37.570384, "lon": 127.001844, "desc": "전통시장과 길거리 음식 🍢"},
]

# 지도 중심 설정
map_center = [37.5665, 126.9780]
m = folium.Map(location=map_center, zoom_start=12)

# 관광지 마커 표시
for place in places:
    folium.Marker(
        [place["lat"], place["lon"]],
        popup=f"<b>{place['name']}</b><br>{place['desc']}",
        tooltip=place["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# 지도 출력
st_data = st_folium(m, width=800, height=600)

st.markdown("---")
st.caption("🗓️ 데이터 출처: VisitSeoul / Tripadvisor / Google Travel")
