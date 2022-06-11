##program to find the fequency of words in a sentence
##
##string="this is a value of a value"
#this:1, is:1,a:2,value:2
##
##read a string
##list of words --> use split function of string
##create a dictionary with words and frequency
s=input("Enter a sentence :")
words=s.split()
d=dict()
for w in words:
    d[w]=d.get(w,0)+1
print(d)
for i,j in d.items():
    if (j==max(d.values())):
        print("Most frequently used word is",i)
