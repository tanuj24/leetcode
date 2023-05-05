class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        length = len(s)
        winSum = sum(1 for i in range(k) if s[i] in vowels)
        res = winSum
        for i in range(k, length):
            winSum += 1 if s[i] in vowels else 0
            winSum -= 1 if s[i-k] in vowels else 0
            res = max(res, winSum)
        return res