class Solution:
    def merge(self,nums1: List[int], nums2: List[int]) -> List[int]:
        i = 0
        k = 0
        newNums = []

        while i < len(nums1) and k < len(nums2):
            if nums1[i] < nums2[k]:
                newNums.append(nums1[i])
                i+=1
            elif nums1[i] > nums2[k]:
                newNums.append(nums2[k])
                k+=1
            else:
                newNums.append(nums1[i])
                newNums.append(nums2[k])
                i+=1
                k+=1
            
        while i != len(nums1):
            newNums.append(nums1[i])
            i+=1
        while k != len(nums2):
            newNums.append(nums2[k])
            k+=1

        return newNums

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <=1 :
            return nums
        
        mid = len(nums) // 2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)