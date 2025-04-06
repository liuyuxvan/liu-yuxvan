n=int(input())
lan=list(map(int,input().split()))
hong=list(map(int,input().split()))
lan.sort()
hong.sort()
print(lan)
print(hong)
sum1=0
for i in range(n):
    for j in range(i+1):
        if lan[i]>hong[j]:
            sum1+=1
print(sum1)