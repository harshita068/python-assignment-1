a=int(input("enter any number : "))
sum=0
while(a>0):
    x=int(a%10)
    sum=sum+x
    a=int(a/10)
print(sum)