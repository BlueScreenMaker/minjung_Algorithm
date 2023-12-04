n,m = map(int,input().split())
cards = list(map(int,input().split()))
cards = sorted(cards)
answer_list = []

for i in range(len(cards)) :
    for j in range(i+1,len(cards)) :
        for k in range(j+1,len(cards)) :
            if sum([cards[i],cards[j],cards[k]])<=m :
                answer_list.append(sum([cards[i],cards[j],cards[k]]))
print(max(answer_list))