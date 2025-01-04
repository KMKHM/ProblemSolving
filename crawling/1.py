import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Selenium 설정 - 크롬 드라이버 경로 설정
driver_path = "/path/to/chromedriver"  # ChromeDriver의 실제 경로로 변경
driver = webdriver.Chrome(driver_path)

# 사이트 접속
driver.get("https://www.bigkinds.or.kr/v2/news/index.do")
time.sleep(2)  # 페이지 로딩 시간 대기

# IT/과학 카테고리 클릭 (XPath 또는 CSS Selector에 따라 변경 가능)
it_science_category = driver.find_element(By.XPATH, '//button[contains(text(),"IT_과학")]')
it_science_category.click()
time.sleep(2)  # 카테고리 로딩 시간 대기

# 현재 페이지에서 기사 목록 가져오기
soup = BeautifulSoup(driver.page_source, "html.parser")
articles = soup.select(".news-item")  # 각 기사의 CSS 클래스명에 따라 변경 가능

# 무작위 기사 선택
random_article = random.choice(articles)
article_link = random_article.find("a")["href"]

# 무작위 기사 클릭하여 상세 페이지 접근
driver.get("https://www.bigkinds.or.kr" + article_link)
time.sleep(2)

# 상세 페이지 크롤링
soup = BeautifulSoup(driver.page_source, "html.parser")
title = soup.find("h1", class_="news-title").get_text(strip=True)
content = soup.find("div", class_="news-contents").get_text(strip=True)

print("제목:", title)
print("내용:", content)

# 드라이버 종료
driver.quit()
