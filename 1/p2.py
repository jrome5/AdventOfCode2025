'''
dial 0-99

L turn decreases
R turn increases

numbers wrap

goal: count how many times 0 is visited at any time
'''

def turn_dial(dial, turn):
    direction = turn[0]
    amount = int(turn[1:])

    if direction == "L":
        step = -1
    else:
        step = 1

    zero_count = 0

    #turn dial individually
    for i in range(amount):
        dial += step
        if dial % 100 == 0:
            zero_count += 1

    # #correct for wrap
    while not 100 > dial >= 0:
        if dial < 0:
            dial += 100
        elif dial > 99:
            dial -= 100

    # print(f'passed zero {zero_count} times {current} + {direction} {amount} = {dial}')

    return dial, zero_count

if __name__ == "__main__":
    dial = 50
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        # print(lines)
        password = 0
        for line in lines:
            dial, zero_count = turn_dial(dial, line)
            password += zero_count
            assert 100 >= dial >= 0
    print("password: ", password)