n=int(input())
arr=[[0 for i in range(n+1)] for j in range(n+1)]
for i in range(1,n+1):
    arr[i]=[0]+list(map(int, input().split()))
sum_a=[[0 for i in range(n+1)] for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        sum_a[i][j] = arr[i][j] + sum_a[i - 1][j] + sum_a[i][j - 1] - sum_a[i - 1][j - 1]
max_a=0
for i in range(1,n+1):
    for j in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                if a<i or b<j :
                    continue
                max_a=max(max_a,sum_a[a][b]-sum_a[i-1][b]-sum_a[a][j-1]+sum_a[i-1][j-1])
print(max_a)