class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        n = set(range(1,l+1))
        return list(n-set(nums))