'''
each row is a battery bank
each value is a digit of joltage
you can only turn on two batteries at a time
find the largest value produced per bank: ex 1024 is 24
sum the largest values
'''

'''
go through each element and find the largest
take a subset after and find the next largest
concatenate and return
'''
def find_largest_value(battery_pack):
    largest = 0
    largest_index = 0
    for i in range(len(battery_pack)-1):
        if int(battery_pack[i]) > largest:
            largest = int(battery_pack[i])
            largest_index = i

    second_largest = 0
    subset = battery_pack[largest_index+1:]
    for i in range(len(subset)):
        if int(subset[i]) > second_largest:
            second_largest = int(subset[i])

    print(f"battery pack {battery_pack} has largest {largest} + {second_largest}")
    largest = int(str(largest) + str(second_largest))
    # print(f"largest is {largest}")
    return largest



def main():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        total = 0
        for battery_pack in lines:
            total += find_largest_value(battery_pack)
        print(total)
    return

if __name__ == "__main__":
    main()