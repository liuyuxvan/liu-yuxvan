n=int(input())
x=0
y=0
arr_y=[]
sum=0
for i in range(n):
    x,y=map(int, input().split())
    arr_y.append(y)
arr_y.sort()
if n%2==0:
    for i in range(n):
        sum+=abs(arr_y[i]-arr_y[n//2])
else:
    for i in range(n):
        sum+=abs(arr_y[i]-arr_y[n//2])
print(sum)