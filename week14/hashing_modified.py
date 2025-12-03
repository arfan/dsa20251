# hashing.py
from typing import Optional, Any


class ListNode:
    """Simple singly-linked list node used for separate chaining."""
    __slots__ = ("key", "value", "next")

    def __init__(self, key: int, value: Any, nxt: 'ListNode' = None):
        self.key = key
        self.value = value
        self.next = nxt

    def __repr__(self):
        return f"ListNode(key={self.key}, value={self.value})"


def is_prime(n: int) -> bool:
    """Return True if n is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def get_closest_prime(size: int) -> int:
    """Find the smallest prime >= size."""
    if size <= 2:
        return 2
    candidate = size if size % 2 != 0 else size + 1
    while not is_prime(candidate):
        candidate += 2
    return candidate


class HashTable:
    """
    Hash table using separate chaining (linked lists).
    Methods: insert(key, value), search(key) -> value or None, delete(key) -> bool, contains(key) -> bool
    """

    def __init__(self, size: int = 11):
        self.table_size = get_closest_prime(size)
        self.table = [None] * self.table_size  # type: list[Optional[ListNode]]
        self.count = 0  # number of stored elements
        # Resize threshold: when load factor > 0.7, rehash into a larger table
        self._max_load_factor = 0.7

    def _hash_function(self, key: int) -> int:
        return key % self.table_size

    def _load_factor(self) -> float:
        return self.count / self.table_size

    def _maybe_resize(self):
        if self._load_factor() > self._max_load_factor:
            new_size = get_closest_prime(self.table_size * 2)
            self._rehash(new_size)

    def _rehash(self, new_size: int):
        old_table = self.table
        self.table_size = new_size
        self.table = [None] * self.table_size
        old_count = self.count
        self.count = 0
        for head in old_table:
            curr = head
            while curr:
                self.insert(curr.key, curr.value)
                curr = curr.next
        # ensure count restored correctly (insert increments)
        assert self.count == old_count

    def insert(self, key: int, value: Any) -> None:
        """Insert (key, value). If key already exists, update the value."""
        index = self._hash_function(key)
        head = self.table[index]
        curr = head
        # check if key exists -> update
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next
        # insert new node at head
        new_node = ListNode(key, value, head)
        self.table[index] = new_node
        self.count += 1
        self._maybe_resize()

    def search(self, key: int) -> Optional[Any]:
        """Return the value associated with key or None if not found."""
        index = self._hash_function(key)
        curr = self.table[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None

    def delete(self, key: int) -> bool:
        """Delete key from table. Return True if deleted, False if not found."""
        index = self._hash_function(key)
        curr = self.table[index]
        prev = None
        while curr:
            if curr.key == key:
                if prev is None:
                    # removing head
                    self.table[index] = curr.next
                else:
                    prev.next = curr.next
                self.count -= 1
                return True
            prev = curr
            curr = curr.next
        return False

    def contains(self, key: int) -> bool:
        return self.search(key) is not None

    def __len__(self):
        return self.count

    def __repr__(self):
        # Show bucket lists for debugging
        parts = []
        for i, head in enumerate(self.table):
            if head:
                nodes = []
                curr = head
                while curr:
                    nodes.append(f"({curr.key}:{curr.value})")
                    curr = curr.next
                parts.append(f"{i}: " + " -> ".join(nodes))
            else:
                parts.append(f"{i}: []")
        return "<HashTable size={}, count={}>\n{}".format(self.table_size, self.count, "\n".join(parts))

if __name__ == "__main__":
    h = HashTable(size=7)       # will choose closest prime >= 7

    h.insert(10, "kuda")
    h.insert(17, "ayam")
    h.insert(14, "zebra")
    h.insert(21, "singa")

    print(h)

    result = h.search(10)
    print(result)

    h.delete(10)

    print(h)

    result = h.search(10)
    print(result)
