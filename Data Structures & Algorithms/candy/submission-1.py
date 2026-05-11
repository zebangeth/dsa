class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        # left to right: ensure every kid with rating higher than left get more candy than left nei
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # right to left:
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i + 1] + 1, candies[i])
        
        print(candies)
        return sum(candies)

