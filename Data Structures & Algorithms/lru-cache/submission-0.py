class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    # use a doubly linkedlist to store the most frequently used key
    # we will have a dummy head node and a dummy tail node
    # the head node will point to the most recently used node and the tail node will point to the least frequently used node
    def __init__(self, capacity: int):
        self.cap = capacity
        # every entry in the hashmap will point a key, to the corresponding node in the linkedlist
        self.hashmap = {}
        self.tail = Node(val=None)
        self.head = Node(val=None)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if not key in self.hashmap:
            return -1
        # move the node we read from to the front of the linked list
        # remove the node from its current position
        node = self.hashmap[key]
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        # add the node to the front of the linked list
        recent_node = self.head.next
        self.head.next = node
        recent_node.prev = node
        node.prev = self.head
        node.next = recent_node
        # return the value of the node
        return self.hashmap[key].val[1]

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = [key, value]
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
            # add the node to the front of the linked list
            recent_node = self.head.next
            self.head.next = node
            recent_node.prev = node
            node.prev = self.head
            node.next = recent_node
            # move the node to the front of the hashmap
        else:
            # create a new node at the front of the hashmap
            if len(self.hashmap) >= self.cap:
                # evict the node at the back of the linked list
                evicted_node = self.tail.prev
                prev = evicted_node.prev
                del self.hashmap[evicted_node.val[0]]
                prev.next = self.tail
                self.tail.prev = prev
            new_node = Node(val=[key, value])
            recent_node = self.head.next
            self.head.next = new_node
            recent_node.prev = new_node
            new_node.prev = self.head
            new_node.next = recent_node
            self.hashmap[key] = new_node


