class Solution:
    def isHappy(self, n: int) -> bool:


        def sum(n):
            sumSquares = 0
            while n >= 1:
                digit = n % 10
                n = n // 10
                sumSquares += digit ** 2

            return sumSquares


        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum(n)


        return True