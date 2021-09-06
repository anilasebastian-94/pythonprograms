dict={1:10,2:20,3:30,4:40,5:50}
# e= int(input('enter key'))
# if e in dict:
#     print('element found')
# else :
#     print('not found')
def is_key_present(x):
    if x in dict:
        print('element',x,'found')
    else:
        print('element',x,'not found')
is_key_present(4)
is_key_present(9)