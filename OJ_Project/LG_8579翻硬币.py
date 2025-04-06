arr1=list(input())
arr2=list(input())
sum1=0
for i in range(len(arr1)):
    if arr1[i]!=arr2[i]:
        sum1+=1
        if arr1[i+1]=='*':
            arr1[i+1]='o'
        else:
            arr1[i+1]='*'
print(sum1)
