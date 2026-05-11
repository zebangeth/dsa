class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counter = collections.Counter(hand)
        for num in hand:
            if num not in counter:
                continue
            # find the sequence start
            while num - 1 in counter:
                num -= 1
            
            # check this group
            for i in range(groupSize):
                if num + i not in counter:
                    return False
                counter[num + i] -= 1
                if counter[num + i] == 0:
                    counter.pop(num + i)
            
        return True
            