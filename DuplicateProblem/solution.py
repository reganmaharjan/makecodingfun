def checkForDuplicateBibs(nums):
    seen_numbers = set()
    for num in nums:
        if num in seen_numbers:
            return True  # A duplicate bib number found
        seen_numbers.add(num)
    return False  # No duplicates, race can start

# Example Usages
print(checkForDuplicateBibs([1, 2, 3, 1]))  # Output: True
print(checkForDuplicateBibs([1, 2, 3, 4]))  # Output: False
print(checkForDuplicateBibs([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output: True