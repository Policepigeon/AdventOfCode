def calculate_distance(left_list, right_list):
    # Sort both lists before calculating the distance
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)

    # Calculate the difference between corresponding elements in both lists
    distances = [abs(sorted_left[i] - sorted_right[i]) for i in range(min(len(sorted_left), len(sorted_right)))]


    return sum(distances)

def main():
    with open('/home/policepigeon/Documents/code/AdventOfCode/2024/2024⁄01.txt', 'r') as f:
        puzzle_input = [int(x) for x in f.read().split()]

    left_list, right_list = puzzle_input[:len(puzzle_input)//2], puzzle_input[len(puzzle_input)//2:]
    
    distance = calculate_distance(left_list, right_list)
    print(distance)

if __name__ == "__main__":
    main()