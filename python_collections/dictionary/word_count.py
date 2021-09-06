count={}
data=input('enter data')
words=data.split(' ')
for word in words:
    if word not in count:
        count.update({word:1})
    else:
        val=int(count[word])
        val+=1
        count.update({word:val})
print(count)
# string='hello,hi,hello,hi'
# new=string.split(',')
# dict={}
# f1=0
# f2=0
# for i in new:
#     if i in new':
#         f1=f1+1
#         dict.update({i:f1})
#     else:
#         f2=f2+1
#         dict.update({'hi': f1})
# print(dict)

