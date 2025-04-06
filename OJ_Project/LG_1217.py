import math
import sys

# 快速输入


# 快速输出

def check(n):
    if 1000<=n<=9999 or 100000<=n<=999999 or 10000000<=n<=99999999:
        return True
    else:
        return False
def huiwen(n):
        n=str(n)
        if n==n[::-1]:
            return True
        else:
            return False
def zhishu(n):
    if n==1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n, m = map(int, sys.stdin.readline().split())
if n==2:
    sys.stdout.write(f"{n}\n")
if n%2==0:
    n+=1
for i in range(n,m+1,2):
    if  check(i):
        continue
    if  huiwen(i):
        if zhishu(i):
            sys.stdout.write(f"{i}\n")

