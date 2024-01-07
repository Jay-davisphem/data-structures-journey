from typing import List
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        preSum = nums[0]
        pre = nums[0]
        for num in nums[1:]:
            if num - pre == 1:
                pre = num
                preSum += num
            else:
                break
        
        while preSum in nums:
            preSum += 1
        
        return preSum
    
# Time complexity: O(N)
# Space complexity: O(1)

# Tests

sol = Solution()

# Test 1
nums1 = [1, 2, 3, 4, 6, 7]
assert sol.missingInteger(nums1) == 10