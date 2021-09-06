my_string=input('enter string')
bad_string='!@#$%^''{}[]\&"*()_+<>?:;,./'
no_punctuaions=''
for char in my_string:
    if char not in bad_string :
        no_punctuaions = no_punctuaions+char

print(no_punctuaions)

    