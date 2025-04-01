class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        table = {}
        max_length = 0
        for num in nums
            x = table.get(num-1, 0)
            y = table.get(num+1, 0)
            length = x + y +1
            table[num - x] = length
            table[num + y] = length
            max_length = max(max_length, length)
        return max_length
