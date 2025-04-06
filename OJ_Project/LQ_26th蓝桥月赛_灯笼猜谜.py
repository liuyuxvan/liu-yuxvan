n,m=map(int,input().split())
index=1
num=0
for i in range(1,n+1):
    L,R=map(int,input().split())
    if index<L:
        num+=L-index
        index=L
    if index>R:
        num+=index-R
        index=R
print(num)