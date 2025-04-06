n=int(input())
arr=list(map(int,input().split()))
m=len(arr)
sum1=0
for i in range(m//2):
    while arr[i]!=arr[m-1-i]:
        if arr[i]<arr[m-1-i]:
            arr[i]+=1
            sum1+=1
        else:
            arr[m-1-i]+=1
            sum1+=1
print(sum1)
