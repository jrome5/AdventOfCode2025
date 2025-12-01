'''
dial 0-99

L turn decreases
R turn increases

numbers wrap

goal: count how many times 0 is visited after a turn
'''



def turn_dial(dial, turn):
    direction = turn[0]
    amount = int(turn[1:])
    if direction == "L":
        dial -= amount
    else:
        dial += amount

    #correct for wrap
    while not 100 > dial >= 0:
        if dial < 0:
            dial += 100
        if dial > 99:
            dial -= 100

    # print(dial)
    return dial

if __name__ == "__main__":
    dial = 50
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        # print(lines)
        zero_count = 0
        for line in lines:
            dial = turn_dial(dial, line)
            zero_count += dial == 0
            assert 100 >= dial >= 0
            print(f'{line}: {dial}')
    print("password: ", zero_count)