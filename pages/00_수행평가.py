import streamlit as st
import pandas as pd

st.title("ISTP 정보 CSV 생성기")

# ISTP 데이터
data = {
    "Category": [
        "별칭",
        "성격 개요",
        "주요 특성",
        "강점",
        "약점",
        "선호하는 환경",
        "직업 예시",
        "대인관계 스타일"
    ],
    "Description": [
        "ISTP - 장인형 (Virtuoso / Craftsman)",
        "논리적이고 실용적이며, 도구 다루기와 문제 해결에 강한 유형",
        "냉정함, 분석적 사고, 손재주, 즉흥적 유연성, 실험적 성향",
        "실용적 해결 능력, 위기 대처 능력, 집중력, 독립성",
        "감정 표현 어려움, 일관성 부족, 장기 계획에 약함",
        "자율성 높은 환경, 실험·조작 가능한 상황, 간섭 적은 업무",
        "엔지니어, 정비사, 프로그래머, 파일럿, 데이터 분석가, 구조·특수직",
        "과묵하지만 현실적 도움 제공, 과한 감정적 교류를 선호하지 않음"
    ]
}

df = pd.DataFrame(data)

st.write("### ISTP 기본 정보 미리보기")
st.dataframe(df)

# CSV 변환
csv = df.to_csv(index=False, encoding="utf-8-sig")

# 다운로드 버튼
st.download_button(
    label="📥 ISTP 정보 CSV 다운로드",
    data=csv,
    file_name="istp_info.csv",
    mime="text/csv"
)
