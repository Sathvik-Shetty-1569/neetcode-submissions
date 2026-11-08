class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        smap={}
        for i in range(len(nums)):
            sum = target - nums[i]
            if sum in smap:
                return [smap[sum],i]
            smap[nums[i]] = i
        
