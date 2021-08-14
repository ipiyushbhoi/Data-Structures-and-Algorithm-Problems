

def sortbinary(l):

    a=[-1]*len(l)
    z=0
    for i in range(len(l)):
        if l[i]==0:
            z+=1

    k=0
    while z:
        a[k]=0
        k+=1
        z-=1
        
    while k<len(l):
        a[k]=1
        k+=1

    print(z)
    for i in a:
        print(i,end=' ')


x=list(map(int,input().split()))
sortbinary(x)
