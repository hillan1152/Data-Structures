""""
How do you find and return the middle node of a singly linked list in one pass? You do not have access to the length of the list. If the list is even, you should return the first of the two "middle" nodes. You may not store the nodes in another data structure.
""""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def middle(node):
        # have current value = midpoint
        curr_value = node
        end = node.next
        # create while loop that keeps track of 2 ahead (next next)
        while end is not None and end.next is not None:
            curr_value = curr_value.next
            end = end.next.next
        return curr_value
        # return midpoint value

    def reverse(node):
        curr = self.value
        next_num = curr.next
        prev = curr

        while next_num is not None:
            curr = prev
            next_num = curr
            ???


1 -> 2 -> 3 -> None
curr = 2
next_num = 2
prev = 2
