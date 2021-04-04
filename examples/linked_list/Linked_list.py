# from ..linked_list.Node import Node
# from .Node import *
# !/usr/bin/env python3
from examples.linked_list.Node import Node


class LinkedList:
    def __init__(self):
        self.start_node = None

    def traverse(self):
        print("Inside traverse function")
        if self.start_node is None:
            print(">>>>>>> List is empty")
        else:
            n = self.start_node
            while n is not None:
                print(n.item)
                n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is not None:
            n = self.start_node
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
        else:
            self.start_node = new_node

    def insert_at_item(self, x, data):
        n = self.start_node
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("Item is not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def merge_list(self,at,andAt,first_list,list_to_be):
        # n = self.start_node
        n1= first_list.start_node
        n2= list_to_be.start_node
        temp_Node_1 = Node("")
        temp_Node_2 = Node("")
        previous_node = Node("")

        # while n1 is not None:
        #     if n1.item == at:
        #         temp_Node_1.item = n1.item
        #         temp_Node_1.ref = n1.ref
        #
        #         break
        #     n1 = n1.
        # while n1 is not None:
        #     print(">>>>>")
        #     if n1.item == at:
        #         temp_Node_1.item = n1.item
        #         temp_Node_1.ref = n1.ref
        #         print(n1.item)
        #         break
        #     elif n1.item == andAt:
        #         temp_Node_2.item = n1.item
        #         temp_Node_2.ref = n1.ref
        #         print(n1.item)
        #         break
        #     n1 = n1.ref
        #
        #
        # if n1 is None:
        #     print("Item is not in the list")
        # else:
        #     print("elseeeee")
        #     print(n1.item)
        #     list_to_be.traverse()

        # while n1 is not None:
        #     if n1.item == at:
        #         temp_Node_1.item = n1.item
        #         temp_Node_1.ref = n1.ref
        #         print(temp_Node_1.item)
        #     elif n1.item == andAt:
        #         temp_Node_2.item = n1.item
        #         temp_Node_2.ref = n1.ref
        #         print(temp_Node_2.item)
        #
        #     n1 = n1.ref
        # while n1 is not None:
        #     if n1.item == at:
        #         break
        #     n1 = n1.ref
        # if n1 is None:
        #     print("Item is not in the list")
        # else:
        #     n1.ref = n2
####### works partially
        # while n1 is not None:
        #     print(n1.item)
        #     if n1.item == at:
        #         previous_node.ref = n2
        #
        #     if n1.item == andAt:
        #         temp_Node_2.ref = n1.ref
        #         temp_Node_2.item = n1.item
        #         # print("??????")
        #         # print(temp_Node_2.item)
        #         # print(temp_Node_2.ref.item)
        #     if n1.ref == None:
        #         print("Bhooommmm")
        #         print(temp_Node_2.item)
        #         n1.ref = temp_Node_2.ref
        #         break
        #
        #     previous_node = n1
        #     n1 = n1.ref
######## secon half works
        # while n1 is not None:
        #     if n1.item == andAt:
        #         temp_Node_2.ref = n1.ref
        #         temp_Node_2.item = n1.item
        #     n1 = n1.ref
        #
        # while n1 is not None:
        #     print(n1.item)
        #     if n1.item == at:
        #         previous_node.ref = n2
        #
        # while n2 is not None:
        #     if n2.ref == None:
        #         n2.ref = temp_Node_2.ref
        #         break
        #
        #     previous_node = n1
        #     n2 = n2.ref

        ###############
        while n1 is not None:
            print(n1.item)
            if n1.item == at:
                previous_node.ref = n2

            if n1.item == andAt:
                temp_Node_2.ref = n1.ref
                temp_Node_2.item = n1.item
                # print("??????")
                # print(temp_Node_2.item)
                # print(temp_Node_2.ref.item)
            if n1.ref == None:
                print("Bhooommmm")
                print(temp_Node_2.item)
                n1.ref = temp_Node_2.ref
                break

            previous_node = n1
            n1 = n1.ref


        print(">>>>>>>>>> Done <<<<<<<")
        # first_list.traverse()


if __name__ == '__main__':
    new_linked_list = LinkedList()
    new_linked_list_to_be_merged = LinkedList()

    new_linked_list.insert_at_start('a')
    new_linked_list.insert_at_start('b')
    new_linked_list.insert_at_start('c')
    # print(new_linked_list.start_node.item)
    new_linked_list.insert_at_end('1')
    new_linked_list.insert_at_end('2')
    new_linked_list.insert_at_end('3')
    new_linked_list.insert_at_item('2',"dummy1")
    new_linked_list.insert_at_item('2',"dummy2")
    new_linked_list.insert_at_end('4')
    new_linked_list.insert_at_end('5')

    new_linked_list_to_be_merged.insert_at_end('x')
    new_linked_list_to_be_merged.insert_at_end('y')
    new_linked_list_to_be_merged.insert_at_end('z')

    # new_linked_list.traverse()
    # print("==================")
    new_linked_list.merge_list("dummy2","dummy1",new_linked_list,new_linked_list_to_be_merged)
    new_linked_list.traverse()
    # new_linked_list_to_be_merged.traverse()

