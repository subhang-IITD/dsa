class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        heap  = []
        counted = Counter(nums)
        for num ,freq in counted.items():
            heapq.heappush(heap,(freq,-num))

        result = []
        while(len(heap)>0):
            freq, num = heapq.heappop(heap)
            for i in range(freq):
                result.append(-num)
        
        return result