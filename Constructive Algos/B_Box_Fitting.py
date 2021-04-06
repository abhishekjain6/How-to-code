"""
https://codeforces.com/problemset/problem/1498/B

Hint: Use an Nlog(N) approach, and try to think of what special
properties powers of 2 have.
"""


from math import log2
for _ in range(int(input())):
    n,w=map(int,input().split())
    arr=list(map(int,input().split()))
    d={x:0 for x in range(21)}
    for x in arr:
        d[int(log2(x))]+=1
    c_w=w
    count=n
    h=1
    while(count>0):
        max_p=0
        flag=0
        for x in d.keys():
            if pow(2,x)<=c_w: 
                if d[x]>0:
                    max_p=pow(2,x)
                    k=x
                    flag=1
                    
                    
        if flag:
            d[k]-=1
            c_w-=max_p
            count-=1
        else:
            h+=1
            c_w=w
    print(h)