class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Inserting a node at the beginning of a list
    def insert_front(self, data):
        # creates a new node for the list, floating in the ether
        new_node = Node(data)
        if not self.head:
            self.tail = new_node

        val = self.head.data
        
        if not self.head.next:
            self.tail = None
        
        self.head = self.head.next
        return val
        # "next" defaults to none, so now we're reassigning the next position to the current head (the currently existing node)
        new_node.next = self.head
        # Now that we've redefined the "next" to the next piece, we're reassigning the head to be the newly created node.
        self.head = new_node

    # Inserting a node at the end of a list
    def insert_end(self, data):
        new_node = Node(data)
        if not self.tail:
            self.tail = new_node
            self.head = new_node
        else:
            # Save the old tail
            old_tail = self.tail
            # Set the tail to the new end
            self.tail = new_node

            old_tail.next = new_node

    def delete_front(self):
        # Takes the first entity, the "head" of the list, and reassigns the head to the next entity, removing the current head from the list.
        if not self.head:
            print('No list')
            return
        
        if not self.head.next:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.next

    def delete_end(self):
        if not self.head:
            print('There is no list to delete from.')
            return None
        current = self.head

        # Store the value of the data being deleted
        val = self.tail.data

        # Determine whether or not there is only one element. If there is...
        if not current.next:
            # Head & Tail become nothing. Meaning, there is nothing here.
            self.head = None
            self.tail = None
        else:
            # Count up to the second-to-last item
            while current.next != self.tail:
                current = current.next

            # Reassign the tail, set the last element to null
            self.tail = current
            current.next = None
        # Return the value being deleted.
        return val

    def delete_at(self, position):
        if not self.head:
            print('There is no list to delete from')
            return
        if position == 0:
            self.delete_front()
            return
        current = self.head
        for i in range(position - 1):
            if not current:
                print(f'Not a valid position: {position}')
                return
            current = current.next
        # Check to see if we're at the end of the list
        if not current.next:
            self.delete_end()
        else:
            current.next = current.next.next


    def insert_at(self, data, position):
        # This handles if the position provided was at the front of the list. Simply handle as an insert_front.
        if position == 0:
            self.insert_front(data)
            return
        current = self.head
        # For loop that terminates at the index directly before the index called by position
        for i in range(position - 1):
            if not current:
                print(f'failed to insert at position {position}')
                return
            current = current.next
        
        if not current.next:
            self.insert_end(data)
        else:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node


    def print_list(self):
        this_list = []
        current = self.head
        if current:
            while current:
                this_list.append(current.data)
                current = current.next
            print(this_list)

    def length(self):
        length = 1
        current = self.head
        if current:
            while current.next:
                length += 1
                current = current.next
            return length
        else:
            return 'No Length'


# Tests below


my_list = LinkedList()
print('List length should be empty: ', my_list.length())
my_list.print_list()
my_list.insert_front(3)
my_list.insert_front(2)
my_list.insert_front(1)
my_list.insert_end(4)
my_list.insert_end(5)
my_list.insert_end(6)
my_list.insert_end('banana')
my_list.insert_at(10, 1)
print('List length should be 8: ', my_list.length())
my_list.print_list()
my_list.delete_front()
my_list.delete_end()
my_list.delete_end()
print('List length should be 5:', my_list.length())
my_list.print_list()
my_list.delete_end()
my_list.delete_end()
print('List length should be 3: ', my_list.length())
my_list.print_list()
my_list.delete_end()
my_list.delete_end()
my_list.delete_end()
print('List length should be empty: ', my_list.length())
my_list.print_list()
my_list.insert_front(1)
my_list.insert_at(10, 10)
print('List length should be 1:', my_list.length())
my_list.print_list()
# Additional tests
my_list.insert_end(2)
my_list.insert_end(3)
my_list.insert_end(4)
print('List length should be 4:', my_list.length())
my_list.print_list()
my_list.insert_at(10, 0) # insert at front
my_list.insert_at(11, 1) # insert in middle
my_list.insert_at(12, 6) # insert at end
my_list.insert_at(13, 9) # fail to insert past end
print('List length should be 7:', my_list.length())
my_list.print_list()
my_list.delete_at(0) # delete front
my_list.delete_at(1) # delete in middle
my_list.delete_at(4) # delete end
my_list.delete_at(8) # fail to delete past end
my_list.print_list()