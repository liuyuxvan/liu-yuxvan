n,m=map(int,input().split())
min_num=min(n,m)
sum_fang=0
sum_zong=0
for i in range(1,min_num+1):
    sum_fang+=(n-i+1)*(m-i+1)
sum_zong=(n+1)*n/2*(m+1)*m/2-sum_fang
print(int(sum_fang),end=" ")
print(int(sum_zong),end=" ")