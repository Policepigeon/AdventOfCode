import csv

with open('/home/policepigeon/Documents/code/AdventOfCode/2024/2024/01.txt', 'r') as input_file:
    reader = csv.reader(input_file)
    data = list(reader)

# Split the data into two lists
left_column = [row[0] for row in data]
right_column = [row[1] for row in data]

# Create output files
with open('/home/policepigeon/Documents/code/AdventOfCode/2024/2024/02.txt', 'w') as left_file, open('/home/policepigeon/Documents/code/AdventOfCode/2024/2024/03.txt', 'w') as right_file:
    # Write the elements from the left list to one file
    left_file.write('\n'.join(left_column) + '\n')
    # Write the elements from the right list to another file
    right_file.write('\n'.join(right_column) + '\n')
    /home/policepigeon/Documents/code/AdventOfCode/2024/2024⁄01.txt