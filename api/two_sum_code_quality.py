cluster_1 = [ 'correctness', 
'''
# Prompt 1:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return [0, 0]  # Error: Incorrect return statement

# Hint:
# Ensure the return statement returns an empty list or appropriate indices.

# Output:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Prompt 2:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return digs[target-num]  # Error: Returning single index
    digs[num] = index
    index += 1
return []

# Hint:
# Return both indices of the numbers that add up to the target.

# Output:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Prompt 3:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return [index, index]  # Error: Returning the last index twice

# Hint:
# Ensure the return statement returns an empty list or appropriate indices.

# Output:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Prompt 4:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
# Error: Missing return statement

# Hint:
# Ensure there is a return statement to handle the case where no solution is found.

# Output:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Prompt 5:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[target - num] = index  # Error: Storing the target difference as key
    index += 1
return []

# Hint:
# Store the number itself as the key in the dictionary, not the target difference.

# Output:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Prompt 6:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    # Error: Missing update of the dictionary
    index += 1
return []

# Hint:
# Ensure the dictionary is updated with the current number and its index.

# Output:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Prompt 7:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if num in digs:  # Error: Not checking for target difference
        return [index, digs[num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Check for target - num in the dictionary to find the correct pair.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 8:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return [index, index]  # Error: Returning the last index twice

# Hint:
# Ensure the return statement returns an empty list or appropriate indices.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 9:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return [0, 0]  # Error: Incorrect return statement

# Hint:
# Ensure the return statement returns an empty list or appropriate indices.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 10:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Ensure the dictionary and index are correctly initialized and used.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []
''']

cluster_2 = [ 'efficiency', 
'''
# Prompt 1:
# Given the following code:
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):  # Error: Unnecessary nested loop
        if nums[i] + nums[j] == target:
            return [i, j]
return []

# Hint:
# Use a dictionary to store the indices of the elements to avoid the unnecessary nested loop and achieve O(n) time complexity.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 2:
# Given the following code:
digs = []  # Error: Using a list instead of a dictionary
for index, num in enumerate(nums):
    if target - num in digs:  # Error: Inefficient list lookup
        return [index, digs.index(target - num)]
    digs.append(num)
return []

# Hint:
# Use a dictionary for O(1) lookups instead of a list.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 3:
# Given the following code:
for i in range(len(nums)):
    for j in range(len(nums)):  # Error: Inefficient nested loop
        if nums[i] + nums[j] == target and i != j:
            return [i, j]
return []

# Hint:
# Use a dictionary to store the indices of the elements to avoid the unnecessary nested loop and achieve O(n) time complexity.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 4:
# Given the following code:
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):  # Error: Unnecessary nested loop
        if nums[i] + nums[j] == target:
            return [i, j]
return []

# Hint:
# Use a dictionary to store the indices of the elements to avoid the unnecessary nested loop and achieve O(n) time complexity.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 5:
# Given the following code:
digs = {}
for index, num in enumerate(nums):
    for key in digs:  # Error: Inefficient nested loop
        if target - num == key:
            return [index, digs[key]]
    digs[num] = index
return []

# Hint:
# Use a single loop with dictionary lookups to achieve O(n) time complexity.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 6:
# Given the following code:
digs = {}
for i in range(len(nums)):
    if target - nums[i] in digs:
        return [i, digs[target - nums[i]]]
    digs[nums[i]] = i
return []

# Hint:
# Use the index variable to avoid calling range and len functions repeatedly.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 7:
# Given the following code:
digs = {}
for num in nums:
    index = nums.index(num)  # Error: Inefficient index lookup
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []

# Hint:
# Use enumerate to avoid calling the index function repeatedly.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 8:
# Given the following code:
digs = {}
for index, num in enumerate(nums):
    for key in digs:  # Error: Inefficient nested loop
        if target - num == key:
            return [index, digs[key]]
    digs[num] = index
return []

# Hint:
# Use a single loop with dictionary lookups to achieve O(n) time complexity.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 9:
# Given the following code:
digs = []
for index, num in enumerate(nums):
    if target - num in digs:  # Error: Inefficient list lookup
        return [index, digs.index(target - num)]
    digs.append(num)
return []

# Hint:
# Use a dictionary for O(1) lookups instead of a list.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 10:
# Given the following code:
digs = {}
for index, num in enumerate(nums):
    for key in digs:  # Error: Inefficient nested loop
        if target - num == key:
            return [index, digs[key]]
    digs[num] = index
return []

# Hint:
# Use a single loop with dictionary lookups to achieve O(n) time complexity.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []
'''
]

