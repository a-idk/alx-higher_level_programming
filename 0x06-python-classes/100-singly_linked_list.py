#!/usr/bin/python3

'''
a class Node that defines a node of a singly linked list

@a_idk scripting
'''


class Node:
    ''' class node definition '''
    def __init__(self, data, next_node=None):
        ''' Initializing the class '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        ''' data getter '''
        return self.__data

    @data.setter
    def data(self, value):
        ''' data setter '''
        if not isinstance(value, int):
            # print out message
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        ''' node getter '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        ''' node setter '''
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


'''
write a class SinglyLinkedList that defines a singly linked list
'''


class SinglyLinkedList:
    ''' class SinglyLinkedList definition '''
    def __init__(self):
        ''' initializing the class '''
        self.__head = None

    def __str__(self):
        """ String class object """
        tmp = self.__head
        nodal_printer = []
        while tmp:
            nodal_printer.sort()
            nodal_printer.append(str(tmp.data))
            tmp = tmp.next_node
        nodal_printer.sort(key=int)
        return "\n".join(nodal_printer)

    def sorted_insert(self, value):
        ''' singly linked properties '''
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            new_node.data = value
            new_node.next_node = self.__head
            self.__head = new_node
