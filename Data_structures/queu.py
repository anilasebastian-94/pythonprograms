#enqueue...addition
#dequeue....deletion
#fifo

q=[]
size=int(input('enter size of stack'))
front=0
rear=0
n=0
def enqueue():
    global size,front,rear,q
    if rear>=size:
        print('queue is full')
    else:
        p=int(input('enter element'))
        q.insert(rear,p)
        rear+=1

    for i in range(front,rear):
        print(q[i], end=' ')
def dequeue():
    global size,front,rear,q
    if rear==front:
        print('queue is empty')
    else:
        front+=1
        for i in range(front,rear):
            print(q[i],end =' ')
while n!=1:
    print('enter operation to perform')
    opt=int(input('press option:\n 1) enqueue\n 2) dequeue'))
    if opt==1:
        enqueue()
    elif opt==2:
        dequeue()
    n=int(input('\ndo you want to continue press 1 to exit'))