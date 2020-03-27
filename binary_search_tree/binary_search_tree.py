from dll_stack import Stack
from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        # value at the current node
        self.value = value
        # reference to the nodes left child
        self.left = None
        # reference to the nodes right child
        self.right = None

    # Insert the given value into the tree

    def insert(self, value):
        # if the value being passed in the insert, is less than the value of the current node
        if value < self.value:
            # check to see if the node to its left exists
            if self.left is None:
                # if true,  create a new node for the left side of the tree
                self.left = BinarySearchTree(value)
            else:
                # else, insert a new node to compare to the current node
                self.left.insert(value)
        # if the value of the new node is >= the current node
        elif value >= self.value:
            # if a node to the right doesn't exist
            if self.right is None:
                # place that new value as the node to the right.
                self.right = BinarySearchTree(value)
            else:
                # else insert the new node to the right of the current node.
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # if node.value == self.target
        if self.value == target:
            #  return true
            return True
        # if the value is none, return false
        if self.value is None:
            return False
        else:
            # checks to see if the target is less than the current node
            if target < self.value:
                # if true, check to see if the next node to the left is not None
                if self.left is not None:
                    # recurse through the left side until the target returns true.
                    return self.left.contains(target)
            # checks to see if the target is >= the current node
            if target >= self.value:
                # if true, check to see if the next node to the right is not None
                if self.right is not None:
                    return self.right.contains(target)

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
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    # UNDERSTAND:
    #   IN ORDER = LNR : LEFT - NODE - RIGHT
    #       EXAMINES THE FIRST NODE, CHECKS LEFT UNTIL IT CAN'T GO LEFT (PRINT)
    def in_order_print(self, node):
        # PLAN
        # # If self.right and self.left is None: ---- if both left and right don't exist. print the current node
        # check if value is not empty.
        if self.value is not None:
            # if the left node is none, print it
            if self.left is None:
                print(self.value)
            # if the left node exists, run the function, and print the value.
            if self.left is not None:
                self.left.in_order_print(self.left)
                print(self.value)
            # if the left node exists, run the function. Don't print b/c we don't need it
            if self.right is not None:
                self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # FIFO
    def bft_print(self, node):
        # create a queue
        que = Queue()
        # add root to queue
        que.enqueue(node)
        # while queue is not empty:
        while que is not None:
            curr_node = que.dequeue()
            print(curr_node.value)
            if curr_node.left:
                que.enqueue(curr_node.left)
            if curr_node.right:
                que.enqueue(curr_node.right)
            # DO THE THING!! (PRINT)
            # add children of node to queue
            # pop node of queue
            #

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while len(stack) > 0:
            cur = stack.pop()
            print(cur.value)
            if cur.left:
                stack.push(cur.left)
            if cur.right:
                stack.push(cur.right)
        # create queue
        # add root to queue
        # while queue is not empty
        # node = pop top of stack
        # do the thing
        # add children of to the stack

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
bst.bft_print(bst)
