"""
USD/KRW 환율 데이터 수집 및 파싱 스크립트

[수집 방법]
1. https://www.poundsterlinglive.com/history/USD-KRW-2025
   https://www.poundsterlinglive.com/history/USD-KRW-2026
   위 두 페이지(연도별 히스토리 테이블)를 웹에서 조회하여 원본 텍스트를 확보했습니다.
   (Bank of England 기준환율을 바탕으로 한 일별 시가/종가/고가/저가 데이터)

2. 각 페이지의 데이터 테이블 행("| 날짜 | 시가 | 종가 | 고가 | 저가 | 중간값 |")을
   data/raw_2025.txt, data/raw_2026.txt 로 저장했습니다.

3. 이 스크립트는 위 두 원본 텍스트 파일을 정규식으로 파싱하여
   data/usdkrw_2025_2026.csv (분석용 정제 데이터)로 변환합니다.

[재현 방법]
    python scripts/fetch_and_parse.py

[주의]
이 스크립트는 이미 저장된 raw_*.txt를 파싱하는 용도이며, 실시간으로 웹에 재접속하지 않습니다.
데이터를 처음부터 새로 수집하려면 위 URL을 브라우저 또는 requests로 조회한 뒤,
페이지 내 히스토리 테이블(Date | Open | Close | High | Low | Mid)을 동일한 형식으로 저장하면 됩니다.
"""

import re
import csv


def parse_raw_file(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line.startswith("|"):
                continue
            parts = [p.strip() for p in line.strip("|").split("|")]
            if len(parts) != 6:
                continue
            date_field, o, c, h, l, m = parts
            m_date = re.search(r"\((\d{2})/(\d{2})/(\d{4})\)", date_field)
            if not m_date:
                continue
            dd, mm, yyyy = m_date.groups()
            date_str = f"{yyyy}-{mm}-{dd}"

            def clean(x):
                return float(x.replace(",", ""))

            rows.append([date_str, clean(o), clean(c), clean(h), clean(l), clean(m)])
    return rows


def main():
    rows = []
    for fname in ["data/raw_2025.txt", "data/raw_2026.txt"]:
        rows.extend(parse_raw_file(fname))

    rows.sort(key=lambda r: r[0])

    out_path = "data/usdkrw_2025_2026.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date", "open", "close", "high", "low", "mid"])
        w.writerows(rows)

    print(f"총 {len(rows)}행 저장 완료: {out_path}")
    print(f"기간: {rows[0][0]} ~ {rows[-1][0]}")


if __name__ == "__main__":
    main()
