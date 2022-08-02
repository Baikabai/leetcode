class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic = {
            0 : 0,
            1 : 0,
            2 : 0
        }
        for i in nums:
            dic[i] += 1
        nums[:] = dic[0]*[0]+dic[1]*[1]+dic[2]*[2]