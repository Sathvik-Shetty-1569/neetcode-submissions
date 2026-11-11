class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ls=[0]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            ls[i] = prefix
            prefix*=nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            ls[i] *= postfix
            postfix *=nums[i]
        return ls