
list1 = [3,5,6,7,1,4,6]
list2 = [1,9,0,4,7]

if(len(list1)==len(list2)):
    print("Lists are of same length")
else:
    print("Lists are not of same length")
if(sum(list1)==sum(list2)):
    print("Lists are of same sum")
else:
    print("Lists are not of same sum")

list3 = [value for value in list1 if value in list2]
print("Common values : "+str(list3))