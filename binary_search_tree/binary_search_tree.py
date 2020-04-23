from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = value
        if new_node >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(new_node)
            else:
                self.right.insert(new_node)
        elif new_node < self.value:
            if self.left is None:
                self.left = BinarySearchTree(new_node)
            else:
                self.left.insert(new_node)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        curr_num = self.value
        if target == curr_num:
            return True
        if self.left is None and self.right is None:
            return False
        if target > self.value:
            return self.right.contains(target)
        else:
            return self.left.contains(target)
    # Return the maximum value found in the tree

    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right is not None:
            self.right.for_each(cb)
        if self.left is not None:
            self.left.for_each(cb)
    # Why didn't return work?
    # What happened with elif self.left...

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
