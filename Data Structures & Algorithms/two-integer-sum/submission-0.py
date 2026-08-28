class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [0]*2
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    arr[0] = i
                    arr[1] = j
                    return arr
        