import math
n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))
def is_prime(num):
    """判断一个数是否为素数"""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(2))