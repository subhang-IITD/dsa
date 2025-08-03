class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        
        minHeap = []

        for num, frq in freq.items():
            heapq.heappush(minHeap,(frq,num))
        
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        result = []
        while minHeap:
            frq , num = heapq.heappop(minHeap)
            result.append(num)
        return result