class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        for card in sorted(hand):
            n = count[card]
            if n == 0:
                continue
            for c in range(card, card + groupSize):
                if count[c] < n:
                    return False
                count[c] -= n
        return True
