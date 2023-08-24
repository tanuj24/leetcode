class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result, line, line_length = [], [], 0

        for word in words:
            if line_length + len(line) + len(word) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                spaces_needed = maxWidth - line_length
                if len(line) == 1:
                    result.append(line[0] + ' ' * spaces_needed)
                else:
                    gaps = len(line) - 1
                    spaces_between_words = spaces_needed // gaps
                    extra_spaces = spaces_needed % gaps
                    line_str = line[0]
                    for i in range(1, len(line)):
                        spaces = spaces_between_words + (1 if extra_spaces > 0 else 0)
                        line_str += ' ' * spaces + line[i]
                        extra_spaces -= 1

                    result.append(line_str)

                line, line_length = [word], len(word)

        result.append(' '.join(line).ljust(maxWidth))
        return result
