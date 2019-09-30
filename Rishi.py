# Rishi
a=int(input("Enter the n.o="))
fact=1
if(a<0):
    print("Factorial of negative n.o doesnot exist")
elif(a==0):
    print("Factorial of 0 is 1")
else:
    for i in range(1,a+1):
        fact=fact*i
    print("Factorial of",a,"is:-",fact)
