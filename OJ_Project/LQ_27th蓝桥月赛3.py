n=int(input())
sum1=0
diff=[]
for i in range(n):
    a,b=map(int,input().split())
    sum1+=b
    diff.append(a-b)
diff.sort(reverse=True)
for i in range(n//2):
    sum1+=diff[i]
print(sum1)