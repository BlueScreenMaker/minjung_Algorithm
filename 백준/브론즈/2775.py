def solution(a,b) :
    if a == 1 :
        print(sum(b))
    else :
        newFloor = [0]*len(b)
        for i in range(len(b)) :
            newFloor[i] = sum(b[0:i+1])
        solution(a-1,newFloor)


t = int(input())
for i in range(t) :
    a = int(input())
    b = int(input())
    b = [i for i in range(1,b+1)]
    solution(a,b)