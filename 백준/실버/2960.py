def find_es(default_list,count) :
    s = default_list[0]
    new_list = default_list
    for ele in default_list :
        if ele%s == 0 :
            count+=1
            if count == k :
                return ele
            new_list.remove(ele)
    return find_es(new_list,count)

n,k = map(int,input().split())
num_list = [i for i in range(2,n+1)]
ans = find_es(num_list,0)
print(ans)