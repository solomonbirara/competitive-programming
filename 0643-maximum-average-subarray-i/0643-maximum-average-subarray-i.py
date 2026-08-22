class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        cur_sum=0
        max_ave=0
        for i in range(k):
            cur_sum+=nums[i]
        max_ave=cur_sum/k
        for i in range(k,n):
            cur_sum+=nums[i]
            cur_sum-=nums[i-k]
            ave=cur_sum/k
            max_ave=max(max_ave,ave)
        return max_ave