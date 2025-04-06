n,m,p=map(int,input().split())
l=True
for a in range(1,10):
    for b in range(1, 10):
        if b==a:
            continue
        for c in range(1, 10):
            if c==a or c==b:
                continue
            for d in range(1, 10):
                if d == a or d == b or d==c :
                    continue
                for e in range(1, 10):
                    if e==d or e==c or e==b or e==a:
                        continue
                    for f in range(1, 10):
                        if f==e or f==d or f==c or f==b or f==a:
                            continue
                        for g in range(1, 10):
                            if g==f or g == e or g == d or g == c or g == b or g == a:
                                continue
                            for h in range(1, 10):
                                if h==g or h==f or h == e or h == d or h == c or h == b or h == a:
                                    continue
                                for i in range(1, 10):
                                    if i==h or i == g or i == f or i == e or i == d or i == c or i == b or i == a:
                                        continue
                                    if (a*100+b*10+c*1)*m==(d*100+e*10+f*1)*n and (a*100+b*10+c*1)*p==(g*100+h*10+i*1)*n:
                                        print(a*100+b*10+c*1,d*100+e*10+f*1,g*100+h*10+i*1)
                                        l=False
if l:
    print("No!!!")