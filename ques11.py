n=int(input("enter value of n : "))
i=1
a=0
b=1
print(a)
print(b)
while(i<=n):
    next=a+b
    print(next)
    a=b
    b=next
    i+=1