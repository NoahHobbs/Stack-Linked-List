"""
Noah Hobbs
10/8/2020
"""
from ListEmptyException import ListEmptyException


class Node:

    # creates the nodes for the linked list
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None  # setting my head to none

    def size(self):
        """
        Gets the size of the stack
        :return: should
        """
        size = 0
        if self.is_empty():
            raise ListEmptyException('The list is empty')
        else:
            curr = self.head
            while curr:
                size += 1
                curr = curr.next
            return size

    def is_empty(self):
        """
        Used for my exception and for logic later in the program
        :return: Returns a boolean flag that will
        tell the program/user if the stack is empty
        """
        empty_flag = False
        if self.head is None:
            empty_flag = True
            return empty_flag
        else:
            return empty_flag

    def push(self, value_to_be_added):
        """
        This will add values to the top/head if head is empty simply add it
        otherwise we have to shift the current node over and add the new one
        to the head
        :param value_to_be_added: This is what will be added to the stack
        """
        if self.head is None:
            self.head = Node(value_to_be_added)

        else:
            new_node = Node(value_to_be_added)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        """
        Should remove the last entered values
        :return: if the list is empty raise the exception otherwise return
        the value that was popped from the stack
        """
        if self.is_empty():
            raise ListEmptyException('List is empty')

        else:
            removed_node = self.head
            self.head = self.head.next
            removed_node.next = None
            return removed_node.data

    def peek(self):
        """
        This function will allow you to look at the top of the linked stack
        without popping it
        :return: will return the value in the head or raise an exception
        """
        if self.is_empty():
            raise ListEmptyException('List is empty')

        else:
            return self.head.data

    def print(self):
        """
        This will just print out my stack
        :return: if the stack is empty raise the ListEmptyException otherwise
        print each value with some hyphens between
        """
        curr_node = self.head
        if self.is_empty():
            raise ListEmptyException('Stacked list is empty')
        else:

            while curr_node is not None:
                print(curr_node.data, "---", end=" ")
                curr_node = curr_node.next
            return


if __name__ == '__main__':
    # creating my stack
    my_stack_list = Stack()
    # testing is_empty()
    print(my_stack_list.is_empty())
    # pushing 5 values to my stack
    my_stack_list.push(66)
    my_stack_list.push(324)

    # testing my size method
    print(my_stack_list.size())
    # testing is_empty()
    print(my_stack_list.is_empty())
    my_stack_list.push(12)
    my_stack_list.push(999)
    my_stack_list.push(1)
    print(my_stack_list.size())
    # printing my stack before I pop
    my_stack_list.print()
    # peeking at the top value which should be the last value inserted
    print("\nTop of my stack -", my_stack_list.peek())
    # popping my two top values which should leave 12, 324 and 66 with the
    # values I pushed
    my_stack_list.pop()
    my_stack_list.pop()
    # testing my size method
    print(my_stack_list.size())
    # printing the values after pop
    my_stack_list.print()
    # peeking at my new top value which should be 12 with the order I pushed
    print("\nTop of my stack -", my_stack_list.peek())