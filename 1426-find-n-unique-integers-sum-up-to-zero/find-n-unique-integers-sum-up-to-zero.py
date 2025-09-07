class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n&1:
            for i in range(1,n//2+1):
                result.append(-1*i)
                result.append(i)
            result.append(0)
        else:
            for i in range(1,n//2+1):
                result.append(-1*i)
                result.append(i)
            
        return result
            