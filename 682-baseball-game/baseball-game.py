class Solution(object):
    def calPoints(self, operations):
        arr = [0] * len(operations)
        top, total_sum = -1, 0
        for i in range(len(operations)):
            if operations[i] == '+':
                arr[top + 1] = arr[top] + arr[top - 1]
                top += 1
                total_sum += arr[top]
            elif operations[i] == 'D':
                arr[top + 1] = 2 * arr[top]
                top += 1
                total_sum += arr[top]
            elif operations[i] == 'C':
                total_sum -= arr[top]
                top -= 1
            else:
                # It's an integer
                x = int(operations[i])
                top += 1
                arr[top] = x
                total_sum += x
        return total_sum
        