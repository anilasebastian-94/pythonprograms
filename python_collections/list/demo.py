#keep order
#support duplicate elements
#heterogenious
#nesting possible
#list is mutable
# a=[1,2,3,4,0,4]
# print(a)
# print(type(a))
#  for i in a:
#     print(i)
# b=[1,2,3,'hai',True,7.8]
# print(b)
b=[]
#...................................Adding elements...............
b.append(8)
b.append(9)
b.append('hai')
print(b)
#..................................nesting possible...............
lst=[1,2,3,[4,5,6,[7,8,9]]]
print(lst)
#..................................list is mutable..................
lst1=[1,2,3]
lst1.append(4)
print(lst1)
lst1.remove(4)
print(lst1)
lst1.clear
print(lst1)
