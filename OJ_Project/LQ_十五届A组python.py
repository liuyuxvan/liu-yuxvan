import os
import sys

# 请在此输入您的代码
def guess(x):
  if x <= 2:
    return False
  if x % 2 == 1:
    return True
  return guess(x / 2)

n = int(input())
li = input().split()
li = [int(x) for x in li]
count = 0
for i in range(n):
  if not guess(li[i]):
    count += 1

print(count)
