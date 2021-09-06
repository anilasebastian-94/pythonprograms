my_string=input('enter string')
vowels='aeiouAEIOU'
count=0
for i in my_string:
    if i in vowels :
        count=count+1
print(count)