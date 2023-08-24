class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            remainder = (columnNumber - 1) % 26
            char = chr(ord('A') + remainder)
            result.append(char)
            columnNumber = (columnNumber - 1) // 26

        return ''.join(result[::-1])