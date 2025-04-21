class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        max_candy = max(candies)
        return list(map(lambda x : x + extraCandies >= max_candy,candies))
