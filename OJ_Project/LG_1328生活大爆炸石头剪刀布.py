n,m,p=map(int,input().split())
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
sum_A=0
sum_B=0
s_a=0
s_b=0
guess_arr=[[0,-1,1,1,-1],
           [1,0,-1,1,-1],
           [-1,1,0,-1,1],
           [-1,-1,1,0,1],
           [1,1,-1,-1,0]]
for i in range(n):
    if s_a>=m:
        s_a=0
    if s_b>=p:
        s_b=0
    if guess_arr[arr1[s_a]][arr2[s_b]]==1:
        sum_A+=1
    elif guess_arr[arr1[s_a]][arr2[s_b]]==-1:
        sum_B+=1
    s_a+=1
    s_b+=1
print(sum_A,end=" ")
print(sum_B,end=" ")



