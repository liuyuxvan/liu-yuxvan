import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
n = int(input())
if n==1:
    print(1)
elif n==2:
    print(2)
else:
    for i in range(2, int(math.sqrt(n))+1):
        if is_prime(i) and n%i==0 and is_prime(n//i):
            print(int(max(i,n//i)))
            break
