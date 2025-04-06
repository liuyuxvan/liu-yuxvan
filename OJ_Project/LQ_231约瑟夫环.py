def upstair(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return upstair(n-1)+upstair(n-2)
n=int(input())
print(upstair(n))