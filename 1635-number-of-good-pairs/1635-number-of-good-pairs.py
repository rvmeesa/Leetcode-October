class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        count = [0] * 101  # Create a list of size 101 initialized with zeros

        for num in nums:
            ans += count[num]
            count[num] += 1

        return ans