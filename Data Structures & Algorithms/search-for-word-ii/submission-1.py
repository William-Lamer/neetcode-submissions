class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.fullWord = str()

    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        cur.fullWord = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build the prefix tree
        root = TrieNode()
        for word in words:
            root.add_word(word)

        
        ROWS = len(board)
        COLS = len(board[0])
        res = []

        def dfs(row, col, cur):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return

            c = board[row][col]
            if c not in cur.children:
                return
            
            cur = cur.children[c]
            if cur.endOfWord:
                res.append(cur.fullWord)
                cur.endOfWord = False

            board[row][col] = "#"
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for dr, dc in directions:
                dfs(row + dr, col + dc, cur)
            board[row][col] = c


        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root)
        return res


        