# Python 3에서 실행하세요.
# istp_info.csv 파일을 현재 폴더에 생성합니다.
import csv
import os
import sys

rows = [
    {"Category": "별칭", "Description": "ISTP - 장인형 (Virtuoso / Craftsman)"},
    {"Category": "성격 개요", "Description": "논리적이고 실용적이며, 도구 다루기와 문제 해결에 강한 유형"},
    {"Category": "주요 특성", "Description": "냉정함, 분석적 사고, 손재주, 즉흥적 유연성, 실험적 성향"},
    {"Category": "강점", "Description": "실용적 해결 능력, 위기 대처 능력, 집중력, 독립성"},
    {"Category": "약점", "Description": "감정 표현 어려움, 일관성 부족, 장기 계획에 약함"},
    {"Category": "선호하는 환경", "Description": "자율성 높은 환경, 실험·조작 가능한 상황, 간섭 적은 업무"},
    {"Category": "직업 예시", "Description": "엔지니어, 정비사, 프로그래머, 파일럿, 데이터 분석가, 구조·특수직"},
    {"Category": "대인관계 스타일", "Description": "과묵하지만 현실적 도움 제공, 과한 감정적 교류를 선호하지 않음"}
]

filename = "istp_info.csv"

try:
    # utf-8-sig는 Excel에서 한글 깨짐을 방지하기 위해 BOM을 포함한 utf-8 인코딩을 사용합니다.
    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        fieldnames = ["Category", "Description"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)
    print(f"파일 생성 완료: {os.path.abspath(filename)}")
except Exception as e:
    print("파일 생성 중 오류가 발생했습니다:", file=sys.stderr)
    print(repr(e), file=sys.stderr)
    sys.exit(1)

