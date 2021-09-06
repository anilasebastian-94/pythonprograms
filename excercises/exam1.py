n1=int(input('enter lower range'))
n2=int(input('enter upper range'))
s=n2
# for i in range(1,n1):
#     s=s*10+s
#     print(s,end='')
#     print('\r')
for k in range(s):
    for i in range (n2):
        for j in range(i+1):
              print(k,end='')
               s=s+2

        print('\r')