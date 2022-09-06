class Solution(object):
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    def searchInsert(self):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if self.target in self.nums:
            return self.nums.index(self.target)
        else:
            for i in range(len(self.nums)):
                if self.nums[i] > self.target:
                    return i
                elif self.nums[len(self.nums)-1] < self.target:
                    return len(self.nums)

nums = [1,3,5,6]
target = 7
sol = Solution(nums, target)
print(sol.searchInsert())