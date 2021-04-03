"""
Given a string of uppercase alphabets, corresponding to columns
of a table, convert them to the column number. Eg: A-->1, AA-->27
BA-->53 and so on.

"""

s=input()
s=s[::-1]
d={chr(x):x-64 for x in range(65,91)}
p=0
ans=0
for t in s:
    ans+=(26**p*(d[t]))
    p+=1
print(ans)   