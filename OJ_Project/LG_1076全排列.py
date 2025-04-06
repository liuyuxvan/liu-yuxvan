import os
import sys
n=int(input())
a=[0]*10
for i in range(1,n+1):
  a[i]=i
b=[0]*10
vis=[False]*10
def dfs(step):
  if step==n+1:
    for i in range(1,n+1):
      print("%5d"%b[i],end='')
    print()
    return
  for i in range(1,n+1):
    if vis[i]==False:
      b[step]=a[i]
      vis[i]=True
      dfs(step+1)
      vis[i]=False
dfs(1)





# 请在此输入您的代码