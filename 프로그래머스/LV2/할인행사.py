def solution(want, number, discount):
    wants = []
    for i in range(len(want)) :
        for num in range(number[i]) :
            wants.append(want[i])
    wants = sorted(wants)

    answer = 0
    for j in range(len(discount)-9) :
        discount_days = []
        for k in range(j,j+10) :
            if discount[k] in want :
                discount_days.append(discount[k])
        discount_days = sorted(discount_days)
        if discount_days == wants :
            answer +=1
    return answer