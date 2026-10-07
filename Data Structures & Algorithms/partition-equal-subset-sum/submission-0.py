class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        else:
            target //= 2

        reachable = {0}
        for n in nums:
            new_sums = set()
            for s in reachable:
                if (s + n) <= target:
                    new_sums.add(s + n)
            reachable |= new_sums
        
        return (target in reachable)