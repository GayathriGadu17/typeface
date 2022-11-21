n=int(input())
a=[]
while n>0:
    a.append(n%3)
    n=n//3
print(*a[::-1],sep='')
