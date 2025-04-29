class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        similar_num = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[similar_num] = nums[i]
                similar_num +=1
        return similar_num

                
