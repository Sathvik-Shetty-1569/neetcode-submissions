class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictt = {}
        dicts={}
        for i in range(len(s)):
            dictt[s[i]] = dictt.get(s[i],0)+1
            dicts[t[i]] = dicts.get(t[i],0)+1
        
        if dictt == dicts:
            return True
        else :
            return False