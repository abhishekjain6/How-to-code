"""
Given a number n, find the shortest valid roman expression 
for n.
Input: N
Output: String
"""

n=int(input())
ans=[]
while(n>0):
    if n>=1000:
        ans.append("M")
        n-=1000
    elif n>=500:
        ans.append("D")
        n-=500
    elif n>=100:
        ans.append("C")
        n-=100
    elif n>=50:
        ans.append("L")
        n-=50
    elif n>=10:
        ans.append("X")
        n-=10
    elif n>=5:
        ans.append("V")
        n-=5
    else:
        ans.append("I"*n)
        n=0
print("".join(ans))