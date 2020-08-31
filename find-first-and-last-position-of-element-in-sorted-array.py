class Solution:
    def __init__(self):
        self.q = []
        
    def findFirst(self,l,r,arr,num):
        if l>r:
            self.q.append(-1)
            return
        m = l + (r-l)//2
    
        if arr[m] == num:
            if m-1<0:
                self.q.append(m)
                return
            
            elif arr[m-1] != num:
                self.q.append(m)
                return 
            else:
                self.findFirst(l,m-1,arr,num)
        if arr[m]>num:
            self.findFirst(l,m-1,arr,num)
        if arr[m]<num:
            self.findFirst(m+1,r,arr,num)
        
        
            
    
    def findLast(self,l,r,arr,num):
        if l>r:
            self.q.append(-1)
            return
        m = l + (r-l)//2
        if arr[m] == num:
            if  m+1>=len(arr):
                self.q.append(m)
                return 
            elif  m+1<len(arr) and arr[m+1] != num:
                self.q.append(m)
                return 
            else:
            
                self.findLast(m+1,r,arr,num)
        if arr[m]>num:
            self.findLast(l,m-1,arr,num)
        if arr[m]<num:
            self.findLast(m+1,r,arr,num)
            
            
                
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return (-1,-1)
        if len(nums) == 1:
            if target == nums[0]:
                return (0,0)
            else:
                return (-1,-1)
       
        n = len(nums)
        first = self.findFirst(0,n-1,nums,target)
        last = self.findLast(0,n-1,nums,target)
        return self.q        
