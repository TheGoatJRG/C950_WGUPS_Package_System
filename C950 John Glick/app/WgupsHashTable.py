"""
John Glick
001418867
C950- WGUPS Delivery System

Ref: "zyBooks: Figure 7.8.2: Hash table using chaining."
Ref: Creation of hash table, insertion function, search function

WgupsHashTable.py
"""


# BIG O- Average- O(1), Worst- O(n)
class WgupsHashTable:
    """A class representing a hash table.

  Attributes:
    table: A list of lists. Each inner list represents a bucket in the hash table.

  """

    def __init__(self, initial_capacity=10):
        """Initializes a HashTable object.

    Arguments:
      initial_capacity: The initial capacity of the hash table.

    """
        self.table = []
        for _ in range(initial_capacity):
            self.table.append([])

    # Hash Table Insertion function- BIG O- O(1)

    def insert(self, key, item):
        """Inserts an item into the hash table.

    Arguments:
      key: The key of the item to insert.
      item: The item to insert.

    """
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Check if the key already exists in the bucket.
        # BIG O- O(n)
        for kv in bucket_list:
            if kv[0] == key:
                # If the key already exists, update the item.
                kv[1] = item
                return

        # If the key does not already exist, insert the item at the end of the bucket list.
        bucket_list.append([key, item])

    # Hash Table Search Function- BIG O- O(1)
    def search(self, key):
        """Searches for an item in the hash table.

    Arguments:
      key: The key of the item to search for.

    Return Value:
      The item if it is found in the hash table, or None if it is not found.

    """
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Search for the key in the bucket list.
        # BIG O- O(n)
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]

        return None
