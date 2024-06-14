str1=str(input("enter first string : "))
str2=str(input("enter second string : "))
if(sorted(str1)==sorted(str2)):
    print("strings are anagram")
else:
    print("strings are not anagram")