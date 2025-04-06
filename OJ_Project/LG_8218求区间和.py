n=int(input())
arr=[0]+list(map(int,input().split()))
arr_sum=[0]*(n+2)
arr_sum[1]=arr[1]
for i in range(1,n+1):
    arr_sum[i]=arr_sum[i-1]+arr[i]
m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    arr[i]=arr_sum[b]-arr_sum[a-1]
for i in range(m):
    print(arr[i])