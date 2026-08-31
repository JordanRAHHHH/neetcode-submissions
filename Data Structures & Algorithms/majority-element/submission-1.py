class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        largest = 0

        for num in seen:
            if seen[num] > largest and seen[num] >= len(nums)/2:
                largest = num

        return largest
        
