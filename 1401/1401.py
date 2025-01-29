class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        '''
        -----
        |   |
        |   |
        |---|
        '''
        
        x1 -= xCenter
        x2 -= xCenter
        y1 -= yCenter
        y2 -= yCenter
        # x^2 + y^2 <= R^2
        minX = 0 if x1 * x2 <= 0 else min(x1*x1,x2*x2)
        minY = 0 if y1 * y2 <= 0 else min(y1*y1,y2*y2)

        return minX + minY <= radius**2
        
