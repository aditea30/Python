#converting multiple input from user into list

n=int(input("Enter the number of items to be inputed into list : \n"))
list=[]
for i in range(1,n):
    a=input("Enter items -")
    list.append(a)
print(list)
