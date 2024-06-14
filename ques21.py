l=[1,2,3,4,4,4,"hii","bye",True]
element=4
occ=l.count(element)
if element in l:
    print(element ,"occurs ",occ ,"times in the list")
else:
    print("element is not present ")