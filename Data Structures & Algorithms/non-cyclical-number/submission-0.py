class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_sum(temp):
            total = 0
            while temp > 0:
                digit = temp % 10
                total += digit ** 2
                temp //= 10
            return total
        

        seen = set()
        while n != 1:
            sum = get_sum(n)

            if sum in seen:
                return False
            seen.add(sum)

            n = sum

        return True