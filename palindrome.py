##Program to read a string and check whether 
##Palindrome or not
##Python -- Non Palindrome
##malayalam -palindrome
##12321
##0123210
s=input("Enter a String :")
r=""
for i in range(1,len(s)+1):
    r=r+s[-i]
    
if (s==r):
    print(s, "is a Palindrome")
else:
    print(s, "is Not a Palindrome")
