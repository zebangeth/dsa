class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t0, t1, t2 = False, False, False
        for triplet in triplets:
            if triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                t0 = True
            if triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <= target[2]:
                t1 = True
            if triplet[2] == target[2] and triplet[0] <= target[0] and triplet[1] <= target[1]:
                t2 = True
            if t0 and t1 and t2:
                return True
        return False
