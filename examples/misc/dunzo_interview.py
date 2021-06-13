#
#     def fizzBuzz(n):
#         for t in range(1,n):
#             if(t!=0 and t%3==0 and t%5==0):
#                 print("FizzBuzz")
#             elif( t!=0 and t%3==0 and t%5!=0):
#                 print("Fizz")
#             elif( t!=0 and t%3 !=0 and t%5==0):
#                 print("Buzz")
#             else:
#                 print(t)
#
# if __name__ == "__main__":
#    fizzBuzz(123)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Function to insert whole linked list in
# to another linked list at position k
def insert(head1, head2, k):
    # traverse the first linked list until k-th
    # point is reached
    count = 1
    curr = head1
    while (count < k):
        curr = curr.next
        count += 1

    # backup next node of the k-th point
    temp = curr.next

    # join second linked list at the kth point
    curr.next = head2

    # traverse the second linked list till end
    while (head2.next != None):
        head2 = head2.next

    # join the second part of the linked list
    # to the end
    head2.next = temp
    return head1


# Function to print linked list recursively
def printList(head):
    if (head == None):
        return

    # If head is not None, print current node
    # and recur for remaining list
    print(head.data, end=" ")
    printList(head.next)


""" Given a reference (pointer to pointer) to the head
of a list and an int, insert a new node on the front
of the list. """


def push(head_ref, new_data):
    new_node = Node(0)
    new_node.data = new_data
    new_node.next = (head_ref)
    (head_ref) = new_node
    return head_ref


# Driver Code
if __name__ == "__main__":
    """ The constructed linked lists are :
    a: 1.2.3.4.5
    b: 7.8.9.10.11 """
    a = None
    b = None
    k = 2

    # first linked list
    a = push(a, 5)
    a = push(a, 4)
    a = push(a, 3)
    a = push(a, 2)
    a = push(a, 1)


    # second linked list
    b = push(b, 11)
    b = push(b, 10)
    b = push(b, 9)
    b = push(b, 8)
    b = push(b, 7)

    printList(a)
    print(">>>>>>")
    print(a.data)
    print(a.head)
    print(type(a))

    printList(b)

    a = insert(a, b, k)

    print("\nResulting linked list\t", end=" ");
    printList(a)

# This code is contributed by Arnab Kundu