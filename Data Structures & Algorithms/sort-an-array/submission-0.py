class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge_sort(a):
            if len(a) <= 1:
                return a
            
            mid = len(a) // 2
            left, right = merge_sort(a[:mid]), merge_sort(a[mid:])

            out, i, j = [], 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    out.append(left[i])
                    i += 1
                else:
                    out.append(right[j])
                    j += 1
            out.extend(left[i:])
            out.extend(right[j:])
            return out
        return merge_sort(nums)