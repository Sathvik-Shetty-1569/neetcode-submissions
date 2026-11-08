class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = {}
        tmap = {}
        for l in range(len(s)):
            smap[s[l]] = smap.get(s[l],0)+1
            tmap[t[l]] = tmap.get(t[l],0)+1

        return smap == tmap