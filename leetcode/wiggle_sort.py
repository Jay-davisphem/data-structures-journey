class Solution:
    def wiggleSort(self, nums):
        for i in range(1, len(nums)):
            if (i % 2 == 1 and nums[i] < nums[i - 1]) or (i % 2 == 0 and nums[i] > nums[i - 1]):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

# Test Case
solution = Solution()
nums = [3, 5, 2, 1, 6, 4]
solution.wiggleSort(nums)
print(nums)  