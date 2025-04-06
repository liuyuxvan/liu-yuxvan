n=int(input())
arr=list(map(int,input().split()))
sum=[0]*(n+1)
ans=10**18
for i in range(1,n+1):
    sum[i]=sum[i-1]+arr[i-1]
for i in range(1,n+1):
    ans=min(ans,max(sum[i],sum[n]-sum[i]))
print(ans)