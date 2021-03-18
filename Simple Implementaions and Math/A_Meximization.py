"""
https://codeforces.com/contest/1497/problem/A

"""

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=[]
    ansseq=[]
    for x in sorted(arr):
        if str(x) not in ans:
            ans.append(str(x))
        else:
            ansseq.append(str(x))
    print(" ".join(ans)+" "+" ".join(ansseq))
     