# Uses python3
import sys

def get_fibonaccihuge(x,y):
    memo = {0:0, 1:1}

    def pisano(z):
        s=[]
        a=k=0
        b=1
        while (s[:k]!=s[k:] or k<1:s+=[a%z]):
            k=len(s)/2
            a,b=b,a+b
        return k
    
    def fib(n):
        fibList=[]
        
        for i in range(n):
            if i == 0:
                fibList.append(0)
            elif i == 1:
                fibList.append(1)
            else:
                fibList.append(fibList[i-1] + fibList[i-2])

        if len(fibList) == 0:
            return 0
        else:
            return fibList[n-1] + fibList[n-2]
    
    def calc_fib(n):

        if n in memo:
            return memo[n]
        else:
            res = fib(x % pisano(y))
            
        memo[n] = res
        
        return res
    
    return calc_fib(x)


def main():
    x,y = map(int,sys.stdin.readline().split())
    print(get_fibonaccihuge(x, y))

main()
