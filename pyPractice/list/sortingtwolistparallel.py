list1 = [2,4,3,5,7]
list2 = [20,40,30,50,70]
data = zip(list1, list2)

list1, list2 =  zip(*sorted(zip(list1,list2)))

print(list1)

print(list2)