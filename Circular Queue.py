class MyCircularQueue:

    def __init__(self, k: int):
        self.q=[0]*k
        self.size=k
        self.head,self.cnt=0,0
    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.q[(self.head+self.cnt)%self.size]=value
        self.cnt+=1
        return True
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head=(self.head+1)%self.size
        self.cnt-=1
        return True
    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.q[(self.head+self.cnt-1)%self.size]

    def isEmpty(self) -> bool:
        return self.cnt==0
    def isFull(self) -> bool:
        return self.cnt==self.size

obj = MyCircularQueue(3)

# Add elements to the queue
param_1 = obj.enQueue(1)  # Returns True
param_2 = obj.enQueue(2)  # Returns True
param_3 = obj.enQueue(3)  # Returns True
param_4 = obj.enQueue(4)  # Returns False because the queue is full

# Get the last element
param_5 = obj.Rear()  # Returns 3

# Check if the queue is full
param_6 = obj.isFull()  # Returns True

# Remove an element from the queue
param_7 = obj.deQueue()  # Returns True

# Add another element to the queue
param_8 = obj.enQueue(4)  # Returns True

# Get the last element
param_9 = obj.Rear()  # Returns 4

# Get the front element
param_10 = obj.Front()  # Returns 2

# Check if the queue is empty
param_11 = obj.isEmpty()  # Returns False

# Print the results
print("enQueue(1):", param_1)
print("enQueue(2):", param_2)
print("enQueue(3):", param_3)
print("enQueue(4):", param_4)
print("Rear():", param_5)
print("isFull():", param_6)
print("deQueue():", param_7)
print("enQueue(4):", param_8)
print("Rear():", param_9)
print("Front():", param_10)
print("isEmpty():", param_11)
