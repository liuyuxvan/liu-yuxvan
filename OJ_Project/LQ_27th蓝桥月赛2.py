arr=list(input())
sum_len=0
sum_l=0
sum_a=0
sum_n=0
length=len(arr)
arr_l=[0 for _ in range(length)]
arr_a=[0 for _ in range(length)]
arr_n=[0 for _ in range(length)]
for i in range(length-1,-1,-1):
    if arr[i]=='n':
        sum_n+=1
    elif arr[i]=='a':
        sum_a+=sum_n
    elif arr[i]=='l':
        sum_l+=sum_a
    arr_n[i] = sum_n
    arr_l[i]=sum_l
    arr_a[i] = sum_a
print(arr_l[0])
