#This program implements the trie operations
#Refernce: askpython.com

class trieNode:
    def __init__(self, char):
        self.char = char
        self.endOfWord = False
        self.children = {}

#Intializes empty trie node
class Trie(object):
    def __init__(self):
        self.root = trieNode("")

    #inseertion
    def insert(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = trieNode(char)
                node.children[char] = new_node
                node = new_node
        node.endOfWord = True

    def dfs(self, node, prev):
        if node.endOfWord:
            self.output.append((prev + node.char))

        for child in node.children.values():
            self.dfs(child, prev + node.char)

    def search(self, val):
        node = self.root
        for char in val:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        self.output = []
        self.dfs(node, val[:-1])

        return self.output

tr = Trie()
tr.insert("dough")
tr.insert("dog")
tr.insert("doughnut")
tr.insert("dot")
tr.insert("time")

print(tr.search("do"))