from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# Driver Code
if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    target = int(input("Enter target: "))
    
    sol = Solution()
    result = sol.twoSum(nums, target)
    
    print("Indices:", result)
