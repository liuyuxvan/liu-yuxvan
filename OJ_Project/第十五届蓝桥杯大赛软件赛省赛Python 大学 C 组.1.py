sum1=0
a=[]
try:
    while True:
        a1, b1, c1 = input().split()
        c1 = int(c1)
        if a1==b1  :
            a.append(c1)
except:
    a1=0
for i in range(len(a)-1):
    if a[i+1]-a[i]<=1000:
        sum1+=1
print(sum1)



