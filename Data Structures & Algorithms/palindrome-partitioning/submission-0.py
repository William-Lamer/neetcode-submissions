class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(substring, palindromes):
            if not substring:
                res.append(palindromes.copy())
            
            for i in range(len(substring)):
                
                if substring[:i + 1] == substring[:i + 1][::-1]:
                    palindromes.append(substring[:i + 1])

                    backtrack(substring[i + 1:], palindromes)

                    palindromes.pop()


        backtrack(s, [])
        return res






