#queue using python
Q=[]
F=None
R=None
def isEmpty(que):
    if(que==[]):
        return True
    else:
        return False
    
def enqueue(que,i):
    que.append(i)
    if (len(que)==1):
        f=r=0
    else:
        r=len(que)-1

def dequeue(que):
    if isEmpty(que):
        print("Queue is empty")
    elif (len(que)==0):
        f=r=None
    else:
        i=que.pop(0)
        print("Dequeued elemet is ",i)

def peek(que):
    if isEmpty(que):
        print("Queue is empty")
    else:
        f=0
        print("Front element is ",que[f])

def display(que):
    if isEmpty(que):
        print("Queue is empty")
    elif (len(que)==1):
        print(que[0],'<---Front','<---Rear')
    else:
        f=0
        r=len(que)-1
        print(que[f],' <--Front')
        for i in (1,r):
            print(que[i])
        print(que[r]," <--Rear")
    
while True :
    n=int(input('''Enter your choice 
    1.Enqueue
    2.Dequeue
    3.Peek
    4.Display
    5.Exit'''))

    if n==1:
        i=int(input("Enter item"))
        enqueue(Q,i)
        print("Queue :",Q)
        input("press any key to continue...")
    elif n==2:
        i=dequeue(Q)
        print("Remaining queue ",Q)
        input("press any key to continue...")
    elif n==3:
        peek(Q)
        input("press any key to continue...")
    elif n==4:
        display(Q)
        input("press any key to continue...")
    elif n==5:
        break
    else:
        print("Invalid")