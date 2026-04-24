class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest_idx = self._find_closest(arr, x)
        l, r = closest_idx - 1, closest_idx
        result = collections.deque()
        while l >= 0 and r < len(arr) and k > 0:
            if abs(arr[l] - x) <= abs(arr[r] - x):
                result.appendleft(arr[l])
                l -= 1
            else:
                result.append(arr[r])
                r += 1
            k -= 1
        
        while k > 0:
            if l >= 0:
                result.appendleft(arr[l])
                l -= 1
            else:
                result.append(arr[r])
                r += 1
            k -= 1

        return list(result)

    
    def _find_closest(self, arr, x):
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] < x:
                start = mid
            elif arr[mid] > x:
                end = mid
            else:
                return mid
        if abs(arr[start] - x) < abs(arr[end] - x):
            return start
        return end
