#PROGRAM TO REVERSE A LINKED LIST
#INPUT: 50 -> 60 -> 70 -> 80 -> None
#OUTPUT: 80 -> 70 -> 60 -> 50 -> None

#Creating a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Creating Linked List
class linkedList:
    def __init__(self):
        self.head = None

    #Reversing Linked List
    def reverse(self):
        current = self.head
        prev = None

        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        
    #Inserting a Linked List
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    #Printing the Linked List
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data, end = " -> ")
            temp = temp.next
        print (temp)

    
llist = linkedList()
llist.push(80)
llist.push(70)
llist.push(60)
llist.push(50)

print ("Linked List: ")
llist.printList()

print ("\nReversed Linked List: ")
llist.reverse()
llist.printList()
