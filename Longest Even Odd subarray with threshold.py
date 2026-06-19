class Solution:
    def longestAlternatingSubarray(self, nums, threshold):
        n = len(nums)
        longest = 0
        left = 0
        while left < n:
            if nums[left] % 2 != 0 or nums[left] > threshold:
                left += 1
                continue
            right = left
            while (
                right + 1 < n
                and nums[right + 1] <= threshold
                and nums[right] % 2 != nums[right + 1] % 2
            ):
                right += 1
            longest = max(longest, right - left + 1)
            left += 1
        return longest
