class Solution(object):
    def sumZero(self, n):
        x = n // 2 if n % 2 == 0 else (n - 1) // 2
        arr = []
        for i in range(-1*x, x + 1):
            if i != 0:
                arr.append(i)
        if n % 2 != 0:
            arr.append(0)

        return arr
        