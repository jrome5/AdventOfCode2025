'''
Examine map of papers. count if the surrounding 8 squares have less than 4 papers. 
'''
def count_valid(lines):
    valid_count = 0
    kernel = []
    #count if above, below, left, right, diagonals have less than 4
    for i, line in enumerate(lines):
        for j, space in enumerate(line):
            roll_count = 0
            if space == '.':
                continue

            #count above 3
            if i != 0:
                above_line = lines[i-1]
                start = max(0, j-1)
                end = min(j+1, len(line)-1) +1
                roll_count += above_line[start:end].count('@')
                count = above_line[start:end].count('@')
            #count below 3
            if i != len(lines)-1:
                below_line = lines[i+1]
                start = max(0, j-1)
                end = min(j+1, len(line)-1) +1
                roll_count += below_line[start:end].count('@')
                count = below_line[start:end].count('@')

            # count adjacent 2
            if j > 0:
                roll_count += line[j-1] == '@'
            if j < len(line)-1:
                roll_count += line[j+1] == '@'
            if roll_count < 4:
                valid_count += 1
    return valid_count

def main():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        print(count_valid(lines))
    return

if __name__ == "__main__":
    main()