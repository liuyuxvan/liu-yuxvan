import os
import sys
def is_prime(n):
    if n <= 1:
        return False
    # 确定性基数组覆盖 n < 2^64
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in bases:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in bases:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
m=int(input())
if m==2:
  sum=1
else:
  sum=0
for i in range(1,m+1):
  if m%i==0 and is_prime(i):
    sum+=1
print(sum)











