class Solution:
    def sortByBits(self, arr):
        def count_bits(num):
            return bin(num).count('1')
        
        return sorted(arr, key=lambda x: (count_bits(x), x))
