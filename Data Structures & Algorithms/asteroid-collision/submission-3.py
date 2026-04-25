class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for a in asteroids:
            # if a is positive, append
            if a > 0:
                result.append(a)
                continue

            # a is negative
            # if a is larger than the last positive asteroid, the last explodes
            while result and result[-1] > 0 and -a > result[-1]:
                result.pop()
            # if a is equal the size ofthe last positive asteroid, both explode
            if result and result[-1] > 0 and -a == result[-1]:
                result.pop()
                continue
            # if all positive explodes
            if not result or result[-1] < 0:
                result.append(a)
        return result
