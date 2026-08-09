class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def helper_expand(l, r):
            total = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                total += 1

                l -= 1
                r += 1
            return total


        for i in range(len(s)):
            # odd length
            res += helper_expand(i, i)

            #even length
            res += helper_expand(i, i+1)

        return res
