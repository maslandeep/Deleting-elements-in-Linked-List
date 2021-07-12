# Deleting all elements in LinkedList

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList: 

    def __init__(self):
        self.head = None
        
    def push(self):
        current = None
        current.next = self.head
        self.head = current
        
    def deleteList(self):

        current = self.head
        
        while(current):
            print(current)
            prev = current
            current = current.next
            del prev.data
            
            
    def push(self,new_data):
        
        new_node = Node(new_data)
        
        new_node.next = self.head
        
        self.head = new_node
        
        
        
# Use push() to construct below  
# list 1-> 12-> 1-> 4-> 1   
if __name__ == '__main__': 
  
    llist = LinkedList() 
    llist.push(1) 
    llist.push(4) 
    llist.push(1) 
    llist.push(12) 
    llist.push(1) 
  
  
    print("Deleting linked list") 
    llist.deleteList() 
        
        