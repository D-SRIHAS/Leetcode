def removeElement(nums, val):
    k = 0  # Pointer for the new position of non-'val' elements
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]  # Overwrite elements instead of deleting
            k += 1  # Move pointer forward
    return k  # Return the new length of the array

# Example test case
nums = [3, 2, 2, 3]
val = 3

new_length = removeElement(nums, val)
print("New length:", new_length)
print("Modified nums:", nums[:new_length])  # Only print the valid part of the array