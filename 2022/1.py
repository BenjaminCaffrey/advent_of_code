from typing import List


# Part 1:
# O(N)
def calculate_max_elf_calories() -> int:
    elven_food: List[List[int]] = []
    cur_elf = []
    with open("1-input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                cur_elf.append(int(line))
            else:
                elven_food.append(cur_elf)
                cur_elf = []
    elven_food_sums = [sum(x) for x in elven_food]
    return max(elven_food_sums)

# Part 2:

# Poor man's max heap... keeps track of max N items
# listify is an O(N) operation
class MaxList:
    def __init__(self):
        self.values = []
        self.limit = 3

    def listify(self, value: int) -> None:
        if len(self.values) < self.limit:
            self.values.append(value)
        else:
            cur_min = min(self.values)
            if value > cur_min:
                for i in range(0, self.limit):
                    if self.values[i] == cur_min:
                        self.values[i] = value 

# O(N * M) = O(N) in this case because M (top number of elves) is constant at 3      
def calculate_max_3_elf_calories() -> int:
    elven_food: List[List[int]] = []
    cur_elf = []
    with open("1-input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                cur_elf.append(int(line))
            else:
                elven_food.append(cur_elf)
                cur_elf = []
    elven_food_sums = [sum(x) for x in elven_food]
    max_list = MaxList()
    for food_sum in elven_food_sums:
        max_list.heapify(food_sum)
    return sum(max_list.values)


if __name__ == "__main__":
    result = calculate_max_elf_calories()
    print(result)

    result = calculate_max_3_elf_calories()
    print(result)