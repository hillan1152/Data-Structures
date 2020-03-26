from doubly_linked_list import DoublyLinkedList
# INPUTS VS OUTPUTS

# INPUT = DOUBLY LINK LIST OF KEY, VALUE PAIRS
# OUTPUT = A CACHE OF 10 USED ITEMS FROM THAT LIST


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        # current number of nodes holding (length)
        self.size = 0
        # doubly linked list holds the key-value entries in the correct order
        self.dll = DoublyLinkedList()
        # storage dict that provides fast access
        self.storage = {}
        self.limit = limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    #   THE KEY GIVES ACCESS TO THE QUICK ENTRIES WITHIN THE LIST

    #   WHEN YOU GET A NODE BY ITS KEY, IT WILL MOVE TO THE FRONT OF THE LIST
    #       IF IT'S NOT THE STORAGE HEAD: ADD TO THE STORAGE HEAD
    #           RETURNING

    def get(self, key):
        # key, values within storage?
        if key in self.storage:
            # puts key-value at head of storage
            node = self.storage[key]
            self.dll.move_to_end(node)
            print(node.value)
            return node.value[1]
        else:
            return None
        # does the key exist
        # returns value of associated key OR None
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    # UNDERSTAND:
    #   ADDING A NEW KEY TO THE CACHE
    #   THIS WILL MAKE THE NEW NODE THE HEAD OF THE LIST AND BUMP EVERYTHING DOWN.

    # PLAN
    # IF STORAGE IS NOT SELF.LIMIT
    #   ADD TO HEAD
    # ELIF STORAGE IS SELF.LIMIT
    #   DELETE THE TAIL
    #   ADD NEW NODE TO HEAD

    def set(self, key, value):
        # if key exists, move to head
        # new_node = (key, value)
        if key in self.storage:
            # move to the front
            node = self.storage[key]
            node.value = (key, value)
            # puts key-value at head of storage
            self.dll.move_to_end(node)
            return

        # if the storage is greater than the limit (10)
        if self.size == self.limit:
            # create new node variable to replace old head
            # new_node = (key, value)
            del self.storage[self.dll.head.value[0]]
            # remove the head
            self.dll.remove_from_head()
            self.size += 1
            # add new node to tail
        self.dll.add_to_tail((key, value))
        self.storage[key] = self.dll.tail
        self.size += 1
        # if storage is not full, add to head
        # self.dll.add_to_tail(self.storage[new_node])
        # self.size +=
        # return new_node.value[0]

