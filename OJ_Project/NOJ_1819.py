size,high= map(int,input().split())
arr = [[0 for _ in range(size+1)] for _ in range(size+1)]
num1=0
num2=0
d = [[0 for _ in range(size+1)] for _ in range(size+1)]
for i in range(size):
    num1,num2=map(int,input().split())
    d[num1]+=1
    d[num2+1]-=1
d[0][0]=arr[0][0]
