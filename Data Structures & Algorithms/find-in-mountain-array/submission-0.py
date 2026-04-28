class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        if not mountainArr:
            return -1

        peak_idx = self._find_peak(mountainArr)

        # check left side
        start, end = 0, peak_idx
        while start + 1 < end:
            mid = (start + end) // 2
            if mountainArr.get(mid) < target:
                start = mid
            else:
                end = mid

        if mountainArr.get(start) == target:
            return start
        if mountainArr.get(end) == target:
            return end

        # check right side
        start, end = peak_idx, mountainArr.length() - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if mountainArr.get(mid) > target:
                start = mid
            else:
                end = mid

        if mountainArr.get(start) == target:
            return start
        if mountainArr.get(end) == target:
            return end
        return -1
        
    def _find_peak(self, arr):
        start, end = 0, arr.length() - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if arr.get(mid) < arr.get(mid + 1):
                start = mid
            else:
                end = mid

        if arr.get(start) > arr.get(end):
            return start
        return end