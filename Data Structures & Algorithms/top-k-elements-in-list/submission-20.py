class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for i in nums:
            hmap[i] = hmap.get(i,0)+1
        
        sortedhmap = sorted(hmap.items(),key = lambda x:x[1],reverse = True)
        ls = []
        i = 0
        while(k!=0):
            ls.append(sortedhmap[i][0])
            i+=1
            k-=1
        
        return ls