cluster_3 = ['readability',
'''
# Prompt 1:
# Given the following code:
d = {}
i = 0
for n in nums:
    if target-n in d:
        return [i, d[target-n]]
    d[n] = i
    i += 1
return []

# Hint:
# Use meaningful variable names to improve readability.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 2:
# Given the following code:
num_dict = {}
ind = 0
for number in nums:
    if target-number in num_dict:
        return [ind, num_dict[target-number]]
    num_dict[number] = ind
    ind += 1
return []

# Hint:
# Use consistent naming conventions for variables.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 3:
# Given the following code:
numbers = {}
current_index = 0
for number in nums:
    if target-number in numbers:
        return [current_index, numbers[target-number]]
    numbers[number] = current_index
    current_index += 1
return []

# Hint:
# Simplify variable names to make the code more concise.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 4:
# Given the following code:
dictionary = {}
idx = 0
for value in nums:
    if target-value in dictionary:
        return [idx, dictionary[target-value]]
    dictionary[value] = idx
    idx += 1
return []

# Hint:
# Use shorter variable names for better readability.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 5:
# Given the following code:
d = {}
i = 0
for n in nums:
    if target-n in d:
        return [i, d[target-n]]
    d[n] = i
    i += 1
return []

# Hint:
# Use meaningful variable names to improve readability.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 6:
# Given the following code:
num_dict = {}
ind = 0
for number in nums:
    if target-number in num_dict:
        return [ind, num_dict[target-number]]
    num_dict[number] = ind
    ind += 1
return []

# Hint:
# Use consistent naming conventions for variables.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 7:
# Given the following code:
numbers = {}
current_index = 0
for number in nums:
    if target-number in numbers:
        return [current_index, numbers[target-number]]
    numbers[number] = current_index
    current_index += 1
return []

# Hint:
# Simplify variable names to make the code more concise.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 8:
# Given the following code:
dictionary = {}
idx = 0
for value in nums:
    if target-value in dictionary:
        return [idx, dictionary[target-value]]
    dictionary[value] = idx
    idx += 1
return []

# Hint:
# Use shorter variable names for better readability.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 9:
# Given the following code:
d = {}
i = 0
for n in nums:
    if target-n in d:
        return [i, d[target-n]]
    d[n] = i
    i += 1
return []

# Hint:
# Use meaningful variable names to improve readability.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []

# Prompt 10:
# Given the following code:
num_dict = {}
ind = 0
for number in nums:
    if target-number in num_dict:
        return [ind, num_dict[target-number]]
    num_dict[number] = ind
    ind += 1
return []

# Hint:
# Use consistent naming conventions for variables.

# Output:
digs = {}
index = 0
for num in nums:
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
    index += 1
return []
'''
]

cluster_4 = ['maintainability', 
'''
# Prompt 1:
# Given the following code:
digs = {}
i = 0
for n in nums:
    if target-n in digs:
        return [i, digs[target-n]]
    digs[n] = i
    i += 1
return []

# Hint:
# Refactor the code to use functions for better maintainability.

# Output:
def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

# Prompt 2:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Extract the main logic into a function for better maintainability.

# Output:
def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

# Prompt 3:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Use functions to encapsulate logic and improve maintainability.

# Output:
def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

# Prompt 4:
# Given the following code:
digs = {}
i = 0
for n in nums:
    if target-n in digs:
        return [i, digs[target-n]]
    digs[n] = i
    i += 1
return []

# Hint:
# Refactor the code to use functions for better maintainability.

# Output:
def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

# Prompt 5:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Extract the main logic into a function for better maintainability.

# Output:
def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

# Prompt 6:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Use functions to encapsulate logic and improve maintainability.

# Output:
def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

# Prompt 7:
# Given the following code:
digs = {}
i = 0
for n in nums:
    if target-n in digs:
        return [i, digs[target-n]]
    digs[n] = i
    i += 1
return []

# Hint:
# Refactor the code to use functions for better maintainability.

# Output:
def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

# Prompt 8:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Extract the main logic into a function for better maintainability.

# Output:
def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

# Prompt 9:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Use functions to encapsulate logic and improve maintainability.

# Output:
def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

# Prompt 10:
# Given the following code:
digs = {}
i = 0
for n in nums:
    if target-n in digs:
        return [i, digs[target-n]]
    digs[n] = i
    i += 1
return []

# Hint:
# Refactor the code to use functions for better maintainability.

# Output:
def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []
''']

