import csv

data = [
    ["Category", "Description"],
    ["별칭", "ISTP - 장인형 (Virtuoso / Craftsman)"],
    ["성격 개요", "논리적이고 실용적이며, 도구 다루기와 문제 해결에 강한 유형"],
    ["주요 특성", "냉정함, 분석적 사고, 손재주, 즉흥적 유연성, 실험적 성향"],
    ["강점", "실용적 해결 능력, 위기 대처 능력, 집중력, 독립성"],
    ["약점", "감정 표현 어려움, 일관성 부족, 장기 계획에 약함"],
    ["선호하는 환경", "자율성 높은 환경, 실험·조작 가능한 상황, 간섭 적은 업무"],
    ["직업 예시", "엔지니어, 정비사, 프로그래머, 파일럿, 데이터 분석가, 구조·특수직"],
    ["대인관계 스타일", "과묵하지만 현실적 도움 제공, 과한 감정적 교류를 선호하지 않음"]
]

with open("istp_info.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("istp_info.csv 파일이 생성되었습니다.")

