class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]*=nums[i]
            i+=1
        nums.sort()
        return nums

