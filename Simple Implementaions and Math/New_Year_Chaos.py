"""
https://www.hackerrank.com/challenges/new-year-chaos/problem
"""

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    flag=1
    for y in range(n):
        if l[y]-y-1>2:
            print("Too chaotic")
            flag=0
            break
        for j in range(max(l[y]-2,0),y):
            if l[j]>l[y]-1:
                c+=1
    if flag:
        print(c)