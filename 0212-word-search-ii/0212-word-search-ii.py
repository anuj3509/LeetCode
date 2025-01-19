class TrieNode():
    def __init__(self):
        self.children = {}
        self.endofword = False

    def addword(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endofword = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # create a trie and put every word in it
        for w in words:
            root.addword(w)

        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r,c, node, word):
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                (r, c) in visit or board[r][c] not in node.children):
                return 
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endofword:
                res.add(word)
            
            # DFS in all 4 directions: right, left, up, down
            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)

            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)