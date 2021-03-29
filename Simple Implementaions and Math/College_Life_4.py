"""
https://www.codechef.com/MARCH21B/problems/COLGLF4
"""


for _ in range(int(input())):
    n,e,h,a,b,c=map(int,input().split())
    arr=[]
    ans=[]
    for x in range(n+2):
        arr.append(x)
    for m in range(n+1):
        val1=2*n-e-2*m
        idx1=0
        for x in range(len(arr)):
            if arr[x]>=val1:
                idx1=x
                break
        val2=h-3*m
        idx2=len(arr)
        for y in range(len(arr)):
            if arr[x]>val2:
                idx2=y-1
                break
        if c>a:
            k=idx1 if (idx1<(n-m)) else n-m
        else:
            k=idx2 if (idx2<(n-m)) else n-m
        o=n-k-m
        if(k+2*m >= 2*n-e and k+3*m <= h):
            ans.append(a*o+b*m+c*k)
    if len(ans)==0:
        print(-1)
    else:
        print(min(ans))
