283. Move Zeroes
Easy

4176

132

Add to List

Share
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Solution:

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        no_of_zeroes=0
        l=[]
        for i in range(len(nums)):
            if nums[i]==0:
                no_of_zeroes+=1
        
        for j in range(len(nums)):
            if nums[j]!=0:
                l.append(nums[j])
                
                
        for k in range(no_of_zeroes):
            l.append(0)
            
        for h in range(len(nums)):
            nums[h]=l[h]
