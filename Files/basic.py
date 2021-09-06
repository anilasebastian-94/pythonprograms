#2 operations can be performed in files
#read ('r')
#write ('w')
f1=open('file1','r')   #f1 is the reference name
for i in f1:           #direct print(f1) will only give location and mode of operation of file
    print(i)           # so to print content of file using iteration
f1=open('file1','w')
f1.write('welcome to luminar')