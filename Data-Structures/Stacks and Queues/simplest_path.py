"""
Given a path to a file or folder, simplify it to make it the shortest.
"""

n=input().split("/")
ans=[]
if n[0]=="":
    ans.append("/")
    p=True
for x in n:
    if x!='' and x!=".." and x!=".":
        ans.append(x)

    if x=="..":
        k=ans.pop()
        if k=="/":
            raise "Illegal Argument"
if p:
    print("/"+"/".join(ans[1:]))
else:
    print("/".join(ans))