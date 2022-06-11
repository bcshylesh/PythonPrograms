##fh=open("one.txt")
##c=0
##for i in fh:
##    print(i,end="")
##    c+=1
##print("Total Lines",c)
##fh.close()


fh=open("two.txt","w")
c=0
for i in range(5):
    fh.write(str(c))
    c+=1
fh.write("\nBCA")
fh.close()
