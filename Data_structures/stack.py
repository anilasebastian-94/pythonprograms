stk=[]
size=int(input('enter size of stack'))
n=0
top=0
def push():
    global top,size
    if top>size:
        print('stack is full')
    else:
        p=int(input('enter element to push'))
        stk.append(p)
        top+=1
def pop():
    global top,size
    if top<=0:
        print('stack is empty ')
    else:
        stk.pop()
        top-=1
def display():
    print(stk)
while n!=1:
    print('enter the operation to perfoem')
    opt=int(input('press 1) push 2) pop 3) display'))
    if (opt==1):
        push()
    elif (opt==2):
        pop()
    elif (opt==3):
        display()
    n=int(input('do you want to continue. press 1 to exit'))