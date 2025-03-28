from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if i < 1 or num > nums[i - 1]:  # Ensures unique elements
                nums[i] = num
                i += 1
        return i

# Function to take user input and call the solution
def main():
    # Taking input as a space-separated string of numbers
    nums = list(map(int, input("Enter sorted numbers separated by space: ").split()))
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Getting the new length of the array after removing duplicates
    new_length = sol.removeDuplicates(nums)
    
    # Printing results
    print("New length:", new_length)
    print("Modified array:", nums[:new_length])  # Only print the unique part

# Run the program
if __name__ == "__main__":
    main()
