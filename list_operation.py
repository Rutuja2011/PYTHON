#slip3_1
#List Operation: Concatenation,iteration, nestedlist, extend,append.

# Original list
li = [10, 20, 30, 40]
print("Original List li:", li)

# Concatenation 
list1 = [11, 22, 33]
list2 = [10, 20, 30]
concatenated_list = list1 + list2
print("Concatenated List:", concatenated_list)

# Nested list 
nested_list = [[10, 20, 30], ['aa', 'gg']]
print("Nested List:", nested_list)

# Iteration
l4 = [10, 40, 90]
print("Iterating over l4:")
for i in l4:
    print(i)

# Append 
l4.append(50)
print("After Append :", l4)

# Extend (adds all elements from another list)
s1 = ['pen', 'pencil']
s2 = ['apple', 'notebook']
s1.extend(s2)
print("After Extend:", s1)

