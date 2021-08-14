

def segragate(l):

    
    a=[-1]*len(l)
    z,o,t=0,0,0
    for i in range(len(l)):
        if l[i]==0:
            z+=1
        if l[i]==1:
            o+=1
        if l[i]==2:
            t+=1
    k=0
    while z:
        a[k]=0
        k+=1
        z-=1

   
    while o:
        a[k]=1
        k+=1
        o-=1

   

    while t:
        a[k]=2
        k+=1
        t-=1

    for i in a:
        print(i,end=' ')


x=list(map(int,input().split()))
segragate(x)
