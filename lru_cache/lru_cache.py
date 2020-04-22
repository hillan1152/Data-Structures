from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        # HASH TABLE
        self.storage = {}
        # LINKED LIST
        self.dll = DoublyLinkedList()
        # SIZE
        self.size = 0
        # Limit
        self.limit = limit
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    # Input Key ------ Output Value
    # Move k-v to head

    def get(self, key):
        # print("KEY ->", key)
        # print("GET Storage --> ", self.storage)
        # if key matches
        if key in self.storage:
            self.dll.move_to_front(self.storage[key])
            # print("KEY IN STORAGE --> ", self.storage[key].value[1])
            return self.storage[key].value[1]
        else:
            return None

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

    def set(self, key, value):
        if key in self.storage:
            storage_key = self.storage[key]
            # print("storage value --> ", storage_key.value[1])
            storage_key.value = (key, value)
            # print("new storage value --> ", storage_key.value[1])
            self.dll.move_to_front(storage_key)
            return
        if self.size == self.limit:
            del self.storage[self.dll.tail.value[0]]
            self.dll.remove_from_tail()
            self.size += 1
        self.dll.add_to_head((key, value))
        self.storage[key] = self.dll.head
        self.size += 1


cache = LRUCache(3)
cache.set('item1', 'a')
cache.set('item2', 'b')
cache.set('item3', 'c')
cache.set('item2', 'z')
print("Get --> ", cache.get('item1'))
# print("Storage --> ", cache.storage)
# print("Size --> ", cache.size)
