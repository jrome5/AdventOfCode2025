'''
split up input by comma
split again by dash
check if an ID is valid - cant have repeating numbers
sum all invalid IDs
'''
def check_password(n):
    midpoint = len(n) // 2 
    l = n[:midpoint]
    r = n[midpoint:]
    if l == r:
        print(f'{n} invalid with {l} = {r}')
        return True
    return False

if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.readlines()
        print(lines)
        lines = [line.split() for line in lines]
        dashed_pairs = []
        for line in lines:
            for l in line:
                split = l.split(',')
                dashed_pairs.extend([s for s in split if len(s) != 0])

        total = 0
        for dp in dashed_pairs:
            [l,r] = dp.split('-')
            l = int(l)
            r = int(r)
            for n in range(l,r):
                invalid = check_password(str(n))
                if invalid:
                    total += int(n)
        print(total)

        