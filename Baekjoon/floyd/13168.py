import sys

input = sys.stdin.readline

# 도시의 수, 내일로 티켓 가격
n, r = map(int, input().split())

# 도시들
city = list(input().split())

# 도시들 번호로 표현
city_num = {}

for i, j in enumerate(city, 1):
    city_num[j] = i

# 여행할 도시 수
m = int(input())

# 여행할 도시
travel = list(input().split())
for c in range(m):
    travel[c] = city_num[travel[c]]

# 교통 수단의 수
k = int(input())

for _ in range(k):
    t, a, b, cost = input().split()
    cost = int(cost)
    a, b = city_num[a], city_num[b]



"""
Subway = {}
Bus = {}
Taxi = {}
Airplane = {}
KTX = {}
S-Train = {}
V-Train = {}
ITX-Saemaeul = {}
ITX-Cheongchun = {}
Mugunghwa = {}
"""


print(travel)


