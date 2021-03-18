"""
https://codeforces.com/contest/1497/problem/B

"""



for _ in range(int(input())):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    mod={}
    ans=0
    for x in arr:
        if x%m==0:
            ans=1
        else:
            try:
                mod[x%m]+=1
            except:
                mod[x%m]=1
    b=0
    l=list(mod.keys())
    while b<len(mod.keys()):
        #print(mod)
        a=l[b]
        if mod[a]!=0:
            try:
                if mod[a]==mod[m-a]:
                    ans+=1
                    mod[a]=0
                    mod[m-a]=0
                else:
                    k=min(mod[a],mod[m-a])+1
                    ans+=1
                    mod[a]-=min(mod[a],k)
                    mod[m-a]-=min(mod[m-a],k)
                    ans+=(mod[a] or mod[m-a])
                    mod[a],mod[m-a]=0,0
            except:
                ans+=mod[a]
                mod[a]=0
        #print(mod)
        b+=1
    print(ans)