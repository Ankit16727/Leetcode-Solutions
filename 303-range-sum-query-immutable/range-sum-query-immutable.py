class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        self.prefixSums = []
        for i in range(len(nums)):
            if i == 0:
                self.prefixSums.append(nums[i])
            else:
               self.prefixSums.append(nums[i] + self.prefixSums[i - 1]) 
        

    def sumRange(self, left, right):
        return self.prefixSums[right] if left == 0 else self.prefixSums[right] - self.prefixSums[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)