class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            r, c = self._conver_to_2d(mid, m, n)
            if matrix[r][c] < target:
                start = mid
            elif matrix[r][c] > target:
                end = mid
            else:
                return True
        
        start_r, start_c = self._conver_to_2d(start, m, n)
        end_r, end_c = self._conver_to_2d(end, m, n)
        if matrix[start_r][start_c] == target or matrix[end_r][end_c] == target:
            return True
        return False

        
    def _conver_to_2d(self, x, m, n):
        return x // n, x % n

