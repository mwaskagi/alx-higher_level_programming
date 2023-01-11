#!/usr/bin/python3
def weight_average(my_list=[]):
    avg, cnt, div = 1, 0, 0
    sum_avg = 0
    if my_list == []:
        return 0
    for i in my_list:
        for j in i:
            avg *= j
            if cnt == 1:
                div += j
            cnt += 1
        sum_avg += avg
        avg, cnt = 1, 0
    total = sum_avg / div
    return total
