class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = sum(range(n))
        actual_sum = sum(nums)
        return expected_sum - actual_sum