cluster_5 = ['edge case handling - robustness', 
'''
# Prompt 1:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add edge case handling for empty input lists.

# Output:
if not nums:
    return []
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []

# Prompt 2:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add checks for input types to ensure robustness.

# Output:
if not isinstance(nums, list) or not isinstance(target, int):
    raise TypeError("Invalid input types")
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []

# Prompt 3:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Ensure the code handles duplicate numbers correctly.

# Output:
if not nums:
    return []
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []

# Prompt 4:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add edge case handling for empty input lists.

# Output:
if not nums:
    return []
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []

# Prompt 5:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add checks for input types to ensure robustness.

# Output:
if not isinstance(nums, list) or not isinstance(target, int):
    raise TypeError("Invalid input types")
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []

# Prompt 6:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Ensure the code handles duplicate numbers correctly.

# Output:
if not nums:
    return []
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []

# Prompt 7:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add edge case handling for empty input lists.

# Output:
if not nums:
    return []
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []

# Prompt 8:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add checks for input types to ensure robustness.

# Output:
if not isinstance(nums, list) or not isinstance(target, int):
    raise TypeError("Invalid input types")
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []

# Prompt 9:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Ensure the code handles duplicate numbers correctly.

# Output:
if not nums:
    return []
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []

# Prompt 10:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add edge case handling for empty input lists.

# Output:
if not nums:
    return []
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []
'''
]

cluster_6 = ['error handling',
'''
# Prompt 1:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add error handling to manage unexpected input types.

# Output:
if not isinstance(nums, list) or not all(isinstance(n, int) for n in nums) or not isinstance(target, int):
    raise ValueError("Invalid input: nums must be a list of integers and target must be an integer")
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []

# Prompt 2:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Handle empty lists by returning a meaningful error message.

# Output:
if not nums:
    raise ValueError("Input list nums cannot be empty")
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []

# Prompt 3:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Ensure input validation and handle cases where no solution is found.

# Output:
if not isinstance(nums, list) or not all(isinstance(n, int) for n in nums) or not isinstance(target, int):
    raise ValueError("Invalid input: nums must be a list of integers and target must be an integer")
if not nums:
    raise ValueError("Input list nums cannot be empty")
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
raise ValueError("No solution found")

# Prompt 4:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add type checks for the input to ensure robustness.

# Output:
if not isinstance(nums, list) or not all(isinstance(n, int) for n in nums) or not isinstance(target, int):
    raise ValueError("Invalid input: nums must be a list of integers and target must be an integer")
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []

# Prompt 5:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Handle cases where the list is too short to find a pair.

# Output:
if len(nums) < 2:
    raise ValueError("Input list nums must contain at least two elements")
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []

# Prompt 6:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add error handling for non-integer elements in the list.

# Output:
if not all(isinstance(num, int) for num in nums):
    raise ValueError("All elements in nums must be integers")
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []

# Prompt 7:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Ensure the code gracefully handles cases where no valid pairs are found.

# Output:
if not nums:
    raise ValueError("Input list nums cannot be empty")
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
raise ValueError("No solution found")

# Prompt 8:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add input validation to ensure the list contains integers.

# Output:
if not all(isinstance(num, int) for num in nums):
    raise ValueError("All elements in nums must be integers")
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []

# Prompt 9:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add error handling for unexpected input types.

# Output:
if not isinstance(nums, list) or not all(isinstance(n, int) for n in nums) or not isinstance(target, int):
    raise ValueError("Invalid input: nums must be a list of integers and target must be an integer")
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []

# Prompt 10:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Handle cases where the input list is empty.

# Output:
if not nums:
    raise ValueError("Input list nums cannot be empty")
digs = {}
for index, num in enumerate(nums):
    if target - num in digs:
        return [index, digs[target - num]]
    digs[num] = index
return []
'''
]

