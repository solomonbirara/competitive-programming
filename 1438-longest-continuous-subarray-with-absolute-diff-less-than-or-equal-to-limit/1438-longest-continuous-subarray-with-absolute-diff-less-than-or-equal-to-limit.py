from collections import deque

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        minq, maxq = deque(), deque()
        l = 0
        res = 0

        for r in range(len(nums)):
            while minq and nums[minq[-1]] > nums[r]:
                minq.pop()
            while maxq and nums[maxq[-1]] < nums[r]:
                maxq.pop()

            minq.append(r)
            maxq.append(r)

            while nums[maxq[0]] - nums[minq[0]] > limit:
                l += 1
                if minq[0] < l:
                    minq.popleft()
                if maxq[0] < l:
                    maxq.popleft()

            res = max(res, r - l + 1)

        return res