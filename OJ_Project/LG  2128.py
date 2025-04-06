N=100002
arr=[0]*N
cnt=[0]*N
d=[0]*N
arr_len=int(input())
arr[1:arr_len+1]=list(map(int,input().split()))
m=int(input())
ans1=0
ans2=0
for _ in range(m):
    Left,Right=map(int,input().split())
    d[Left]+=1
    d[Right+1]-=1
cnt[0]=d[0]
for i in range(1,arr_len+1):
  cnt[i]=cnt[i-1]+d[i]
for i in range(1,arr_len+1):
    ans1+=arr[i]*cnt[i]
arr=sorted(arr[1:arr_len+1])
cnt=sorted(cnt[1:arr_len+1])
for i in range(0,arr_len):
    ans2+=arr[i]*cnt[i]
print(ans2-ans1)