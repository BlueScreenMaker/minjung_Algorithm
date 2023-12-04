def solution(k,m,score) :
    answer = 0
    score = sorted(score)
    boxes = []
    for i in range(len(score)//m) :
        box = []
        for j in range(m) :
            box.append(score[-1])
            del score[-1]
        boxes.append(m*min(box))
    answer = sum(boxes)
    return answer