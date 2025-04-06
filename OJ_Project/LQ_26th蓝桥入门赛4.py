n=int(input())
sum1=0
M=10**9+7
for _ in range(n):
   a,b,c,d=map(int,input().split())
   d=pow(2,d,M-1)
   a = pow(a, d , M)
   b = pow(b, d , M)
   c = pow(c, d , M)
   print((a*b*c)%M)
