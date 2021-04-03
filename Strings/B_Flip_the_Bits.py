for _ in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    if a==b:
        print("YES")
    else:
        psum=[0 for x in range(n+1)]
        for x in range(n):
            if a[x]=='1':
                psum[x+1]=psum[x]+1
            else:
                psum[x+1]=psum[x]-1
        ans=1
        st=0
        for x in range(n-1,-1,-1):
            if (not st and a[x]==b[x]) or (st and a[x]!=b[x]):
                continue
            elif psum[x+1]==0:
                if st==0:
                    st=1
                else:
                    st=0
            else:
                ans=0
                break
        if ans:
            print("YES")
        else:
            print("No")