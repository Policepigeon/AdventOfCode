input_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

lines = input_data.splitlines()
correct = 0
for line in lines:
    numbers = list(map(int, line.split()))
    differences = []
    for i in range(1, len(numbers)):
        differences.append(numbers[i] - numbers[i - 1])

    level = differences[0]
    incorrect_count = 0

    for diff in differences:
        if diff != level:
            incorrect_count += 1
            if incorrect_count > 1:
                break

 

# Split input into lines
lines = input_data.strip().split("\n")

# Initialize safe report counter
safe_count = 0

for line in lines:
    # Convert the line into a list of integers
    levels = list(map(int, line.split()))
    
    # Calculate the differences between adjacent levels
    diffs = []
    for i in range(len(levels) - 1):
        diffs.append(levels[i + 1] - levels[i])
    
    # Check if differences are within the allowed range
    valid_diffs = all(-3 <= diff <= 3 for diff in diffs)
    
    # Check if the sequence is strictly increasing or decreasing
    is_increasing = all(diff > 0 for diff in diffs)
    is_decreasing = all(diff < 0 for diff in diffs)
    
    # Increment safe count if the report is valid
    if valid_diffs and (is_increasing or is_decreasing):
        safe_count += 1
print(incorrect_count)
print(safe_count)
safe_count += correct
print(safe_count)