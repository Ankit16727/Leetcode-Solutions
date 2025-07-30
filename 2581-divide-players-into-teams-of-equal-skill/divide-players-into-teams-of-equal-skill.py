class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()
        k = skill[0] + skill[len(skill) - 1]
        total = 0
        l, h = 0, len(skill) - 1

        while l < h:
            if skill[l] + skill[h] == k:
                total += skill[l] * skill[h]
            else:
                return -1
            l += 1
            h -= 1
        
        return total
        