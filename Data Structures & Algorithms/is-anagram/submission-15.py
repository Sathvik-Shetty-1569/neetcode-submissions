class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = {}
        tmap = {}
        for l in s:
            smap[l] = smap.get(l,0)+1
        
        for l in t:
            tmap[l] = tmap.get(l,0)+1

        if smap == tmap:
            return True

        return False