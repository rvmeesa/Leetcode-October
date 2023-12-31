
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first_occurrence(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def find_last_occurrence(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        first_occurrence = find_first_occurrence(nums, target)
        last_occurrence = find_last_occurrence(nums, target)

        if first_occurrence <= last_occurrence:
            return [first_occurrence, last_occurrence]
        else:
            return [-1, -1]