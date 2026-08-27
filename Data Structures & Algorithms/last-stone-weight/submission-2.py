class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        
        while len(stones) > 1:
            heaviest = heapq.heappop_max(stones)
            second_heaviest = heapq.heappop_max(stones)

            if heaviest == second_heaviest:
                smashed = 0
            else:
                smashed = abs(heaviest - second_heaviest)
            
            heapq.heappush_max(stones, smashed)

        return stones[0] if stones else 0