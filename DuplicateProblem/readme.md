# The Great Animal Race Duplicate Dilemma

Welcome to "The Great Animal Race Duplicate Dilemma" project! This whimsical and engaging Python programming challenge combines fun storytelling with a practical coding exercise, designed to improve your understanding of data structures and algorithms in a playful context.

## Overview

In the enchanting world of Faraway Land, the much-anticipated annual Great Animal Race is about to commence. Each animal participant, from the swift fox to the mighty elephant, is assigned a unique number on their racing bib. However, a mix-up in bib distribution has led to some animals wearing the same number, creating a potential for confusion and chaos at the start of the race. Your mission, should you choose to accept it, is to help the race organizers identify any duplicate numbers to ensure a fair and orderly race.

## Problem Statement

A group of animals, each with a number on their racing bibs, are lined up at the starting line for the Great Animal Race. Due to an unfortunate mix-up, some animals have ended up wearing bibs with the same number. The organizers must identify any duplicates before the race can proceed.

Your task is to write a Python function that checks for duplicate numbers among the animals' bibs. If any number appears more than once, the function should return `True`, indicating that there are duplicates and the race cannot start. If all numbers are unique, the function returns `False`, and the race can begin.

### Visualization

![The Great Animal Race](/DuplicateProblem/bibs.webp)

*Note: Illustration is a whimsical depiction of the diverse array of animals at the starting line, showcasing the vibrant and chaotic scene just before the race begins.*

## Python Solution

```python
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
```

This solution utilizes a `set` to keep track of the numbers (bib numbers) we've seen so far. As we iterate through the list of bib numbers (`nums`), we check if a number is already in the set. If it is, we've identified a duplicate, indicating a problem. If we complete the iteration without finding any duplicates, the race can safely begin.

## How to Use

1. **Clone the repository** to your local machine to get started with the challenge.
2. **Run the Python script** with different arrays of numbers to test for duplicates.
3. **Modify and experiment** with the code to explore different scenarios or to optimize the solution.

## Contributing

We welcome contributions to "The Great Animal Race Duplicate Dilemma" project! Whether you have an improvement to the existing code, additional test cases, or even new and creative problem statements, we would love to see your input.

Please read through our contribution guidelines before submitting your pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Have Fun!

We hope you enjoy solving "The Great Animal Race Duplicate Dilemma" as much as we enjoyed creating it. Happy coding, and may the best animal win!