n,c=map(int,input().split())
a=[]
for i in range(n):
    w,v=map(int,input().split())
    p=v/w
    a.append((w,v,p))
a.sort(key=lambda x:x[2],reverse=True)
sum=0.0
for i in range(n):
    if c>=a[i][0]:
        sum+=a[i][1]
        c-=a[i][0]
    else:
        sum+=c*a[i][2]
        break
print('%.2f'%sum)
