import os
import re
from typing import List, Tuple
from time import sleep

BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\u001b[0m\033[0m"
BOLD = '\033[1m'
FADED = '\033[2m'
CRANE = '\U0001F3D7'

class CrateStacks:
    def __init__(self, crate_stacks: List[List[str]]):
        self.crate_stacks = crate_stacks

    def pretty_print(self, num: int, source: int = None, destination: int = None):
        sleep(0.2)
        os.system("clear")
        print("\nCurrent state:\n")
        highlight = {
            source : RED,
            destination : BLUE
        }
        emoji = {
            source: CRANE,
            destination: CRANE
        }

        for i, stack in enumerate(self.crate_stacks):
            if num and (i + 1 == destination):
                crate_stack = ' '.join(stack[:-num]) + BLUE + BOLD + ' ' + ' '.join(stack[-num:]) + RESET
            else:
                crate_stack = ' '.join(stack)

            print(f"   {emoji.get(i + 1, ' ')}    {highlight.get(i + 1, FADED)}{i+1} -> {RESET} {crate_stack}")

        print('\n')

    def execute_command_9000(self, command: str):
        num, source, destination = [int(x) for x in re.findall(r'[0-9]+', command)]
        for _ in range(0, num):
            crate_val = self.crate_stacks[source - 1].pop()
            self.crate_stacks[destination - 1].append(crate_val)
            self.pretty_print(1, source, destination)



    def execute_command_9001(self, command: str):
        num, source, destination = [int(x) for x in re.findall(r'[0-9]+', command)]
        crate_vals = self.crate_stacks[source -1 ][-num:]
        self.crate_stacks[destination - 1] += crate_vals
        self.crate_stacks[source - 1] = self.crate_stacks[source - 1][:-num]

        self.pretty_print(num, source, destination)

class Commands:
    def __init__(self, command_list: List[str]):
        self.command_list = command_list

    def __iter__(self):
        return iter(self.command_list)

def parse_input() -> Tuple[CrateStacks, Commands]:
    with open("5-input.txt") as f:
        stack_lines = []
        command_lines = []
        past_break = False
        for line in f.readlines():
            if not line.strip():
                past_break = True
            elif not past_break:
                stack_lines.append(line)
            else:
                command_lines.append(line)

    num_stacks = max([int(x) for x in stack_lines.pop().strip().split("   ")])
    stacks: List[List[str]] = [[] for _ in range(num_stacks)]

    for line in stack_lines[::-1]:
        crate_input_lines = line.strip('\n')
        for i in range(0, len(crate_input_lines), 4):
            if crate_input_lines[i+1].strip():
                stacks[i//4].append(crate_input_lines[i+1])

    return CrateStacks(stacks), Commands(command_lines)



if __name__ == "__main__":
    crate_stacks, stack_commands = parse_input()

    for command in stack_commands: 
        crate_stacks.execute_command_9001(command)    