from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges nums2 into nums1 as a sorted array in-place.
        """
        i = m - 1  # nums1's index (the actual nums)
        j = n - 1  # nums2's index
        k = m + n - 1  # nums1's index (the next filled position)

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

# User Input Handling
if __name__ == "__main__":
    nums1 = list(map(int, input("Enter nums1 with extra space (comma-separated): ").split(',')))
    m = int(input("Enter the number of actual elements in nums1: "))
    nums2 = list(map(int, input("Enter nums2 (comma-separated): ").split(',')))
    n = int(input("Enter the number of elements in nums2: "))
    
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print("Merged array:", nums1)