def change(arr:list):
    if len(arr)%2!=0:
        return -1
    sum_L = 0
    sum_R = 0
    sum_U = 0
    sum_D = 0
    sum_acr = 0
    sum_iter = 0
    for i in arr:
        if i == 'L':
            sum_L += 1
        elif i == 'R':
            sum_R += 1
        elif i == 'U':
            sum_U += 1
        elif i == 'D':
            sum_D += 1
    sum_acr = abs(sum_L - sum_R)
    sum_iter = abs(sum_U - sum_D)
    return (sum_acr + sum_iter)//2
arr=list(input())
print(int(change(arr)))


