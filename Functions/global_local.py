x=5

def foo():
    #x=3 local variable
    global x
    x+=10
    print('local variable:',x)

foo()
print('global variable:',x)

#if we need to use a variable in and out a function we should define global in functn
