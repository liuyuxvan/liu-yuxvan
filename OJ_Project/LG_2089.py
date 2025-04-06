sum=0
n=int(input())
for a in range(1,4):
    for b in range(1, 4):
        for c in range(1, 4):
            for d in range(1, 4):
                for e in range(1, 4):
                    for f in range(1, 4):
                        for g in range(1, 4):
                            for h in range(1, 4):
                                for i in range(1, 4):
                                    for j in range(1, 4):
                                        if a+b+c+d+e+f+g+h+i+j==n:
                                            sum+=1
print(sum)
for a in range(1,4):
    for b in range(1, 4):
        for c in range(1, 4):
            for d in range(1, 4):
                for e in range(1, 4):
                    for f in range(1, 4):
                        for g in range(1, 4):
                            for h in range(1, 4):
                                for i in range(1, 4):
                                    for j in range(1, 4):
                                        if a+b+c+d+e+f+g+h+i+j==n:
                                            print(a,b,c,d,e,f,g,h,i,j)
