m,n = map(int,input().split())
chess = []
for i in range(m) :
    chess.append(input())
size = 8
counts = []

for i in range(m-7) :
    for j in range(n-7) :
        case1 = 0
        case2 = 0
        for k in range(i,i+size) :
            for u in range(j,j+size) :
                if (k+u)%2 == 0 : #색 분기
                    if chess[k][u] == "B" :
                        case1+=1
                    else :
                        case2+=1
                else :
                    if chess[k][u] == "B" :
                        case2+=1
                    else :
                        case1+=1
        counts.append(min(case1,case2))
print(min(counts))