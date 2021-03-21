for t in range(int(input())):
    r,c=map(int,input().split())
    arr=[]
    ans=0
    for x in range(r):
        arr.append(list(map(int,input().split())))
    vert={}
    horz={}
    mat=[[0 for p in range(c)] for j in range(r)]
    mat2=[[0 for p in range(c)] for j in range(r)]
    #print(mat)
    for i in range(r):
        for j in range(c):
            l=0
            rt=0
            if arr[i][j]==1:
                if j!=0:
                    for m in range(j,-1,-1):
                        if arr[i][m]==1:
                            l+=1
                        else:
                            break
                if j!=c-1:
                    for n in range(j,c):
                        if arr[i][n]==1:
                         rt+=1
                        else:
                            break
            mat[i][j]=[l,rt]
    # for i in mat:
    #     print(i)
    
    for i in range(r):
        for j in range(c):
            #print(i,j)
            u,d=0,0
            if mat[i][j][0]>=2 or mat[i][j][1]>=2:    
                
                if i!=0:
                        for m in range(i,-1,-1):
                            if arr[m][j]==1:
                                u+=1
                            else:
                                break
                if i!=r-1:
                        for n in range(i,r):
                            if arr[n][j]==1:
                                d+=1
                            else:
                                break
                l=mat[i][j][0]
                rt=mat[i][j][1]
                if mat[i][j][0]>=2:
                    
                    for k in range(2,l+1):
                        if u>=k*2:
                            ans+=1
                        if d>=k*2:
                            ans+=1
                if mat[i][j][1]>=2:
                    
                    for k in range(2,rt+1):
                        if u>=k*2:
                            ans+=1
                        if d>=k*2:
                            ans+=1
                if u>=2:
                    for k in range(2,l+1):
                        if l>=k*2:
                            ans+=1
                    for k in range(2,rt+1):
                        if rt>=k*2:
                            ans+=1
                if d>=2:
                    for k in range(2,l+1):
                        if l>=k*2:
                            ans+=1
                    for k in range(2,rt+1):
                        if rt>=k*2:
                            ans+=1
    print("Case #"+ str(t+1)+": "+str(ans))
                                
    
    
    #         mat2[i][j]=[u,d]
    # for i in mat2:
    #     print(i)

                        