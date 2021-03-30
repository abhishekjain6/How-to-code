"""
https://codeforces.com/contest/1498/problem/0
"""


def gcd(a,b):
    if a == 0 :
        return b
     
    return gcd(b%a, a)
def sod(x):
    p=[int(y) for y in str(x)]
    return(sum(p))
for _ in range(int(input())):
    n=int(input())
    while(True):
        if gcd(n,sod(n))!=1:
            print(n)
            break
        else:
            n+=1