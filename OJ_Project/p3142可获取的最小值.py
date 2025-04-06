n,k=map(int,input().split())
b=list(map(int,input().split()))
a=[0]+sorted(b)
s=[0]*(n+1)
for i in range(1,n+1):s[i]=s[i-1]+a[i]
ans=10**18
for p in range(1,k+1):
  ans=min(s[n]-s[n+p-k]+s[2*p],ans)
print(ans)