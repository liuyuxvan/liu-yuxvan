n=int(input())
sum=0
cnt=0
for i in range(1,n+1):
    for j in range(1,i+1):
        sum+=i
        cnt+=1
        if cnt==n:
            break
    if cnt == n:
        break
print(sum)

