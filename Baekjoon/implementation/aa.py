# 시간 계산
start, end = "05:34", "07:59"


# 시간 계산 함수
def time_calc(start, end):
    start = start.split(":")
    end = end.split(":")
    start_time = int(start[0]) * 60 + int(start[1])
    end_time = int(end[0]) * 60 + int(end[1])
    return end_time - start_time

a = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
dic = dict()

for e in a:
    e = e.split()
    if e[2] == "IN":
        dic[e[1]] = [e[0], 1]
    if e[2] == "OUT":
        if e[1] in dic:
            dic[e[1]] = [time_calc(dic[e[1]], e[0]), 0]

print(dic)

# fees = [180, 5000, 10, 600]
# cnt = 0
# print(dic)
#
# for car in dic.keys():


