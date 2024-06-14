str1=str(input("enter any string : "))


'''freq={}
for i in str1:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)'''

char=input("enter the character : ")
freq=str1.count(char)
if char in str1:
    print(char ,"is ocuuring ",freq ,"times in string ")
else:
    print("character is not present")
    