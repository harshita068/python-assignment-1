str1=str(input("enter any string : "))
char=input("enter the character : ")
freq=str1.count(char)
if char in str1:
    print(char ,"is ocuuring ",freq ,"times in string ")
else:
    print("character is not present")
    