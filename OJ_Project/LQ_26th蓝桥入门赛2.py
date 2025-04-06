n=int(input())
str1=list(input())
str2=list(input())
str1_0=0
str1_1=0
str2_0=0
str2_1=0
for i in range(len(str1)):
    if str1[i]=='0':
        str1_0+=1
    else:
        str1_1+=1
for i in range(len(str2)):
    if str2[i]=='0':
        str2_0+=1
    else:
        str2_1+=1
print(min(str1_0,str2_1)+min(str1_1,str2_0))