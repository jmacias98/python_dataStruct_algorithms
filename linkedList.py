'''
This program implements stack algorithm without using linked-list concept.
It will store full names and phone numbers and print them in ascending order.
'''
class Node:  
    def __init__(self,data):  
        self.data = data  
        self.next = None
          
class SortList:  
    #Represent the head and tail of the singly linked list  
    def __init__(self):  
        self.head = None 
        self.tail = None  
          
    #addNode() will add a new node to the list  
    def addNode(self, data):  
        #Create a new node  
        newNode = Node(data)  
          
        #Checks if the list is empty  
        if(self.head == None):  
            #If list is empty, both head and tail will point to new node  
            self.head = newNode  
            self.tail = newNode 
        else:  
            #newNode will be added after tail such that tail's next will point to newNode  
            self.tail.next = newNode 
            #newNode will become new tail of the list  
            self.tail = newNode  
              
    #sortList() will sort nodes of the list in ascending order  
    def sortList(self):  
        #Node current will point to head  
        current = self.head  
        index = None 
          
        if(self.head == None):  
            return 
        else:  
            while(current != None):  
                #Node index will point to node next to current  
                index = current.next 
                  
                while(index != None):  
                    #If current node's data is greater than index's node data, swap the data between them  
                    if(current.data > index.data):  
                        temp = current.data  
                        current.data = index.data  
                        index.data = temp 
                    index = index.next 
                current = current.next
                  
    #display() will display all the nodes present in the list  
    def display(self):  
        #Node current will point to head  
        current = self.head
        if(self.head == None):  
            print("List is empty") 
            return;  
        while(current != None):  
            #Prints each node by incrementing pointer  
            print(current.data),  
            current = current.next 
        print()

def main():
    phones = SortList()
    names = SortList()
    names.display()
    print()
    #Adds data to the list  
    names.addNode("Tom Brady") 
    names.addNode("Al Capone")  
    names.addNode("John Cena")
    names.addNode("Alfred Molina")  
    names.addNode("Greg Hardy")
    names.addNode("Mark Henry")
    names.addNode("Eli Manning")
    phones.addNode(8141892000)
    phones.addNode(9752765398)
    phones.addNode(1982376701)
    phones.addNode(1863862002)
    phones.addNode(9870192871)
    phones.addNode(7781129018)
    phones.addNode(6308751728)

    
    #Displaying original list  
    print("Original Lists: ") 
    names.display() 
    phones.display()
    
    #Sorting list  
    names.sortList() 
    phones.sortList()
    
    #Displaying sorted list  
    print("Sorted Lists: ")
    names.display()
    phones.display()

main()

'''
List is empty

Original Lists:
Tom Brady
Al Capone
John Cena
Alfred Molina
Greg Hardy
Mark Henry
Eli Manning

8141892000
9752765398
1982376701
1863862002
9870192871
7781129018
6308751728

Sorted Lists:
Al Capone
Alfred Molina
Eli Manning
Greg Hardy
John Cena
Mark Henry
Tom Brady

1863862002
1982376701
6308751728
7781129018
8141892000
9752765398
9870192871
'''














