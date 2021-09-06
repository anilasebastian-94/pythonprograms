def fibanocci(n): # 0,1,2,3
    if n<=1:
        return n  #0,1
    else:
        return fibanocci(n-1) + fibanocci(n-2)
        #fib(1)+fib(0)=1, (fib(2)+fib(1))+fib(1)

nterms=10
for i in range (nterms):#0,1,2,3
    print(fibanocci(i))  #0,1,1,2