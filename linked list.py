
class node:
    def __init__(self,d):
        self.data=d
        self.next=None
n1=node(3)
n2=node(9)
n3=node(7)
n1.next=n2
n2.next=n3
print(n1.next)