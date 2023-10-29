import math

class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        times = minutesToTest // minutesToDie
        result = 0
        while (times + 1) ** result < buckets:
            result += 1
        return result
