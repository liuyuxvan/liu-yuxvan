def calcu_double():
    n = int(input())
    l = list(map(int, input().split()))
    left,right=0,len(l)-1
    sumnum=0
    while left<right:
        if l[left]==l[right]:
            left+=1
            right-=1
        else:
            cnt=abs(l[left]-l[right])
            sumnum+=cnt
            if l[left]<l[right] and l[left-1]<l[right-1] :
                l[left]=min(cnt+l[left],l[right])
            elif l[left]>l[right] and l[left-1]>l[right-1] :
                l[right]=min(cnt+l[right],l[left])
            left += 1
            right -= 1
    return sumnum
print(calcu_double())


