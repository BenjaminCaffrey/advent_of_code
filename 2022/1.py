from typing import List, Optional


# Part 1:
# O(N) where N is the total number of elf snacks
def calculate_max_elf_calories() -> int:
    elven_food: List[List[int]] = []
    cur_elf_food = []
    with open("1-input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                cur_elf_food.append(int(line))
            else:
                elven_food.append(cur_elf_food)
                cur_elf_food = []
    elven_food_sums = [sum(x) for x in elven_food]
    return max(elven_food_sums)

# Part 2:

# Poor man's max heap... keeps track of max N items
# listify is an O(N) operation where N is the number of max items we're tracking
class MaxList:
    def __init__(self, n):
        self.limit = n
        self.values = [0] * self.limit
        self.cur_min: int = 0

    def listify(self, value: int) -> None:
        if value > self.cur_min:
            for i in range(0, self.limit):
                if self.values[i] == self.cur_min:
                    self.values[i] = value 
                    self.cur_min = min(self.values)
                    break

# O(N * M) where N is the total number of elf snacks and M is the number of top elves we're tracking
# O(N) in this case because M (top number of elves) is constant at 3      
def calculate_max_n_elf_calories(n: int) -> int:
    elven_food: List[List[int]] = []
    cur_elf_food = []
    with open("1-input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                cur_elf_food.append(int(line))
            else:
                elven_food.append(cur_elf_food)
                cur_elf_food = []
    elven_food_sums = [sum(x) for x in elven_food]
    max_list = MaxList(n)
    for food_sum in elven_food_sums:
        max_list.listify(food_sum)
    return sum(max_list.values)


if __name__ == "__main__":
    result = calculate_max_elf_calories()
    print(result)

    result = calculate_max_n_elf_calories(3)
    print(result)