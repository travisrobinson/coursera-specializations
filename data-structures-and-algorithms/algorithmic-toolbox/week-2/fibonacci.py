# Uses python3
def calc_fib(n):
    fibList=[]
    
    for i in range(n):
        if i < 2:
            fibList.append(i)
        else:
            fibList.append(fibList[i-1] + fibList[i-2])

    if len(fibList) == 0:
        return 0
    elif len(fibList) < 3:
        return 1
    else:
        return fibList[n-1] + fibList[n-2]

n = int(input())
print(calc_fib(n))
