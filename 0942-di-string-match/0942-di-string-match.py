class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        res=[]
        minN=0
        maxN=len(s)
        n=len(s)
        for i in range(0,n):
            if s[i]=="I":
                res.append(minN)
                minN+=1
            else:
                res.append(maxN)
                maxN-=1
            
            
        res.append(minN)
        return res