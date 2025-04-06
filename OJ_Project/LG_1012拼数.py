n=int(input())
arr=list(map(int, input().split()))
def first(a,b):
    return str(a)+str(b)>str(b)+str(a)
arr.sort(key=first,reverse=True)
str1=""
for i in arr:
    str1+=str(i)
print(int(str1))