class Solution(object):
    def minimumDistance(self, nums):
        hash_nums, min_dis = {}, None
        for i in range(len(nums)):
            if nums[i] in hash_nums:
                if len(hash_nums[nums[i]]) == 3:
                    hash_nums[nums[i]][0] = hash_nums[nums[i]][1]
                    hash_nums[nums[i]][1] = hash_nums[nums[i]][2]
                    hash_nums[nums[i]][2] = i
                else:
                    hash_nums[nums[i]].append(i)
            else:
                hash_nums[nums[i]] = [i]
            
            if len(hash_nums[nums[i]]) == 3:
                dist = 2 * (hash_nums[nums[i]][2] - hash_nums[nums[i]][0])
                min_dis = dist if min_dis is None else min(min_dis, dist)
        
        return min_dis if min_dis != None else -1

            
            
            
        












































        