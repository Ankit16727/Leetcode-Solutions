class Solution(object):
    def intersection(self, nums1, nums2):
        ret_arr = []
        hash_set = {}
        for i in range(len(nums1)):
            if nums1[i] not in hash_set:
                for j in range(len(nums2)):
                    if nums1[i] == nums2[j]:
                        ret_arr.append(nums1[i])
                        break
                
                hash_set[nums1[i]] = i
        return ret_arr
                
                

        