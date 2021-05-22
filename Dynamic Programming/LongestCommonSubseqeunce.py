"""
Given two strings, find the length of the longest common subsequence between them.
Example:
    LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
    LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""

def LCS(a,b):
    n,m=len(a),len(b)
    dp=[[0 for x in range(n+1)] for y in range(m+1)]
    for x in range(m+1):
        for y in range(n+1):
            if x==0 or y==0:
                dp[x][y]==0
            elif a[y-1]==b[x-1]:
                dp[x][y]=dp[x-1][y-1]+1
            else:
                dp[x][y]=max(dp[x][y-1],dp[x-1][y])
    return(dp[m][n])



n=input()
m=input()
print(LCS(n,m))