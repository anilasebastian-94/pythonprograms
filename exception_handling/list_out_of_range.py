lst=[1,2,3,4,5,6]
n=int(input('enter index of element'))
try:
    print(lst[n])
except:
    print('list out of range exception occured')