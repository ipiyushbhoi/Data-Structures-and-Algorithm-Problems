
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

row=len(mat)

col=len(mat[0])


k=0
l=0


while k<row and l<col:

    for i in range(col):
        print(mat[k][i],end=' ')

    k+=1

    for i in range(k,row):
        print(mat[i][col-1],end=' ')

    col-=1

    if k<row:
        for i in reversed(range(l,col-1)):
            print(mat[row-1][i],end=' ')
        row-=1

    if l<col:
        for i in reversed(range(k,row-1)):
            print(mat[i][l],end=' ')

        l+=1
    

    



    

    
