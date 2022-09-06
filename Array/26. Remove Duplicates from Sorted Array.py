# Solution 1
class Solution(object):
    def __init__(self,nums):
        self.nums = nums
    def removeDuplicates(self):
        for i in range(1,len(self.nums)):
            for j in range(0,i):
                if self.nums[i] == self.nums[j]:
                    self.nums[i] = 'a'
        while 'a' in self.nums:
            self.nums.remove('a')
        return self.nums

nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution(nums)
print(sol.removeDuplicates())

# Solution 2
class Solution2(object):
    def __init__(self,nums):
        self.nums = nums
    def removeDuplicates(self):
        for i in range(len(self.nums)-1,0,-1):
            if self.nums[i] == self.nums[i-1]:
                self.nums.pop(i)
        print(len(self.nums), ', nums  = ', self.nums)

nums2 = [0,0,1,1,1,2,2,3,3,4]
sol2 = Solution2(nums2)
sol2.removeDuplicates()

