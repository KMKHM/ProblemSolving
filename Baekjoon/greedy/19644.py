"""
좀비 떼가 기관총 진지에도 오다니
문제: https://www.acmicpc.net/problem/19644
"""
import sys
from collections import deque

input = sys.stdin.readline

L = int(input())

# 사격 거리, 데미지
ml, mk = map(int, input().split())

# 수류탄 수
c = int(input())

# 좀비
zombie = deque(int(input()) for _ in range(L))

# 좀비 전체 체력
zh = sum(zombie)

# 현재 인덱스
idx = 0

while 1:
    # ml 거리에 있는 좀비의 체력 모두 깎기
    if len(zombie) <= ml:
        #for i in range(len(zombie)):
        #    zombie[i] -= mk
        zh -= (mk * len(zombie))

    else:
        # for i in range(ml):
        #     zombie[i] -= mk
        zh -= (mk * ml)

    # 인덱스 있는 좀비 체력깍기
    zombie[idx] -= mk

    # 가장 앞에 있는 좀비의 체력이 0 보다 작으면 idx + 1
    if zombie[idx] <= 0:
        idx += 1
    else:
        # 수류탄 있으면 사용
        if c > 0:
            c -= 1
            idx += 1
        # 없으면 게임 끝
        else:
            print("NO")
            break

    # 더 이상 좀비가 없으면
    if zh <= 0:
        print("YES")
        break

