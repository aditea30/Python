#Stack using python 
S=[]
top=None
def isEmpty(stk):
    if (stk==[]):
        return True
    else:
        return False
    
def push(stk,item):
    stk.append(item)
    top=len(stk)-1
    
def  s_pop(stk):
    if isEmpty(stk):
        return ('Underflow')
    else:
        i=stk.pop()
        
    return i
def peek(stk):
    if isEmpty(stk):
        return('Underflow')
    else:
        top=len(stk)-1
    return stk[top]
    
def display(stk):
    if isEmpty(stk):
        return('Underflow')
    else:
        top=len(stk)-1
        print(stk[top],'<---top')
        for p in range(top-1,-1,-1):
            print(stk[p])
    
while True:
    n=int(input('''
    1. Push
    2.Pop
    3.Peek
    4.Display
    5.Exit '''))

    if n==1:
        item=int(input("Enter item : "))
        push(S,item)
        print("%d item added successfully ",S)
        input("press key to continue..")

    elif n==2:
        item=s_pop(S)
        if (item=='Underflow'):
            print("Stack is empty")
        else:
            print("Popped element : ",item)
        input("press key to continue..")

    elif n==3:
        item=peek(S)
        if (item=='Underflow'):
            print("Stack is empty")
        else :
            print("First element is %d ",item)
        input("press key to continue..")

    elif n==4:
        display(S)
        input("press key to continue..")

    elif n==5:
        break

    else:
        print("Invalid input")


