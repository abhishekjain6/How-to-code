"""
https://codeforces.com/contest/1506/problem/B
"""


for _ in range(int(input())):
    n,k=map(int,input().split())
    s=[x for x in input()]
    c=0
    for x in range(n):
        if s[x]=="*":
            idx=x
            c+=1
            break
    for y in range(n-1,-1,-1):
        if s[y]=="*":
            idx1=y
            if idx1!=idx:
                c+=1
            break
    #print(idx,idx1)
    cidx=idx+k
    while cidx<idx1:
        
        cidx=idx+k
        #print(cidx)
        if cidx>=idx1:
            break
        for x in range(cidx,idx-1,-1):
            if s[x]=="*":
                s[x]="x"
                idx=x
                c+=1
                break
    print(c)
