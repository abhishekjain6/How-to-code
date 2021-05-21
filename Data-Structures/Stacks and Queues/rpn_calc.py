"""
A simple stack based approcah has been used to solve the given probelm.
We remove the immediate two elements to the absolute left the operator we encounter and 
use the operator on these two operations.
Time Complexity:O(n) for a RPN expression of length n
Memory Complexity:O(n+d) for a RPN expression of length n and d opperators
Please enter the RPN string with a ',' separator. It handles addition, subtraction,
multiplication, division and power operators.
"""





while True:
    s=input()
    if s=="quit":
        break
    else:
        s=s.split(",")
    arr=[]
    import operator
    op={'+':operator.add,'-':operator.sub,'/':operator.truediv,"*":operator.mul,"^":operator.pow}
    for x in range(len(s)):
        if s[x] in op:
            try:
                  a=float(arr.pop())
                  b=float(arr.pop())
                  arr.append(op[s[x]](b,a))
            except IndexError:
                  break
        else:
            arr.append(s[x])       
    if len(arr)!=1:
        print("Invalid RPN expression")
    else:
        print("Answer :"+str(arr.pop()))