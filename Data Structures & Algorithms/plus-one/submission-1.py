class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        i = len(digits) - 1

        while carry or i == len(digits) - 1:
            carry = 0
            digits[i] += 1
            if digits[i] >= 10:
                digits[i] %= 10
                carry = 1
            
            if i == 0 and carry:
                return [1] + digits
            
            i -= 1

        return digits

