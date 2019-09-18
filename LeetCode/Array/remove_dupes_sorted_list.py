'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/
'''
class Solution:

    def remove_duplicates(self, nums: list) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1
        val = nums[0]
        for index, num in enumerate(nums[1:len(nums)]):
            if val == num:
                nums.remove(num)
            else:
                val = num
        return len(nums)
