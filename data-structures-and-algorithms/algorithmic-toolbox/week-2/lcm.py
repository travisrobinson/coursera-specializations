# Uses python3
import sys

def gcd(a, b):
    while b!= 0:
        (a,b) = (b,a%b)
    return a


def main():
    a,b = map(int,sys.stdin.readline().split())
    c = gcd(a, b)
    d = (a*b)//c
    print(d)

main()
