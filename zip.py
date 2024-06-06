#Zip method helps to work on more than 1 list at a time
l1=[1,3,5,7,9]
l2=['January','March','May','July','September']
for a,b in zip(l1,l2):
    print(a ,b,"\n")
#Without using zip
t=len(l1)
for i in range(t):
    print(l1[i],l2[i])