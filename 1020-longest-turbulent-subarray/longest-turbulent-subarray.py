class Solution(object):
    def maxTurbulenceSize(self, arr):
        l, max_len = 0, 1
        for r in range(len(arr) - 1):
            if r == l:
                if arr[r] == arr[r + 1]:
                    l += 1
            else:
                if arr[r] == arr[r + 1]:
                    l = r + 1
                elif arr[r - 1] > arr[r]:
                    if arr[r] > arr[r + 1]:
                        l = r
                else:
                    # arr[r - 1] < arr[r]
                    if arr[r] < arr[r + 1]:
                        l = r
            max_len = max(max_len, r - l + 2)
        return max_len