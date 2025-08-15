class Solution(object):
    def totalFruit(self, fruits):
        l, no_dist, dist, curr, max_f = 0, 0 , {}, None, 0
        for r in range(len(fruits)):
            if fruits[r] not in dist:
                dist[fruits[r]] = 1
                no_dist += 1
                curr = r if no_dist <= 2 else curr
            else:
                # fruits[r] in dist
                if dist[fruits[r]] == 0:
                    no_dist += 1
                    dist[fruits[r]] = 1
                curr = r if fruits[r] != fruits[r - 1] and no_dist <= 2 else curr

            if no_dist > 2:
                max_f = max(max_f, r - l)
                dist[fruits[curr - 1]] = 0
                l = curr
                curr = r
                no_dist -= 1
        return max(max_f, len(fruits) - l)


                

        