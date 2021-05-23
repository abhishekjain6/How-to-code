"""
Implement a queue using stacks.

"""

class queue:
    def __init__(self):
        self.queue1=[]
        self.queue2=[]
    def enque(self,n):
        self.queue1.append(n)
    def deque(self):
        if len(self.queue2)==0:
            m=len(self.queue1)
            for x in range(m-1):
                self.queue2.append(self.queue1.pop())
            self.queue1.pop()
        else:
            self.queue2.pop()
    def show(self):
            print(*self.queue2[::-1],*self.queue1)
q=queue()
q.enque(10)
q.enque(15)
q.enque(25)
q.show()
q.deque()
q.enque(50)
q.show()
q.enque(100)
q.enque(130)
q.deque()
q.deque()
q.show()
