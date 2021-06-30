class Solution:
    def intToRoman(self, num: int) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        
        i = 0
        roman_num = ""
        while num > 0:
            for _ in range(num//val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
                