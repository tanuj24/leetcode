class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequencies = {}
        for i in words:
            if i in frequencies:
                frequencies[i] += 1
            else:
                frequencies[i] = 1
        
        res = [(k,v) for k,v in frequencies.items()]
        res.sort(key = lambda i:(-i[1],i[0]))
        print(res)
        return [k for k,v in res[0:k]]