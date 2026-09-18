class Solution:
    def defangIPaddr(self, address: str) -> str:
        i=0
        res=""
        while i<len(address):
            if address[i]==".":
                res+="[.]"
                i+=1
            else:
                res+=address[i]
                i+=1
        return res
