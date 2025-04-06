N,K=map(int,input().split())
arr=list(map(int,input().split()))
sum1=0
arr.sort()
for i in range(N//2):
    sum1+=arr[i]
print(sum1)