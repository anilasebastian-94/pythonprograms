
#...................................List out of range............

# lst=[1,2,3,4,5,6,7]
# n=int(input('enter index'))
# try:
#     print(lst[n])
# except Exception as e:
#     print(e.args)         #output is inthe form of tuple ('list index out of range',)


#.....................................Division...................................
n1=int(input('enter first number'))
n2=int(input('enter secnd number'))
try:
    res=n1/n2
    print(res)
except Exception as e:
    print(e.args)
