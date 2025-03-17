"""
주사위 윷놀이
문제: https://www.acmicpc.net/problem/17825
"""
import sys

input = sys.stdin.readline

dices = list(map(int, input().split()))
check = [0] * 10
horse = [0] * 4

board = [i for i in range(2, 41, 2)]
blue1 = [10, 13, 16, 19, 25, 30, 35, 40]
blue2 = [20, 22, 24, 25, 30, 35, 40]
blue3 = [30, 28, 27, 26, 25, 30, 35, 40]

def backtracking(cur1, cur2, cur3, cur4, horse1, horse2, horse3, horse4):

        for i in range(10):
            for j in range(4):
                if not check[i]:
                    check[i] = 1

                    check[i] = 0
