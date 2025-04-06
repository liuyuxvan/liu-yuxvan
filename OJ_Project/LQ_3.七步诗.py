import os
import sys
n, m = map(int,sys.stdin.readline().strip().split())
arr=[]
arr_bool=[[0 for _ in range(m)]for _ in range(n)]
for _ in range(n):
    arr.append(list(sys.stdin.readline().strip()))
sum_max=0

