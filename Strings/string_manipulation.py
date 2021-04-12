"""
Write a program that takes an integer n and return the 
kth integer in the look and say sequence.
Input:
SIngle line, 2 numbers, n and k
n<100
k<10^5

"""

n,k=map(int,input().split())
c=[int(x) for x in str(n)]
for x in range(k):
    print(c)
    s=(c[0])
    cnt=0
    ans=[]
    for x in range(len(c)):
        #print(c)
        #print(s)
        if c[x]==s:
            cnt+=1
            if x==len(c)-1:
                #print("a")
                ans.append(cnt)
                ans.append(s)
                #print(ans)

        else:
            ans.append(cnt)
            ans.append(s)
            #print(cnt)
            cnt=1
            try:
                s=c[x]
            except:
                continue
    try:
        if c[-1]!=c[-2]:
            ans.append(1)
            ans.append(c[-1])
    except:
        c=ans[:]
        continue
    c=ans[:]
print(*ans)
