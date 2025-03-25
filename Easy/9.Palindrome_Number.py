class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]

# Example usage
if __name__ == "__main__":
    x = int(input("Enter a number: "))
    solution = Solution()
    if solution.isPalindrome(x):
        print(f"{x} is a palindrome.")
    else:
        print(f"{x} is not a palindrome.")
