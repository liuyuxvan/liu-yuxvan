N,K=map(int,input().split())
a=[]
for _ in range(N):
   ar1=list(map(int,input().split()))
   a.append(ar1)
def find(lengthen):
    ans = 0
    for length,high in a:
        ans += (length//lengthen)*(high//lengthen)
        if ans>=K:
            return True
    return False
left,right=0,100000
while left<=right:
    mid=(left+right)//2
    if find(mid):
        left=mid+1
    else:
        right=mid-1
print(right)
