a=int(input("enter first number : "))
b=int(input("enter second number : "))
ch=int(input("enter your choice : "))
if ch==1:
    print(a ,"+ ",b ,"= ",a+b)
elif ch==2:
    print(a ,"- ",b ,"= ",a-b)
elif ch==3:
    print(a ,"X ",b ,"= ",a*b)
elif ch==4:
    print(a ,"/ ",b ,"= ",a/b)
else:
    print("your choice is wrong ")