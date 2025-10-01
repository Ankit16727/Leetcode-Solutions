class Solution(object):
    def longestMountain(self, arr):
        
        if len(arr) < 3:
            return 0
        else:
            # len >= 3
            si, p, mx = None, None, 0
            for i in range(1, len(arr)):
                if arr[i] > arr[i - 1]:
                    if si is None:
                        si = i - 1
                    elif p != None:
                        mx = max(mx, i - si)
                        si, p = i - 1, None
                elif arr[i] < arr[i - 1]:
                    if si != None and p is None:
                        p = i - 1
                else:
                    # Both are equal
                    if p != None:
                        mx = max(mx, i - si)
                        p = None
                    si = None

                if i == len(arr) - 1:
                    if p != None:
                        mx = max(mx, len(arr) - si)

            return mx

        