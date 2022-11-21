a=input()
b=input()
if len(b)>0:
    b=b[-1]
k=0
m=len(a)
n=len(b)
if ((m==0 and n==0) or n==0):
    print(k+1)
elif (m==0):
    print(k)
else:
    for i in range(m-n+1):
        if a[i:n+i]==b:
            k+=1
    print(k)
