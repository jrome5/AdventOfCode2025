'''
split up input by comma
split again by dash
check if an ID is valid - cant have repeating numbers anywhere
sum all invalid IDs
'''
def check_password(n):
    #perform sliding window checking for repeating numbers. window from 1 to len/2
    num_windows = len(n)//2
    for window_size in range(1,num_windows+1):
        if len(n) % window_size != 0:
            continue
        slides = len(n) // window_size - 1
        valid = False
        target = int(n[0:window_size])
        for s in range(slides):
            start = (s+1)*window_size
            end = (s+2)*window_size
            r = n[start:end]
            if int(r) != target:
                #valid, can continue
                valid = True
                break
        if not valid:
            print(f'{n} invalid with {target}')
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
            r = int(r)+1
            for n in range(l,r):
                invalid = check_password(str(n))
                if invalid:
                    total += int(n)
        print(total)

        