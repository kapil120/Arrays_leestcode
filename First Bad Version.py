278. First Bad Version
Easy

1593

714

Add to List

Share
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 

Solution:


class Solution:
    def firstBadVersion(self, n):
        
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n

        if n == 1:
            if isBadVersion(1) == True:
                return 1
            else:
                return False

        while l <= h:

            m = (l+h)//2


            if isBadVersion(m-1) == False and isBadVersion(m) == True:
                return m


            elif isBadVersion(m-1) == False and isBadVersion(m) == False:
                l = m+1
