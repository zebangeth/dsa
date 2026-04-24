class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_m = [self.get_prefix_sum(nums) for nums in matrix]
        print(self.prefix_m)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0

        for row in range(row1, row2 + 1):
            total += self.prefix_m[row][col2 + 1] - self.prefix_m[row][col1]

        return total

    def get_prefix_sum(self, nums):
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        return prefix_sum
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)