def fun(n):
    l=['0','1','2','5','6','8','9']
    if(all(i in l for i in list(str(n)))):
        return 1
    return 0
    
n=int(input())
i=1
c=0
while(i):
    if(fun(i)):
        c+=1
    if c==n:
        print(i)
        exit(0)
    i+=1
