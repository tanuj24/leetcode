class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Initialize two pointers for backtracking
        s_ptr, p_ptr = 0, 0
        s_star_ptr, p_star_ptr = -1, -1
        
        # Continue until we reach the end of the string
        while s_ptr < len(s):
            #  If the pattern and string characters match or pattern character is '?'
            if p_ptr < len(p) and (s[s_ptr] == p[p_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            # If the pattern character is '*'
            elif p_ptr < len(p) and p[p_ptr] == '*':
                # Update the pointers to the current positions
                s_star_ptr = s_ptr
                p_star_ptr = p_ptr
                # Move the pattern pointer to the next character
                p_ptr += 1
            # If the previous pattern character was '*'
            elif p_star_ptr != -1:
                # Move the string pointer to the next character
                s_star_ptr += 1
                s_ptr = s_star_ptr
                # Move the pattern pointer to the position after '*'
                p_ptr = p_star_ptr + 1
            # If none of the above cases match, the pattern doesn't match the string
            else:
                return False
        
        # Checking for any remaining '*' characters in the pattern
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
        
        # Return True if we have reached the end of both the pattern and string
        return p_ptr == len(p)