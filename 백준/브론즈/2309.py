mini = []
for i in range(9) :
    mini.append(int(input()))
mini = sorted(mini)

remove_sum = sum(mini) - 100 #난쟁이들의 키합 -> 100, 9명중 2명을 뺀다
remove_index = []

for i in range(9) :
    for j in range(i+1,9) :
        if mini[i] + mini[j] == remove_sum and len(remove_index) < 2 :
            remove_index.append(i)
            remove_index.append(j)

del mini[remove_index[1]]
del mini[remove_index[0]]

for i in mini :
    print(i)