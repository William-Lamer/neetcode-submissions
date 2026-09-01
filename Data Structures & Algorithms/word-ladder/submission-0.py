class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # returns a list of words that differ by 1 from a set of words
        def neighbors(word, words):
            chars = "abcdefghijklmnopqrstuvwxyz"
            for i in range(len(word)):
                for c in chars:
                    candidate = word[:i] + c + word[i+1:]
                    if candidate in words:
                        yield candidate
        
        words = set(wordList)
        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])
        seen = {beginWord}

        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for nxt in neighbors(word, words):
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, dist + 1))
        return 0



