class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Using Manchester algorithm
        # creating the string to handle even-length palindromes
        processed_s = '#'.join('^{}$'.format(s))
        n = len(processed_s)
        P = [0] * n
        C, R = 0, 0

        for i in range(1, n - 1):
            if i < R:
                mirror = 2 * C - i
                P[i] = min(R - i, P[mirror])

            # expand palindrome centered at i
            a, b = i + (1 + P[i]), i - (1 + P[i])
            while processed_s[a] == processed_s[b]:
                P[i] += 1
                a += 1
                b -= 1

            # If palindrome centered at i expands past R,
            # adjust center based on expanded palindrome
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Finding the maximum element in P
        max_len, center_index = max((n, i) for i, n in enumerate(P))

        start = (center_index - max_len) // 2
        return s[start : start + max_len]