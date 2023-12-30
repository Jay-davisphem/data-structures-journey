class Solution:
    def checkSubarraySum(self, nums, k):
        total, hash_map = 0, {0: -1}

        for i in range(len(nums)):
            total += nums[i]
            mod = total % k if k != 0 else total
            
            # meant we've add our required subarray, which makes us get the same mod
            if mod in hash_map and i - hash_map[mod] >= 2:
                return True

            if mod not in hash_map:
                hash_map[mod] = i

        return False

def main():
    sol = Solution()
    
    # Testcase 1
    nums1 = [23, 2, 4, 6, 7]
    k1 = 6
    assert sol.checkSubarraySum(nums1, k1) == True

    # Testcase 2
    nums2 = [23, 2, 6, 4, 7]
    k2 = 6
    assert sol.checkSubarraySum(nums2, k2) == True

    # Testcase 3
    nums3 = [23, 2, 6, 4, 7]
    k3 = 13
    assert sol.checkSubarraySum(nums3, k3) == False

    # Testcase 4
    nums4 = [5, 0, 0, 0]
    k4 = 3
    assert sol.checkSubarraySum(nums4, k4) == True

    # Testcase 5
    nums5 = [0, 0]
    k5 = 0
    assert sol.checkSubarraySum(nums5, k5) == True

    print("All test cases passed!")

# Run the test cases
main()
