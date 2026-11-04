class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for i in strs:
            sortedstrs = tuple(sorted(i))
            hmap[sortedstrs].append(i)
        return list(hmap.values())