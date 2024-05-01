
class node:
    def __init__(self,d):
        self.data=d
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.head=None
        
    def add_node(self,val):
        new_node=node(val)
        if(self.head == None):
            self.head=new_node
        else:
            traveller=self.head
            while(traveller.next != None):
                traveller=traveller.next
            traveller.next=new_node
            new_node.prev=traveller
            
    def traverse(self):
        traveller=self.head
        while(traveller.next != None):
            print(traveller.data)
            traveller=traveller.next
        print(traveller.data)
        
    def delete_node(self):
        traveller=self.head
        prev=self.head
        while(traveller.next != None):
            prev=traveller
            traveller=traveller.next
        prev.next=None
        
    def __init__(self):
        self.head=None
        
    def delete_node_at_first(self):
        self.head=self.head.next
        
    def add_node_at_first(self):
        new_node=node(2)
        temp=self.head
        self.head=new_node
        self.head.next=temp
        
            
             
LL1=LL()
LL1.add_node(3)
LL1.add_node(8)
LL1.add_node(6)
LL1.add_node(1)
LL1.traverse()
LL1.delete_node()
LL1.traverse()
LL1.delete_node_at_first()
LL1.traverse()
LL1.add_node_at_first()
LL1.traverse()




        
        
        
    
        
 
 
 
 
 
 





        
    