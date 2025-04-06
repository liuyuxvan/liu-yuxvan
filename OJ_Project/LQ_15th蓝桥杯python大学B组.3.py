import os
import sys
n=int(input())
arr=list(map(int,input().split()))
sum1=0
def is_two(n):
    return n > 0 and (n & (n - 1)) == 0
for m in arr:
    if is_two(m):
        sum1+=1
print(sum1)
# 请在此输入您的代码