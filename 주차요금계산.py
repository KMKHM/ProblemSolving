import math
# 시간 정수 변환 함수
def cal_time(s):
    s = s.split(":")
    return int(s[0])*60 + int(s[1])


def solution(fees, records):
    record = []

    # 입차 딕셔너리
    dic_in = dict()
    
    # 출차 딕셔너리
    dic_cal = dict()
    
    # 23:59
    limit = 23*60 + 59
    
    for r in records:
        r = r.split()
        dic_cal[r[1]] = 0
        record.append([cal_time(r[0]), r[1], r[2]])
        
    record.sort(key=lambda x:x[1])
    
    for t, num, string in record:
        # 입차라면 시간기록
        if string == "IN":
            dic_in[num] = t
        # 출차
        else:
            # 시간계산딕셔너리에 출차시간에서 입차시간 빼서 기록
            dic_cal[num] += (t-dic_in[num])
            # 입차 기록 0으로 만들기
            del dic_in[num]
    
    for i, j in dic_in.items():
        dic_cal[i] += (limit -j)
    
    for i, j in dic_cal.items():
        if j <= fees[0]:
            dic_cal[i] = fees[1]
        else:
            dic_cal[i] = fees[1] + math.ceil((j-fees[0]) / fees[2]) * fees[3]
    answer =[j for i, j in sorted(dic_cal.items())]
    
    return answer