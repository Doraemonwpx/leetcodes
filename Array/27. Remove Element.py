class Solution(object):
    def __init__(self, nums, val):
        self.nums = nums
        self.val = val
    def removeElement(self):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while self.val in self.nums:
            self.nums.remove(self.val)
        print(len(self.nums), ', nums = ', self.nums)

nums = [3,2,2,3]
val = 3
sol = Solution(nums, val)
sol.removeElement()