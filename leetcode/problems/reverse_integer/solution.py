class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = 1 if x >= 0 else -1
        x = abs(x)
        x_str = str(x)
        
        reversed_str = x_str[::-1]
        
        reversed_num = int(reversed_str)
        
        if reversed_num > INT_MAX:
            return 0
        
        return reversed_num * sign