#user defined functions
('''def add (n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
s=add(a,b)
print("Addition :",s)
print("Substraction: ",sub(a,b))
print("Multiplication : ",mul(a,b))
print("Division :",div(a,b))
 

#Captalize first letter of first and last name
def names():
    first_name =input("Enter first name : ")
    last_name=input("Enter last name: ")

    f_name=first_name.title()
    l_name=last_name.title()

    print("Candidates name is : ",f_name,l_name)

names()
 ''')

#Print even numbers in limit set by user
def print_even_numbers():
    n=int(input("Enter limit : "))
    e=[]
    for i in range(1,n+1):
        if (i%2==0):
            e.append(i)
    print("Even number in the range is : ",e)
print_even_numbers()
