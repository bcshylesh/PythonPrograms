#  [23,5,3,5,34,23,32,45,6]
##input : number
##output:  Present or Not
s=int(input("[23,5,3,5,34,23,32,45,6] Enter the serach number:"))
for i in [23,5,3,5,34,23,32,45,6]:
    if (i==s):
        print(s,"is Present in the list")
        break
else:
    print(s,"not in the list")
