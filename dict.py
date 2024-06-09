#dictionary 
'''d={'1':{'class':'8','fees':'8000'},'3':'March'}
for r in d['1']['class']:
    print(r)'''

#set functions
s=(2,5,34,78)
s1=set(s)
print(s1)
s1.add(72)
print(s1)
s1.pop()
print(s1)#pops the first element
s1.remove(34)#gives an error if item to be removed does'nt exsist
print(s1)
s1.discard(2)#does'nt give an error
print(s1)