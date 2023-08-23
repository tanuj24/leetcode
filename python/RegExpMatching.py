class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a memoization table to store the results of subproblems
        memo = {}

        def backtrack(i, j):
            # Check if the subproblem has already been solved
            if (i, j) in memo:
                return memo[(i, j)]

            # Base case: if both strings are empty, the pattern matches
            if j == len(p):
                return i == len(s)

            # Check if the current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # Handle the case when the pattern has a '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # if '*' matches zero preceding element
                ans = backtrack(i, j + 2)

                # if '*' matches one or more preceding elements
                if first_match:
                    ans = ans or backtrack(i + 1, j)

            # when the pattern doesn't have a '*'
            else:
                ans = first_match and backtrack(i + 1, j + 1)

            # Memoize the result and return
            memo[(i, j)] = ans
            return ans

        # Call the backtrack function with initial indices
        return backtrack(0, 0)