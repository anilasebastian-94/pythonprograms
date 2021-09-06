my_string=input('enter string') #apple
c=''
for i in my_string: #a,p,p
    if i not in c: #true,true,false
        c=c+i      #c=ap
    else:
        print('first recursive character is', i) #p
        break