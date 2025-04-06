n,k=map(int,input().split())
cnt=0
def dfs(x,sum1,u):
    global cnt
    if u==k:
        if sum1==n:cnt+=1
        return
    for i in range(x,int((n-sum1)/(k-u))+1):
        dfs(i,sum1+i,u+1)
dfs(1,0,0)
print(cnt)