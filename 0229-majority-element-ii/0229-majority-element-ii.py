class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return []

        # Initialize candidates and their counts
        candidate1, candidate2, count1, count2 = 0, 1, 0, 0

        # Step 1: Find the two potential candidates
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Reset counts and re-count to verify candidates
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        # Step 3: Check if candidates are valid
        result = []
        if count1 > len(nums) // 3:
            result.append(candidate1)
        if count2 > len(nums) // 3:
            result.append(candidate2)
#return result
        return result
