from typing import List

class SortingEngine:
    """
    Reference implementations of O(n log n) and O(n^2) sorting algorithms.
    Demonstrates algorithmic logic in Python 3.10+
    """

    @staticmethod
    def quick_sort(arr: List[int]) -> List[int]:
        """
        Complexity: O(n log n)
        Strategy: Divide and Conquer (Pivot)
        """
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr.pop()
            greater_than_pivot = []
            lesser_than_pivot = []
            
            for item in arr:
                if item > pivot:
                    greater_than_pivot.append(item)
                else:
                    lesser_than_pivot.append(item)
            
            return (SortingEngine.quick_sort(lesser_than_pivot) + 
                    [pivot] + 
                    SortingEngine.quick_sort(greater_than_pivot))

    @staticmethod
    def merge_sort(arr: List[int]) -> List[int]:
        """
        Complexity: O(n log n)
        Strategy: Recursive Merge
        """
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = SortingEngine.merge_sort(arr[:mid])
        right = SortingEngine.merge_sort(arr[mid:])

        return SortingEngine._merge(left, right)

    @staticmethod
    def _merge(left: List[int], right: List[int]) -> List[int]:
        sorted_arr = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
        
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        return sorted_arr

# Example Usage
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {data}")
    print(f"Sorted:   {SortingEngine.quick_sort(data)}")
