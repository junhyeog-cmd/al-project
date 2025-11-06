import streamlit as st

# 🎨 앱 기본 설정
st.set_page_config(page_title="MBTI 책·영화 추천 🎬📚", page_icon="💫")

st.title("💫 MBTI별 책 & 영화 추천")
st.write("너의 MBTI를 선택하면, 딱 맞는 **책 2권📚**과 **영화 2편🎬**을 추천해줄게!")

# 🎯 MBTI 선택
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]
user_mbti = st.selectbox("👉 너의 MBTI를 골라줘!", mbti_list)

# 📚 데이터: MBTI별 책 & 영화 추천
recommendations = {
    "INTJ": {
        "books": [
            ("사피엔스", "인류의 흐름을 통찰하는 책 🧠"),
            ("데미안", "자신의 세계를 찾아가는 여정 ✨")
        ],
        "movies": [
            ("인터스텔라", "깊은 철학과 감동의 SF 명작 🚀"),
            ("셜록", "논리와 추리의 끝판왕 🕵️")
        ]
    },
    "INFP": {
        "books": [
            ("어린 왕자", "순수함과 진심을 다시 느끼게 해주는 고전 💛"),
            ("참을 수 없는 존재의 가벼움", "사랑과 존재의 의미를 고민하게 만드는 책 🌌")
        ],
        "movies": [
            ("월-E", "감정이 가득한 로봇 이야기 🤖💞"),
            ("이터널 선샤인", "사랑과 기억에 대한 잔잔한 영화 🌙")
        ]
    },
    "ENFP": {
        "books": [
            ("미움받을 용기", "자기 자신을 사랑하는 법 💪"),
            ("죽음에 관하여", "삶을 더 소중히 느끼게 하는 책 🌻")
        ],
        "movies": [
            ("인사이드 아웃", "감정의 세계를 유쾌하게 풀어낸 애니메이션 🎨"),
            ("라라랜드", "꿈과 사랑 사이에서 빛나는 이야기 🎶")
        ]
    },
    "ISTJ": {
        "books": [
            ("총, 균, 쇠", "세상의 질서를 이해하려는 사람에게 📘"),
            ("나미야 잡화점의 기적", "작은 성실함이 만든 따뜻한 기적 🎁")
        ],
        "movies": [
            ("포레스트 검프", "꾸준함과 진심이 만들어낸 감동 🌳"),
            ("이미테이션 게임", "논리적 사고와 책임감의 결정체 💻")
        ]
    },
    "ESFP": {
        "books": [
            ("아몬드", "감정을 배우는 소년의 이야기 💖"),
            ("무지개를 기다리며", "밝고 긍정적인 에너지 가득 🌈")
        ],
        "movies": [
            ("맘마미아!", "음악과 춤이 가득한 행복한 에너지 🎤"),
            ("인턴", "따뜻한 인간미가 느껴지는 힐링무비 ☕")
        ]
    }
}

# 기본 추천 (혹시 없는 MBTI일 경우)
default = {
    "books": [("자기 개발서", "너만의 길을 응원할게 🌱"), ("고양이의 하루", "쉬어가는 힐링 타임 🐾")],
    "movies": [("업", "꿈과 모험의 감동 💭"), ("인사이드 아웃", "감정이란 게 뭘까? 🎨")]
}

# 💡 추천 결과 출력
data = recommendations.get(user_mbti, default)

st.subheader(f"📚 {user_mbti} 유형에게 어울리는 책 추천!")
for title, desc in data["books"]:
    st.markdown(f"**{title}** — {desc}")

st.subheader("🎬 어울리는 영화 추천!")
for title, desc in data["movies"]:
    st.markdown(f"**{title}** — {desc}")

st.divider()
st.write("💬 *추천이 마음에 들었으면 친구한테도 공유해줘!* 😄")
