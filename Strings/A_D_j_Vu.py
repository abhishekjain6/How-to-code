def is_palindrome(s):
    return s == s[::-1]
for _ in range(int(input())):
    s=input()
    c=0
    for t in s:
        if t!="a":
            c+=1
    if c==0:
        print("NO")
    elif is_palindrome("a"+s):
        print("YES")
        print(s+"a")
    else:
        print("YES")
        print("a"+s)
        