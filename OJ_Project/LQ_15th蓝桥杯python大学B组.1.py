sum1=0
for i in range(1,2025):
    sum_2=0
    sum_4=0
    n=i
    while i:
        sum_2+=i%2
        i//=2
    while n:
        sum_4+=n%4
        n//=4
    if sum_2==sum_4:
        sum1+=1
print(sum1)
