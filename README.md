# USD/KRW 환율 1년 트렌드 분석

원/달러 환율 1년치(2025-09-19 ~ 2026-09-18) 일별 데이터를 이용한 시계열 분석 프로젝트입니다.
자세한 분석 내용은 **[REPORT.md](REPORT.md)** 를 참고하세요.

## 폴더 구조

```
usdkrw-analysis/
├── data/
│   ├── raw_2025.txt              # 원본 텍스트(2025년 히스토리 테이블)
│   ├── raw_2026.txt              # 원본 텍스트(2026년 히스토리 테이블)
│   ├── usdkrw_2025_2026.csv      # 파싱된 원본 데이터 (261행)
│   └── usdkrw_processed.csv      # 이동평균/변화율 등 파생변수 포함 데이터
├── images/
│   ├── 01_price_trend_ma.png
│   ├── 02_monthly_mean_volatility.png
│   ├── 03_change_distribution_weekday.png
│   ├── 04_stl_decomposition.png       (보너스: 시계열 분해)
│   └── 05_baseline_forecast.png       (보너스: 베이스라인 예측)
├── scripts/
│   └── fetch_and_parse.py        # 데이터 수집/파싱 스크립트
├── analysis.ipynb                # 전체 분석 노트북
├── REPORT.md                     # 최종 분석 리포트
├── requirements.txt
└── README.md
```

## 실행 방법

```bash
# 1. 의존성 설치
pip install -r requirements.txt

# 2. (선택) 원본 텍스트로부터 CSV 재생성
python scripts/fetch_and_parse.py

# 3. 노트북 실행
jupyter notebook analysis.ipynb   # 열어서 Run All
# 또는 커맨드라인에서 바로 실행:
jupyter nbconvert --to notebook --execute --inplace analysis.ipynb
```

## 데이터 출처

- [Pound Sterling Live — U.S. Dollar-South Korean Won History](https://www.poundsterlinglive.com/history/USD-KRW) (Bank of England 기준환율 데이터베이스 기반)
- 학습·개인 연구 목적으로만 사용. 상업적 재배포 시 원 사이트의 저작권 정책을 확인해야 합니다.

## 보너스 — 대시보드

기간(최근 30/90/180일/전체)을 바꿔가며 추세·변동성을 탐색할 수 있는 웹 대시보드를 제공합니다.

- **배포 URL**: https://claude.ai/artifact/RqhA5L1MBY1Wc6c1UaYEun
- **소스**: `dashboard/index.html` (Chart.js 기반, 데이터 내장형 단일 HTML 파일)
- **기능**: 기간 필터(30/90/180일/전체), 7일·30일 이동평균 토글, 고가-저가 밴드 토글, 구간별 통계 카드(변화율/최고가/최저가/변동성), 월별 평균·변동성 차트
