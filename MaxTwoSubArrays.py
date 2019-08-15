# -*- coding:utf-8 -*-
"""
@param nums: A list of integers
@return: An integer denotes the sum of max two non-overlapping subarrays
"""
def maxTwoSubArrays(nums):
    # write your code here
    # write your code here
    n = len(nums)
    a = nums[:]
    aa = nums[:]
    for i in range(1, n):
        a[i] = max(nums[i], a[i-1] + nums[i])
        aa[i] = max(a[i], aa[i-1])
    b = nums[:]
    bb = nums[:]
    for i in range(n-2, -1, -1):
        b[i] = max(b[i+1] + nums[i], nums[i])
        bb[i] = max(b[i], bb[i+1])
    mx = -65535
    for i in range(n - 1):
        mx = max(aa[i]+bb[i+1], mx)
    return mx


print maxTwoSubArrays([1, 3, -1, 2, -1, 2])