cluster_7 = ['documentation',
'''
# Prompt 1:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add comments to explain the logic of the code.

# Output:
# Initialize a dictionary to store the numbers and their indices
digs = {}
# Iterate over the list of numbers
for index, num in enumerate(nums):
    # Check if the complement of the current number is in the dictionary
    if target - num in digs:
        # Return the indices of the two numbers that add up to the target
        return [index, digs[target - num]]
    # Add the current number and its index to the dictionary
    digs[num] = index
# Return an empty list if no solution is found
return []

# Prompt 2:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Document the purpose and usage of the function.

# Output:
def two_sum(nums, target):
    """
    Finds two numbers in nums that add up to target.

    Args:
        nums: A list of integers.
        target: An integer representing the target sum.

    Returns:
        A list of two indices of the numbers that add up to the target.
        Returns an empty list if no solution is found.
    """
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

# Prompt 3:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Use inline comments to explain key steps in the code.

# Output:
digs = {}
for index, num in enumerate(nums):
    # Check if the complement of the current number is in the dictionary
    if target - num in digs:
        # Return the indices of the two numbers that add up to the target
        return [index, digs[target - num]]
    # Add the current number and its index to the dictionary
    digs[num] = index
# Return an empty list if no solution is found
return []

# Prompt 4:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add a docstring to the function to describe its behavior.

# Output:
def two_sum(nums, target):
    """
    Finds two numbers in nums that add up to target.

    Args:
        nums: A list of integers.
        target: An integer representing the target sum.

    Returns:
        A list of two indices of the numbers that add up to the target.
        Returns an empty list if no solution is found.
    """
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

# Prompt 5:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Use comments to explain the initialization and main steps of the code.

# Output:
# Initialize a dictionary to store the numbers and their indices
digs = {}
# Iterate over the list of numbers
for index, num in enumerate(nums):
    # Check if the complement of the current number is in the dictionary
    if target - num in digs:
        # Return the indices of the two numbers that add up to the target
        return [index, digs[target - num]]
    # Add the current number and its index to the dictionary
    digs[num] = index
# Return an empty list if no solution is found
return []

# Prompt 6:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add detailed comments to each part of the code for better understanding.

# Output:
# Initialize a dictionary to store the numbers and their indices
digs = {}
# Iterate over the list of numbers
for index, num in enumerate(nums):
    # Check if the complement of the current number is in the dictionary
    if target - num in digs:
        # Return the indices of the two numbers that add up to the target
        return [index, digs[target - num]]
    # Add the current number and its index to the dictionary
    digs[num] = index
# Return an empty list if no solution is found
return []

# Prompt 7:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Document the function with a clear description of inputs and outputs.

# Output:
def two_sum(nums, target):
    """
    Finds two numbers in nums that add up to target.

    Args:
        nums: A list of integers.
        target: An integer representing the target sum.

    Returns:
        A list of two indices of the numbers that add up to the target.
        Returns an empty list if no solution is found.
    """
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

# Prompt 8:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Use inline comments to explain the purpose of each variable and key steps.

# Output:
digs = {}
for index, num in enumerate(nums):
    # Check if the complement of the current number is in the dictionary
    if target - num in digs:
        # Return the indices of the two numbers that add up to the target
        return [index, digs[target - num]]
    # Add the current number and its index to the dictionary
    digs[num] = index
# Return an empty list if no solution is found
return []

# Prompt 9:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add a docstring to the function to describe its behavior and purpose.

# Output:
def two_sum(nums, target):
    """
    Finds two numbers in nums that add up to target.

    Args:
        nums: A list of integers.
        target: An integer representing the target sum.

    Returns:
        A list of two indices of the numbers that add up to the target.
        Returns an empty list if no solution is found.
    """
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

# Prompt 10:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Use comments to explain the initialization and key steps of the code.

# Output:
# Initialize a dictionary to store the numbers and their indices
digs = {}
# Iterate over the list of numbers
for index, num in enumerate(nums):
    # Check if the complement of the current number is in the dictionary
    if target - num in digs:
        # Return the indices of the two numbers that add up to the target
        return [index, digs[target - num]]
    # Add the current number and its index to the dictionary
    digs[num] = index
# Return an empty list if no solution is found
return []
'''
]

