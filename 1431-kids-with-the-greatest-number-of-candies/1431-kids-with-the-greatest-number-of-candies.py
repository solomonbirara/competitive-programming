class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        maximum = max(candies)

        for candy in candies:
            res.append(candy + extraCandies >= maximum)

        return res