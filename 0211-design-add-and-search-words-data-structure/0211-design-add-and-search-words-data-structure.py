class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()   # if c does not exist, create a node at that point
            curr = curr.children[c]             # if c exists, update curr to children of curr
        curr.endofword = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):       # root would be the node we will be passing in
            curr = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):    # starting index = i+1 because we are going down a child
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.endofword

        return dfs(0, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)