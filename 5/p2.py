'''
given ranges, how many possible values can be found
'''
class Range:
    def __init__(self):
        self.starts = []
        self.ends = []

    def add(self, start, end):
        # if no ranges yet, just add
        if len(self.starts) == 0:
            self.starts.append(start)
            self.ends.append(end)
            return

        new_start, new_end = start, end
        new_starts = []
        new_ends = []
        inserted = False

        for s, e in zip(self.starts, self.ends):
            if e < new_start:
                # current interval is completely before the new one
                new_starts.append(s)
                new_ends.append(e)
            elif new_end < s:
                # current interval is completely after the new one
                if not inserted:
                    new_starts.append(new_start)
                    new_ends.append(new_end)
                    inserted = True
                new_starts.append(s)
                new_ends.append(e)
            else:
                # overlap: merge with new interval
                new_start = min(new_start, s)
                new_end = max(new_end, e)

        # if we never inserted (new range goes at the end)
        if not inserted:
            new_starts.append(new_start)
            new_ends.append(new_end)

        self.starts = new_starts
        self.ends = new_ends

    def __repr__(self):
        return "[" + ", ".join(f"{s}-{e}" for s, e in zip(self.starts, self.ends)) + "]"

    def count(self):
        total = 0
        for s,e in zip(self.starts, self.ends):
            total += e-s + 1 #add start, end, and inbetween
        return total
        
# first create a dict of start/ends
# if any new range has a smaller start and larger end, delete the old
# go through the dict and count
def count_fresh(ranges_list):
    ranges = Range()
    for r in ranges_list:
        dash_index = r.find('-')
        start = int(r[:dash_index])
        end = int(r[dash_index+1:])

        ranges.add(start, end)
    print(ranges)
    return ranges.count()

def main():
    with open("input.txt") as f:
        lines = f.readlines()
        ranges = []
        for line in lines:
            line = line.strip()
            if line == '':
                break
            ranges.append(line)
        total = count_fresh(ranges)
        print(total)
    return

if __name__ == '__main__':
    main()