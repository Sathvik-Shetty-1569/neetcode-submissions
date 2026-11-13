class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            hmap[nums[i]] = hmap.get(nums[i],0)+1
        sortmap = sorted(hmap.items(), key = lambda x:x[1], reverse = True)
        c = 0
        ls = []
        while(c<k):
            ls.append(sortmap[c][0])
            c+=1
        return ls