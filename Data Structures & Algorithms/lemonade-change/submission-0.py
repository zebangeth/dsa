class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 5:
                changes[5] += 1
            elif bill == 10:
                if changes[5] == 0:
                    return False
                changes[5] -= 1
                changes[10] += 1
            elif bill == 20:
                change = 15
                if changes[10] > 0:
                    changes[10] -= 1
                    change -= 10
                while change > 0 and changes[5] > 0:
                    changes[5] -= 1
                    change -= 5
                if change > 0:
                    return False
                changes[20] += 1
        return True