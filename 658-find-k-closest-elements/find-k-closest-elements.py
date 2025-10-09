class Solution(object):
    def findClosestElements(self, arr, k, x):
        l = 0
        for r in range(len(arr)):
            if r - l == k:
                if arr[r] <= x:
                    l += 1
                elif abs(arr[r] - x) < abs(arr[l] - x):
                    l += 1
                else:
                    return arr[l : l + k]
        return arr[l : l + k]

            
        