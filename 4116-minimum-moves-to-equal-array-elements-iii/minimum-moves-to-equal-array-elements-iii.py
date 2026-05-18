class Solution(object):
    def minMoves(self, nums):
        nums.sort()
        k, moves = nums[len(nums) - 1], 0
        for i in range(len(nums) - 1):
            moves += k - nums[i]
        
        return moves

        