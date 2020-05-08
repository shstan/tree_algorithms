class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.root
        for char in word:
            if cur_node.get(char) == None:
                cur_node[char] = {}
            cur_node = cur_node[char]
        cur_node["*"] = {}  # adding "*" in the end to mark it as end of a word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self.root
        for char in word + "*":
            if cur_node.get(char) == None:
                return False
            cur_node = cur_node[char]
        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.root
        for char in prefix:
            if cur_node.get(char) == None:
                return False
            cur_node = cur_node[char]
        return True