class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        ls = {}
        for i in range(len(s)):
            ls[s[i]]= ls.get(s[i],0)+1
            ls[t[i]]= ls.get(t[i],0)-1
        
        for k in ls :
            if ls[k]!=0:
                return False
        return True 