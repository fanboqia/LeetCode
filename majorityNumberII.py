class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """
    def majorityNumber(self, nums):
        map = {}
        size = len(nums)
        for num in nums:
            if map.get(num) == None:
                map[num] =  1
            else:
               map[num] = map[num] + 1
            if map[num] * 3 > size:
                return num
