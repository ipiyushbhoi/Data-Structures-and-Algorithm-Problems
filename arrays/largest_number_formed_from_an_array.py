


def largestnumber(arr):

    A = sorted(arr,key=lambda x:str(x)*10,reverse=True)
    print(''.join([str(i)for i in A]))



arr = list(map(int,input().split()))
largestnumber(arr)

    
