"""
https://codeforces.com/contest/1506/problem/D
"""
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    l={}
    for x in arr:
        try:
            l[x]+=1
        except:
            l[x]=1
    if len(l.keys())==1:
        print(list(l.values())[0])
    else:
        sp=list(l.values())
        sp.sort(reverse=True)
        pos=1
        x=0
        while(x<len(sp) and pos<len(sp)):
            if sp[x]!=0:
                if sp[x]>=sp[pos]:
                    sp[x]-=sp[pos]
                    sp[pos]-=sp[pos]
                    pos+=1
                else:
                    sp[x]-=sp[x]
                    sp[pos]-=sp[pos]
                    x=pos+1
            else:
                x+=1
        
        print(max(n%2,sum(sp)))
