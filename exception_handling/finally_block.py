lst=[1,2,3,4,5,6,7]
n=int(input('enter index'))
try:
    print(lst[n])
except:
    print('index doesnot exist')
finally:
    print('inside finally')