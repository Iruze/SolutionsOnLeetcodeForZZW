# 裴蜀定理：如果 x + y >= z，且x,y的最大公约数gcd(x, y)能够整除z,则认为x,y水壶可以装满z
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        return z == 0 or x + y >= z and z % math.gcd(x, y) == 0
    
