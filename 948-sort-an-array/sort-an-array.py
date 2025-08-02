class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap,num)
        
        result = []
        while len(minHeap) > 0:
            result.append(heapq.heappop(minHeap))
        return result
