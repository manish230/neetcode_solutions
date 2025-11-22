class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_first(self, data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        ltr = self.head
        while ltr.next:
            ltr=ltr.next
        ltr.next = Node(data,None)


    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        
        llstr= ''
        ltr = self.head
        while ltr:
            
            llstr += str(ltr.data) + "-->"
            ltr = ltr.next
        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_first(10)
    ll.insert_at_first(89)
    ll.insert_at_first(5)
    ll.insert_at_end(15)
    ll.print()

