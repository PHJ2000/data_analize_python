# Data Analysis with Python - Streamlit 기반 데이터 분석 대시보드

## 프로젝트 개요
이 프로젝트는 **Python과 Streamlit을 활용한 데이터 분석 웹 애플리케이션**입니다.
네이버 금융 데이터를 활용한 **환율 분석**, 서울 공공자전거(따릉이) 및 유성우 데이터 분석 기능을 포함하고 있습니다.

## 주요 기능
- **Streamlit 기반 웹 대시보드 제공**
- **네이버 금융 데이터를 크롤링하여 환율 분석** (`finance_naver.py`)
- **서울 공공자전거(따릉이) 데이터 분석** (추가 예정)
- **유성우 데이터 분석** (추가 예정)
- **데이터 시각화 (pandas, matplotlib 활용)**

## 프로젝트 구조
```
data_analize_python/
│── aischoolmain.py  # Streamlit 대시보드 실행 파일
│── finance_naver.py  # 네이버 금융 크롤링 및 환율 분석 코드
│── requirements.txt  # 필요 라이브러리 목록
│── README.md  # 프로젝트 설명 파일
```

## 설치 및 실행 방법
### 1. 필수 라이브러리 설치
```bash
pip install -r requirements.txt
```

### 2. Streamlit 애플리케이션 실행
```bash
streamlit run aischoolmain.py
```

## 사용 방법
1. **Streamlit 웹 애플리케이션 접속**
2. **사이드바에서 로그인 (기본 패스워드: 1234)**
3. **메뉴 선택**
   - `환율조회`: 네이버 금융 데이터를 활용하여 실시간 환율 조회
   - `따릉이`: 서울 공공자전거 데이터 분석 (추가 예정)
   - `유성우`: 유성우 데이터 분석 (추가 예정)

## 필요 라이브러리
- `streamlit`
- `pandas`
- `matplotlib`
- `requests`

## 기여 방법
1. 본 레포지토리를 포크합니다.
2. 새로운 브랜치를 생성합니다.
3. 변경 사항을 커밋하고 푸시합니다.
4. Pull Request를 생성하여 기여합니다.

## 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다.

