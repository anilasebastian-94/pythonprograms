count={}
f1=open('count','r')
for n in f1:
    #print(word)
    wr=n.split(' ')
    # print(w)

    for word in wr:
        if word not in count:
            count.update({word:1})
        else:
            val=int(count[word])
            val+=1
            count.update({word:val})
print(count)