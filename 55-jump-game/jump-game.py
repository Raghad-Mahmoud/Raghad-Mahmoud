class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        outmost = 0
        for i in range(len(nums)):
             if i > outmost:
                 return False
             outmost = max(outmost, i + nums[i])
        return True
 