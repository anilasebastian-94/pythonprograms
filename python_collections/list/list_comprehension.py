n=[1,2,3,4,5]
# s=[i*5 for i in n] #[first operation_for/if_other if inside loop]
# print(s)
odd=[]
even=[]
odd=[i for i in n if i%2!=0]
print(odd)
even=[i for i in n if i%2==0]
print(even)