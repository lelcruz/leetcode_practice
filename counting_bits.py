class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(bin(i).count('1'))
        return ans
