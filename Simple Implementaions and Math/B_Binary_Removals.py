"""
https://codeforces.com/problemset/problem/1499/B
"""

def issort(a):
    for x in range(1,len(a)):
        if a[x]<a[x-1]:
            return(False)
    return(True)
for _ in range(int(input())):
    s=input().strip()
    n = len(s)
    l = n
    for i in range(1,n):
        if s[i] == s[i-1] == '1':
            l = i
            break
    r = -1
    for i in range(n-2,-1,-1):
        if s[i] == s[i+1] == '0':
            r = i
            break
    print('YES') if l >= r else print('NO')