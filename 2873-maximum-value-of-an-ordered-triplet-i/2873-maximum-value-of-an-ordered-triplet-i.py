class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        max_res=0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if i<j<k:
                        res=(nums[i]-nums[j])*nums[k]
                        
                        
                        max_res=max(max_res,res)
                        if max_res<0:
                            max_res==0

        return max_res


        