from collections import deque

dq=deque([])
print("Dequeue: \n 1.Insert element(From right)\n 2.Insert element(From left)\n 3.Remove element(From right)\n 4.Remove element(From left)\n 5.Display\n 6.Exit\n")

while True:
    print("Enter choice: ",end="")
    chce  = int(input())
    if chce == 1:
        print("Enter the number you want to insert in deque from right: ",end=" ")
        n=int(input())
        dq.append(n)
        print(dq)
        
    elif chce == 2:
        print("Enter the number that you want to insert in deque from left: ",end=" ")
        n=int(input())
        dq.appendleft(n)
        print(dq)
    elif chce == 3:
        print("Removed Element from right: ",dq[-1])
        dq.pop()
        print(dq)
    elif chce == 4:
        print("Removed Element from left: ",dq[0])
        dq.popleft()
        print(dq)
    elif chce == 5:
        print(dq)
    else:
      print("LOL")
      break
      exit()
