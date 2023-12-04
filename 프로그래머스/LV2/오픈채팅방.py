def solution(record):
    answer = []
    users = dict()
    actions = []

    for i in range(len(record)) :
        if "Enter" in record[i]  :
            users[record[i].split()[1]] = record[i].split()[2]
            actions.append([record[i].split()[1],1])
        elif "Change" in record[i] :
            users[record[i].split()[1]] = record[i].split()[2]
        else :  
            actions.append([record[i].split()[1],0])
    
    for act in actions :
        act[0] = users[act[0]]
        if act[1] == 1:
            act[1] = "님이 들어왔습니다."
        else :
            act[1] = "님이 나갔습니다."
        answer.append(act[0]+act[1])
    return answer