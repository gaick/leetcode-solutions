class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        max_candy = max(candies)
        for i in candies:
            result.append(extraCandies + i >= max_candy)
        return result
