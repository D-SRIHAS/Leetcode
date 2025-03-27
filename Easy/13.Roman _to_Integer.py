class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert a Roman numeral to an integer.
        
        :param s: A string representing the Roman numeral
        :return: An integer representation of the Roman numeral
        """
        # Mapping of Roman numerals to their integer values
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        
        ans = 0
        prev_value = 0  # To track the previous numeral value
        
        # Iterate over the Roman numeral string in reverse order
        for char in reversed(s):  
            curr_value = roman[char]
            
            # If the current value is less than the previous, subtract it
            if curr_value < prev_value:  
                ans -= curr_value
            else:  # Otherwise, add it to the result
                ans += curr_value
                
            prev_value = curr_value  # Update the previous value
        
        return ans


# Taking user input
if __name__ == "__main__":
    solution = Solution()
    
    # User input
    roman_numeral = input("Enter a Roman numeral: ").strip().upper()
    
    # Convert and display result
    result = solution.romanToInt(roman_numeral)
    print(f"Integer value: {result}")
