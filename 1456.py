"""
거의 소수
https://www.acmicpc.net/problem/1456
"""
a, b = map(int, input().split())

limit = int(b**0.5)

prime = [1] * (limit+1)

# 어차피 0과 1은 소수가 아니다.
prime[0] = prime[1] = 0

# 먼저 아리토스테네스의 체를 이용해 소수를 찾아준다.
for i in range(2, int(limit**0.5)+1):
    if prime[i]:
        for j in range(i*2, limit+1, i):
            prime[j] = 0

answer = 0

# 2이상의 수들 중에서
for i in range(2, len(prime)):
    # 소수라면
    if prime[i]:
        # 제곱수 초기화
        tmp = 0
        # 2제곱근 이상이므로 2부터 시작
        cnt = 2
        while 1:
            # 제곱수는 소수의 제곱이다.(여기서 i는 소수이다.)
            tmp = i**cnt

            # 만약 제곱수가 범위안에 있다면 정답 +1 해주고 다음 제곱수롤 넘어가기 위해 cnt +1 해준다.
            if a <= tmp <= b:
                answer += 1
                cnt += 1
            # 만약 a 보다 작다면 다음 제곱수를 위해 cnt + 1 해준다.
            elif tmp < a:
                cnt += 1
            # b보다 커지는 경우는 break 해주면 된다.
            else:
                break


print(answer)