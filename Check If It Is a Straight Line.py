1232. Check If It Is a Straight Line
Easy

393

66

Add to List

Share
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Solution:

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        y = coordinates[1][1] - coordinates[0][1]
        x = coordinates[1][0] - coordinates[0][0]
        
        for i in range(1, len(coordinates)):
            
            x_ = coordinates[i][0] - coordinates[i - 1][0]
            y_ = coordinates[i][1] - coordinates[i - 1][1]
        
            if y  * x_ != x * y_:
                return False
        
        return True
