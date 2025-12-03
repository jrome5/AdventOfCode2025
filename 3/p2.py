'''
each row is a battery bank
each value is a digit of joltage
you can only turn on two batteries at a time
find the largest value produced per bank: ex 1024 is 24
sum the largest values
'''

'''
go through each element and find the 12 largest in order, we can do this recursively until none are left
'''
def find_joltage(battery_pack, count=1):
    if count == 13:
        return None
    largest = 0
    largest_index = 0
    end = len(battery_pack) - (12-count)
    for i in range(end):
        # print(i)
        if int(battery_pack[i]) > largest:
            largest = int(battery_pack[i])
            largest_index = i

    subset = battery_pack[largest_index+1:]
    next_largest = find_joltage(subset, count+1)
    if next_largest is None:
        return largest
    largest = int(str(largest) + str(next_largest))
    return largest



def main():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        total = 0
        for battery_pack in lines:
            joltage = find_joltage(battery_pack)
            print(f"battery pack {battery_pack} has joltage {joltage}")
            total += joltage

        print(total)
    return

if __name__ == "__main__":
    main()