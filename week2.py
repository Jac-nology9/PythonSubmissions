#Create empty list
my_list = []
print(my_list)

#Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#Insert the value 15 at the second position
my_list.insert(1, 15)
print(my_list)

#Extend my_list
my_list.extend([50, 60, 70])
print(my_list)

#Remove last element 
my_list.pop()
print(my_list)

#Sort my_list in ascending order
my_list.sort()
print(my_list)

#Find and print index of the value 30 
index_of_30 = my_list.index(30)
#print("Sorted list:", my_list)
print("Index of 30:", index_of_30)
