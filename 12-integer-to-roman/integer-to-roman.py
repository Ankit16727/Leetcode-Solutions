class Solution(object):
    def intToRoman(self, num):
        n = 1000
        roman = ""
        while n:
            if num // n != 0:
                digit = num // n
                if digit == 4 or digit == 9:
                    if n == 100:
                        roman += 'C'
                        roman += 'D' if digit == 4 else 'M'
                    elif n == 10:
                        roman += 'X'
                        roman += 'L' if digit == 4 else 'C'
                    else:
                        #n -> 1
                        roman += 'I'
                        roman += 'V' if digit == 4 else 'X'
                else:
                    if n == 1000:
                        roman += digit * 'M'
                    elif n == 100:
                        if digit < 5:
                            roman += digit * 'C'
                        else:
                            roman += 'D' + (digit - 5) * 'C'
                    elif n == 10:
                        if digit < 5:
                            roman += digit * 'X'
                        else:
                            roman += 'L' + (digit - 5) * 'X'
                    else:
                        if digit < 5:
                            roman += digit * 'I'
                        else:
                            roman += 'V' + (digit - 5) * 'I'
                num = num - n * digit
                

            n = n // 10
        
        return roman
        