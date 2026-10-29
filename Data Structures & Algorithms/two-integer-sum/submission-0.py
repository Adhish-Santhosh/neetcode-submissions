class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        newval=0
        output=[]
        for i,j in enumerate(nums):
            newval=target-j
            for k in range(i+1,len(nums)):
                if nums[k]==newval:
                    output.append(i)
                    output.append(k)
                    return output
