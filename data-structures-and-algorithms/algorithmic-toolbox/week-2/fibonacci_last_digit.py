# Uses python3
def calc_fib(n):
    fibList=[]
    
    for i in range(n):
        if i == 0:
            fibList.append(0)
        elif i == 1:
            fibList.append(1)
        else:
            fibList.append((fibList[i-1] + fibList[i-2]) % 10)

    if len(fibList) == 0:
        return 0
    elif len(fibList) == 1:
        return 1
    else:
        return (fibList[n-1] + fibList[n-2]) % 10

n = int(input())
print(calc_fib(n))
