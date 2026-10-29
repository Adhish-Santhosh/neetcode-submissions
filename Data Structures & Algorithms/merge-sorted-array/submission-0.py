class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ch = []
        for i in range(m):
            ch.append(nums1[i])

        for j in range(n):
            ch.append(nums2[j])

        ch.sort()

        for i in range(m + n):
            nums1[i] = ch[i]
        
            