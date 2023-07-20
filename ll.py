# Python3 program to partition a
# linked list around a given value.

# Link list Node
class Node:
    def __init__(self):
        self.data = 0
        self.next = None

# A utility function to create a new node


def newNode(data):

    new_node = Node()
    new_node.data = data
    new_node.next = None
    return new_node

# Function to make two separate lists and return
# head after concatenating


def partition(head, x):

    # Let us initialize first and last nodes of
    # three linked lists
    # 1) Linked list of values smaller than x.
    # 2) Linked list of values equal to x.
    # 3) Linked list of values greater than x.
    smallerHead = None
    smallerLast = None
    greaterLast = None
    greaterHead = None
    equalHead = None
    equalLast = None

    # Now iterate original list and connect nodes
    # of appropriate linked lists.
    while (head != None):

        # If current node is equal to x, append it
        # to the list of x values
        if (head.data == x):

            if (equalHead == None):
                equalHead = equalLast = head
            else:

                equalLast.next = head
                equalLast = equalLast.next

        # If current node is less than X, append
        # it to the list of smaller values
        elif (head.data < x):

            if (smallerHead == None):
                smallerLast = smallerHead = head
            else:

                smallerLast.next = head
                smallerLast = head

        else:
            # Append to the list of greater values

            if (greaterHead == None):
                greaterLast = greaterHead = head
            else:

                greaterLast.next = head
                greaterLast = head

        head = head.next

    # Fix end of greater linked list to None if this
    # list has some nodes
    if (greaterLast != None):
        greaterLast.next = None

    # Connect three lists

    # If smaller list is empty
    if (smallerHead == None):

        if (equalHead == None):
            return greaterHead
        equalLast.next = greaterHead
        return equalHead

    # If smaller list is not empty
    # and equal list is empty
    if (equalHead == None):

        smallerLast.next = greaterHead
        return smallerHead

    # If both smaller and equal list
    # are non-empty
    smallerLast.next = equalHead
    equalLast.next = greaterHead
    return smallerHead

# Function to print linked list


def printList(head):

    temp = head
    while (temp != None):

        print(temp.data, end=" ")
        temp = temp.next

# Driver code


# Start with the empty list
head = newNode(10)
head.next = newNode(4)
head.next.next = newNode(5)
head.next.next.next = newNode(30)
head.next.next.next.next = newNode(2)
head.next.next.next.next.next = newNode(50)

x = 3
head = partition(head, x)
printList(head)

# This code is contributed by Arnab Kundu.
