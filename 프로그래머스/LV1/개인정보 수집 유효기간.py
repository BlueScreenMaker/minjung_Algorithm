def solution(today, terms, privacies):
    terms_dict = {} #{"alpha" : "month"}
    todayYear,todayMonth,todayDay = map(int,today.split("."))
    for i in range(len(terms)) :
        name,month = terms[i].split()
        terms_dict[name] = int(month)
    indexs = []
    for i in range(len(privacies)) :
        startday,alpha = privacies[i].split()
        key = terms_dict[alpha]
        year,month,day = map(int,startday.split("."))
        if (month+key)>12 :
            year = year+1
            month = (month+key)-12
        else :
            month = month+key
        if todayYear>year :
            indexs.append(i+1)
        elif (todayYear==year) :
            if todayMonth>month :
                indexs.append(i+1)
            elif (todayMonth==month) and (todayDay>=day) :
                indexs.append(i+1)
    return indexs
