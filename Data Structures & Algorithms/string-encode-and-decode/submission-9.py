from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+"#"+s
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        ls=[]
        while(i<len(s)):
            j=i
            while(s[j]!="#"):
                j+=1
            l = int(s[i:j])
            ls.append(s[j+1:j+1+l])
            i=j+1+l
        return ls
