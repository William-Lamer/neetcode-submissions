class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # stack is (temp, index)
        res = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                _, index = stack.pop()
                res[index] = i - index
            
            stack.append((temp, i))
        
        for _, index in stack:
            res[index] = 0
        
        return res