cluster_8 = ['testing',
'''
# Prompt 1:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add test cases to validate the function with different inputs.

# Output:
def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [1, 0]
    assert two_sum([3, 2, 4], 6) == [2, 1]
    assert two_sum([3, 3], 6) == [1, 0]
    assert two_sum([1, 2, 3], 5) == []
    print("All test cases pass")

def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

test_two_sum()

# Prompt 2:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Include edge cases in the test cases to ensure robustness.

# Output:
def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [1, 0]
    assert two_sum([3, 2, 4], 6) == [2, 1]
    assert two_sum([3, 3], 6) == [1, 0]
    assert two_sum([1, 2, 3], 5) == []
    assert two_sum([], 0) == []
    assert two_sum([1], 1) == []
    print("All test cases pass")

def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

test_two_sum()

# Prompt 3:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Validate the function with various test cases including duplicates.

# Output:
def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [1, 0]
    assert two_sum([3, 2, 4], 6) == [2, 1]
    assert two_sum([3, 3], 6) == [1, 0]
    assert two_sum([1, 2, 3], 5) == []
    assert two_sum([1, 1, 2, 2], 4) == [3, 2]
    print("All test cases pass")

def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

test_two_sum()

# Prompt 4:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add unit tests to ensure the function works as expected.

# Output:
def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [1, 0]
    assert two_sum([3, 2, 4], 6) == [2, 1]
    assert two_sum([3, 3], 6) == [1, 0]
    assert two_sum([1, 2, 3], 5) == []
    assert two_sum([5, 5, 5], 10) == [1, 0]
    print("All test cases pass")

def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

test_two_sum()

# Prompt 5:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Include test cases with negative numbers to validate the function.

# Output:
def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [1, 0]
    assert two_sum([3, 2, 4], 6) == [2, 1]
    assert two_sum([3, 3], 6) == [1, 0]
    assert two_sum([-1, -2, -3], -5) == [2, 1]
    print("All test cases pass")

def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

test_two_sum()

# Prompt 6:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add tests with mixed positive and negative numbers.

# Output:
def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [1, 0]
    assert two_sum([3, 2, 4], 6) == [2, 1]
    assert two_sum([3, 3], 6) == [1, 0]
    assert two_sum([-1, -2, 3, 4], 2) == [3, 2]
    print("All test cases pass")

def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

test_two_sum()

# Prompt 7:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Ensure the function is tested with an empty list.

# Output:
def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [1, 0]
    assert two_sum([3, 2, 4], 6) == [2, 1]
    assert two_sum([3, 3], 6) == [1, 0]
    assert two_sum([], 0) == []
    print("All test cases pass")

def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

test_two_sum()

# Prompt 8:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Test the function with lists containing only one element.

# Output:
def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [1, 0]
    assert two_sum([3, 2, 4], 6) == [2, 1]
    assert two_sum([3, 3], 6) == [1, 0]
    assert two_sum([1], 1) == []
    print("All test cases pass")

def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

test_two_sum()

# Prompt 9:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Validate the function with various inputs including edge cases.

# Output:
def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [1, 0]
    assert two_sum([3, 2, 4], 6) == [2, 1]
    assert two_sum([3, 3], 6) == [1, 0]
    assert two_sum([1, 2, 3], 5) == []
    assert two_sum([], 0) == []
    assert two_sum([1], 1) == []
    print("All test cases pass")

def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

test_two_sum()

# Prompt 10:
# Given the following code:
digs = {}
index = 0
for num in nums:
    if target-num in digs:
        return [index, digs[target-num]]
    digs[num] = index
    index += 1
return []

# Hint:
# Add comprehensive test cases to ensure all scenarios are covered.

# Output:
def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [1, 0]
    assert two_sum([3, 2, 4], 6) == [2, 1]
    assert two_sum([3, 3], 6) == [1, 0]
    assert two_sum([1, 2, 3], 5) == []
    assert two_sum([], 0) == []
    assert two_sum([1], 1) == []
    assert two_sum([-1, -2, -3], -5) == [2, 1]
    assert two_sum([1, 1, 2, 2], 4) == [3, 2]
    print("All test cases pass")

def two_sum(nums, target):
    digs = {}
    for index, num in enumerate(nums):
        if target - num in digs:
            return [index, digs[target - num]]
        digs[num] = index
    return []

test_two_sum()
'''             
]

code_quality_clusters = [cluster_1, cluster_2, cluster_3, cluster_4, cluster_5, cluster_6, cluster_7, cluster_8]
