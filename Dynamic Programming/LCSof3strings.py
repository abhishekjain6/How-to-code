"""
Given 3 strings, find the length of the longest common subsequnece between them

"""



def LCS(a,b,c):
    n,m,l=len(a),len(b),len(c)
    dp=[[[0 for x in range(n+1)]for y in range(m+1)]for z in range(l+1)]
    for x in range(l+1):
        for y in range(m+1):
            for z in range(n+1):
                if x==0 or y==0 or z==0:
                    dp[x][y][z]=0
                elif a[z-1]==b[y-1] and b[y-1]==c[x-1]:
                    dp[x][y][z]=dp[x-1][y-1][z-1]+1
                else:
                    dp[x][y][z]=max(max(dp[x-1][y][z],dp[x][y-1][z]),dp[x][y][z-1])
    return(dp[l][m][n])



a,b,c=input(),input(),input()
print(LCS(a,b,c))