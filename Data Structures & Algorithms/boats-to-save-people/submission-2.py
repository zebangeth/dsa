class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        survivor = sorted(people)
        boats = 0
        l, r = 0, len(survivor) - 1
        while l <= r:
            boats += 1
            capacity = limit - survivor[r]
            r -= 1
            if capacity >= survivor[l]:
                l += 1
                capacity -= survivor[l]
            
        return boats