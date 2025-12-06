'''
given a list of ingredients and ranges, count how many dont fall within the ranges
'''

#we assume the lists are ordered, thats not neccessarily true
def count_fresh(ranges, ingredients):
    fresh = 0
    for i in ingredients:
        for r in ranges:
            dash_index = r.find('-')
            start = int(r[:dash_index])
            end = int(r[dash_index+1:])
        
            # if i < start: #gone too far
                # print(f'{i} not in ranges')
                # break
            if start <= i <= end:
                fresh += 1
                print(f'{i} between {start} and {end}')
                break

    return fresh

def main():
    with open("input.txt") as f:
        lines = f.readlines()
        ingredients = []
        ranges = []
        newline_found = False
        for line in lines:
            line = line.strip()
            if line == '':
                newline_found = True
                continue
            if not newline_found:
                ranges.append(line)
            else:
                ingredients.append(int(line))
        total = count_fresh(ranges, ingredients)
        print(total)
    return

if __name__ == '__main__':
    main()