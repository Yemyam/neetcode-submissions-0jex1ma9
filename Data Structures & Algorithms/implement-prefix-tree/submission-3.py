class Node:
        def __init__(self, val = ""):
            self.val = val
            self.children = {}

class PrefixTree:
    # insert the chars into a tree, and add a * to indicate that the word is complete
    def __init__(self):
        self.root = Node(val = "*")

    def insert(self, word: str) -> None:
        chars = list(word)
        node = self.root
        for char in chars:
            if char in node.children.keys():
                pass 
            else:
                new_node = Node()
                node.children[char] = new_node
            node = node.children[char]
        node.val = "*"

    def search(self, word: str) -> bool:
        chars = list(word)
        node = self.root
        for char in chars:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        if node.val == "*":
            return True 
        return False
        
    def startsWith(self, prefix: str) -> bool:
        chars = list(prefix)
        node = self.root
        for char in chars:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True
        
        