# Q 1
def findmax():
    a=int(input(" Enter your  1 number "))
    b=int(input(" Enter your 2 number "))
    c=int(input(" Enter your 3 number"))
    y=max(a,b,c)
    print("the greatest number is",y)
# findmax()

# Q 2
def sumofnumbers():
    loaf=[]
    a = int(input(" Enter the number of numbers you want to add"))
    b = 0
    while(b < a):
        b=b+1
        c = int(input(" Type a number"))
        loaf.append(c)
    print(sum(loaf))
#sumofnumbers()        

# Q 4
def multiplicationofnumbers():
    loa=[]
    a = int(input(" Enter the number of numbers you want to multiply"))
    for e in range(0,a):
        f=int(input(" Type a number"))
        loa.append(f)
    mul=1
    for item in loa:
       mul=mul*item
    print(mul) 
# multiplicationofnumbers() 

# Q 4  
def reversestring():
    z = input(" give me a string ")
    reversestring=""
    length=len(z)
    for cool in range (length-1,-1,-1):
        reversestring=reversestring+(z[cool])+" "
    print(reversestring.upper())
reversestring()        