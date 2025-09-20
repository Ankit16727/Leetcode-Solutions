class Solution(object):
    def compress(self, chars):
        k, cnt = 0, 1

        for i in range(1, len(chars)):
            if chars[i] == chars[k]:
                cnt += 1
                if i == len(chars) - 1:
                    k += 1
                    arr = list(str(cnt))
                    for i2 in range(len(arr)):
                        chars[k] = arr[i2]
                        k += 1
                    k -= 1
            else:
                if cnt == 1:
                    k += 1
                    chars[k] = chars[i]
                else:
                    k += 1
                    arr = list(str(cnt))
                    for i2 in range(len(arr)):
                        chars[k] = arr[i2]
                        k += 1
                    chars[k] = chars[i]
                    cnt = 1
        return k + 1
        