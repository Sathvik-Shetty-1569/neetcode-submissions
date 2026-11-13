class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in range(len(strs)):
            dic[tuple(sorted(strs[i]))].append(strs[i])

        return list(dic.values())

