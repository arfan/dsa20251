import heapq

# A Huffman Tree Node
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # defining comparison for heapq (min-heap)
    def __lt__(self, other):
        return self.freq < other.freq

    def __str__(self):
        return f"({self.char!r}: {self.freq})"

    def __repr__(self):
        return self.__str__()


def huffman_encoding(char_freqs):
    # Create a priority queue (min-heap)
    heap = [Node(char, freq) for char, freq in char_freqs.items()]
    print("heap elements", heap)

    heapq.heapify(heap)
    print(heap)

    # Build the Huffman Tree
    while len(heap) > 1:
        print("heap elements: ", heap)
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # create new internal node
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    # The remaining node is the root
    root = heap[0]
    codes = {}

    # Recursive function to generate codes
    def print_codes(node, code=""):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = code
        print_codes(node.left, code + "0")
        print_codes(node.right, code + "1")

    print_codes(root)
    return codes


# Example usage
char_freqs = {
    'a': 5,
    'b': 9,
    'c': 12,
    'd': 13,
    'e': 16,
    'f': 45
}

codes = huffman_encoding(char_freqs)
print("Character Codes:")
for char, code in codes.items():
    print(f"{char}: {code}")
