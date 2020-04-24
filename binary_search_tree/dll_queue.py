from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if not self.storage.head:
            return
        self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        return self.size

    # def __repr__(self):
    #     return f"{self.size}"


# q = Queue()
# q.enqueue(5)
# print(q)