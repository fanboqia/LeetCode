import math
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums):
        #check empty
        if nums == None or len(nums) == 0:
            return None
        #sort
        nums = sorted(nums)
        #odd
        if len(nums) & 1 == 1:
            return nums[len(nums)/2]
        else:
            return nums[int(len(nums)/2)-1]
