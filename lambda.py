('''lambda functions
1.takes any number of arguments
2.takes only 1 expression
3.No loop
4.no return statement it returns implicitly
examples ----''')

('''e_or_o=(lambda x :'even' if x%2==0 else 'odd')
a=e_or_o(6)
print(a)

s=(lambda x,b :x+b)
a=int(input("Enter number : "))
b=int(input("Enter number : "))
print(s(a,b))

s1=(lambda : int(input("Enter number 1 : "))+ int(input("Enter number 2 : ")))
print(s1())

p=lambda x: [i**2 for i in x]
print(p([1,2,3,4]))
''')

#Sort products
dict=[{'names ': 'laptop','price':'56000'},
      {'name':"Mercedes",'price':'20000000'}]
s=sorted(dict, key = lambda x:x['price'] )
print(s)
