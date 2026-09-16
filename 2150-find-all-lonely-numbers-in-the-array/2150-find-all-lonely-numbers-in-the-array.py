class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        res = []
        count = {}

        for x in nums:
            count[x] = count.get(x, 0) + 1

        for x in nums:
            if count[x] == 1 and x - 1 not in count and x + 1 not in count:
                res.append(x)

        return res