import requests

# 요청 URL과 헤더 설정
url = "https://datalab.naver.com/keyword/trendSearch.naver"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "https://datalab.naver.com/",
}

# 요청 파라미터 (네트워크 탭에서 분석 필요)
params = {
    "startDate": "2023-01-01",
    "endDate": "2023-12-31",
    "timeUnit": "month",
    "keyword": "example_keyword",
    "device": "",
    "gender": "",
    "ages": ""
}

response = requests.get(url, headers=headers, params=params)

# 응답 데이터 출력
if response.status_code == 200:
    print(response.text)  # HTML 또는 JSON 확인
else:
    print(f"요청 실패: {response.status_code}")
