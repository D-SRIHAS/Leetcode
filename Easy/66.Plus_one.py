from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i, d in reversed(list(enumerate(digits))):
            if d < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # Set current digit to 0 if it was 9

        return [1] + digits  # If all were 9s, add a new leading 1

# Taking user input
user_input = input("Enter digits separated by space: ")
digits = list(map(int, user_input.split()))  # Convert input to a list of integers

solution = Solution()
result = solution.plusOne(digits)

print("Output:", result)
