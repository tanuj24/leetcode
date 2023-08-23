class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_list = [0] * 26
        for char in s:
            freq_list[ord(char) - ord('a')] += 1
        
        # Step 2: Sort the characters in decreasing order of their frequencies
        sorted_chars = []
        for i in range(26):
            if freq_list[i] > 0:
                sorted_chars.append(chr(i + ord('a')))
        sorted_chars.sort(key=lambda x: (-freq_list[ord(x) - ord('a')], x))
        
        # Step 3: Check if the most frequent character has a frequency greater than half of the string length
        if freq_list[ord(sorted_chars[0]) - ord('a')] > (len(s) + 1) // 2:
            return ""
        
        # Step 4: Initialize the result string
        result = [""] * len(s)
        
        # Step 5: Fill the result string with alternating characters
        idx = 0
        for char in sorted_chars:
            while freq_list[ord(char) - ord('a')] > 0:
                result[idx] = char
                idx += 2
                if idx >= len(s):
                    idx = 1
                freq_list[ord(char) - ord('a')] -= 1
        
        # Step 6: Return the result string
        return "".join(result)