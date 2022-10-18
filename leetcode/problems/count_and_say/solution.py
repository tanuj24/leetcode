class Solution:
    @staticmethod
    def string_grouper(arr):
        curr = arr[0]
        group_final = []
        curr_str = ''
        first = True
        for i in range(len(arr)):
            if arr[i] == curr:
                curr_str+= arr[i]
            else:
                curr = arr[i]
                group_final.append(curr_str)
                curr_str = arr[i]
        group_final.append(curr_str)
        return group_final
    
    @staticmethod
    def pattern(start_with):
        curr = ''.join([str(len(i))+i[0] for i in Solution.string_grouper(list(str(start_with)))])
        # return ''.join(list(map(join_tuple_string, curr)))
        return curr

    def countAndSay(self, n: int) -> str:
        curr = 0
        res = None
        for i in range(1,n+1):
            if i == 1:
                res = str(i)
                curr = n
            elif i == 2:
                res = '11'
                curr = 11
            else:
                res = Solution.pattern(curr)
                curr = Solution.pattern(curr)
        return res