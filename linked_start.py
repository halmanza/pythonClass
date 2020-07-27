# Linked list example

# Node Class

class Node(object):
    def __init__(self,val):
        self.val=val
        self.next=None

    def get_data(self):
        return self.val

    def set_data(self,val):
        self.val=val
    
    def get_next(self):
        return self.next
    
    def set_next(self,next):
        self.next= next

class LinkedList(object):
    def __init__(self, head=None):
        self.head=head
        self.count=0
    def get_count(self):
        return self.count
    def insert(self,data):
        new_node=Node(data) 
        new_node.set_next(self.head)
        self.head= new_node
        self.count += 1 

    def find(self,val):

        item=self.head
        while (item != None):
            if item.get_data()== val:
                return item
            else:
                item=item.get_next()

        return None  
    def deleteat(self,idx):

        if idx > self.count-1:
            return
    def dump_list(self):
        tempnode=self.head
        while(tempnode != None):
            print("None: ", tempnode.get_data())
            tempnode= tempnode.get_next()

# create a liknked list and insert some items

itemsList=LinkedList()
itemsList.insert(38)
itemsList.insert(49)
itemsList.insert(13)
itemsList.insert(15)
itemsList.dump_list()

# exercise the list
print("Item count: ",itemsList.get_count())
print("Finding Item: ",itemsList.find(13))
print("Finding item: ",itemsList.find(78))
