def calc_single_item_priority(char: str) -> int:
    LOWERCHAR_OFFSET = 96
    UPPERCHAR_OFFSET = 38
    if char.islower():
        return ord(char) - LOWERCHAR_OFFSET
    else:
        return ord(char) - UPPERCHAR_OFFSET

class Part1:
    def calculate_priority_sum(self):
        priority_sum = 0
        with open("3-input.txt") as f:
            for line in f.readlines():
                line = list(line.strip())
                rucksack_1 = list(line[0:len(line)//2])
                rucksack_2 = list(line[len(line)//2:])
                rucksack_1_contents, rucksack_2_contents = {}, {}

                for i in range(0, len(rucksack_1)):
                    rucksack_1_item = rucksack_1[i]
                    rucksack_1_contents[rucksack_1_item] = True
                    if rucksack_1_item in rucksack_2_contents:
                        priority_sum += calc_single_item_priority(rucksack_1_item)
                        break

                    rucksack_2_item = rucksack_2[i]
                    rucksack_2_contents[rucksack_2_item] = True
                    if rucksack_2_item in rucksack_1_contents:
                        priority_sum += calc_single_item_priority(rucksack_2_item)
                        break

        return priority_sum



class Part2:
    def calculate_priority_sum(self):
        priority_sum = 0
        with open("3-input.txt") as f:
            elf_group_rucksacks = []
            for line in f.readlines():
                line = list(line.strip())
                elf_group_rucksacks.append(line)
                if len(elf_group_rucksacks) == 3:
                    item_frequencies = {}
                    for i, rucksack in enumerate(elf_group_rucksacks):
                        for item in rucksack:
                            item_frequency = item_frequencies.get(item, [False, False, False])
                            item_frequency[i] = True
                            item_frequencies[item] = item_frequency
                            if all(item_frequency):
                                priority_sum += calc_single_item_priority(item)
                                elf_group_rucksacks = []
                                break    

        return priority_sum
    





if __name__ == "__main__":
    pt1 = Part1()
    result = pt1.calculate_priority_sum()
    print(result)

    pt2 = Part2()
    result = pt2.calculate_priority_sum()
    print(result)