class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res=[words[0]]
        n=len(words)
        for i in range(1,n):
            if sorted(words[i])!=sorted(words[i-1]):
                res.append(words[i])
        return res