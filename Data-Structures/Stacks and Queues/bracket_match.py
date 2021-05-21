"""
Write a program to check if the entered bracket string is valid or not.
Valid: (()()((())))
Invalid: ())()      //(unmatched paranthesis)
"""

s=input()
#arr=[x for x in s]
stack=[]
ans="Valid"
for x in s:
    if x=="(":
        stack.append("(")
    elif x=="{":
        stack.append("{")
    elif x=="[":
        stack.append("[")
    elif len(stack)!=0 and x==")":
        if stack[-1]=="(":
            stack.pop()
        else:
            ans="Not Valid"
            break
    elif x=="}":
        if  len(stack)!=0 and stack[-1]=="{":
            stack.pop()
        else:
            ans="Not Valid"
            break
    elif x=="]":
        if len(stack)!=0 and stack[-1]=="[":
            stack.pop()
        else:
            ans="Not Valid"
            break    
print(ans)
