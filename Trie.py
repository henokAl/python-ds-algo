from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.items = ""


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.items = word

    def search(self, word):
        node = self.root
        for c in word:
            if node.children.get(c) is None:
                return False
            node = node.children[c]

        if word == node.items:
            return True
        return False

    def searchPrefix(self, prefix):
        node = self.root
        for c in prefix:
            if node.children.get(c) is None:
                return False
            node = node.children[c]
        return True


if __name__ == '__main__':
    t = Trie()
    t.insert("apple")
    print(t.searchPrefix("app"))
    print(t.search("apl"))


