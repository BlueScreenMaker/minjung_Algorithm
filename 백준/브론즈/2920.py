ment = ['ascending','descending','mixed']
num_list = list(map(int,input().split()))

if num_list == sorted(num_list) :
    print(ment[0])
elif num_list == sorted(num_list,reverse=True) :
    print(ment[1])
else :
    print(ment[2])