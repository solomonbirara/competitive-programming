class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        counts=[0]*((max(nums)+1)+k)
        for num in nums:
            counts[num]+=1
        prefix=[counts[0]]
        for count in counts[1:]:
            prefix.append(prefix[-1]+count)
        ans=0
        for i in range(len(counts)-k):    
            left=max(0,i-k-1)
            right=min(i+k,len(counts)-1)
            mid=counts[i]
            convertible_amount=prefix[right]-prefix[left]-mid
            if convertible_amount>numOperations:
                ans=max(ans,mid+numOperations)
            else:
                ans=max(ans,mid+convertible_amount)
        return ans   
