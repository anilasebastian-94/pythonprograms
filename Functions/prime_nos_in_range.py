num1=int(input('enter lower range'))
num2=int(input('enter upper range'))
res=0
for a in range (num1,num2+1):
    if a>1:
        for i in range(2,a):
            if a%i==0 :
                break
        else:
            res+=a
print(res)

