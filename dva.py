def solution(m, music):
    # 재생시간 메소드
    def time_diff(a, b):
        return int(b[:2]) * 60 + int(b[3:]) - int(a[:2]) * 60 - int(a[3:])

#  time_diff 계산전에 # 처리

    def check(s1, s2): # m, music
        s2 = s2.replace(s1+"#", "1")
        # abc, abc#d => 1d => false
        return s1 in s2

    # 정답, 정답일 때 재생시간
    ans, ans_diff = "", 0

    #     m = m.replace('A#', '1').replace('G#', '2').replace('F#', '3').replace('D#', '4').replace('C#', '5')

    for info in music:
        s, e, t, a = info.split(",")
        # a = a.replace('A#', '1').replace('G#', '2').replace('F#', '3').replace('D#', '4').replace('C#', '5')
        diff = time_diff(s, e)  # 재생시간
        if diff >= len(a):  # 재생시간이 악보보다 큰 경우
            tmp = a
            while diff >= len(a):  # 악보하고 비슷하거나 클때까지 복사
                a += tmp
        else:
            a = a[:diff]

        if not m.endswith("#"): # 안끝난 경우
            if check(m, a) and diff > ans_diff:
                ans, ans_diff = t, diff
        else: # #으로 끝난 경우
            if m in a and diff > ans_diff:
                ans, ans_diff = t, diff

    return ans if ans else "(None)"