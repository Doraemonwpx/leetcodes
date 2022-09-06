class Solution(object):
    def __init__(self, digits):
        self.digits = digits
    def plusOne(self):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        x = str(0)
        for i in range(len(digits)):
            x = x + str(digits[i])
        inv = []
        x = str(int(x)+1)
        for i in range(len(x)):
            inv.append(x[i])
        return inv
            #self.digits[len(self.digits)-1] = self.digits[len(self.digits)-1] + 1
            #return self.digits

digits = [9]
sol = Solution(digits)
print(sol.plusOne())
#print(sol.plusOne())