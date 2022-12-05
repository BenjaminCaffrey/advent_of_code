def range_envelopes_range(outer_range, inner_range) -> bool:
    return outer_range[0] <= inner_range[0] and outer_range[1] >= inner_range[1]

def ranges_overlap(r1, r2) -> bool:
    r1_in_r2 = (r1[0] >= r2[0] and r1[0] <= r2[1]) or (r1[1] >= r2[0] and r1[1] <= r2[1])
    r2_in_r1 = (r2[0] >= r1[0] and r2[0] <= r1[1]) or (r2[1] >= r1[0] and r2[1] <= r1[1])
    return r1_in_r2 or r2_in_r1
    

class Part1:
    def count_enveloped_ranges(self):
        enveloped_range_count = 0
        with open("4-input.txt") as f:
            for line in f.readlines():
                r1, r2 = line.strip().split(",")
                r1 = [int(x) for x in list(r1.split('-'))]
                r2 = [int(x) for x in list(r2.split('-'))]
                if range_envelopes_range(r1, r2):
                    enveloped_range_count += 1
                elif range_envelopes_range(r2, r1):
                    enveloped_range_count += 1
        return enveloped_range_count

class Part2:
    def count_overlapping_ranges(self):
        overlapping_range_count = 0
        with open("4-input.txt") as f:
            for line in f.readlines():
                r1, r2 = line.strip().split(",")
                r1 = [int(x) for x in list(r1.split('-'))]
                r2 = [int(x) for x in list(r2.split('-'))]
                if ranges_overlap(r1, r2):
                    overlapping_range_count += 1
        return overlapping_range_count


if __name__ == "__main__":
    pt1 = Part1()
    print(pt1.count_enveloped_ranges())

    pt2 = Part2()
    print(pt2.count_overlapping_ranges())
