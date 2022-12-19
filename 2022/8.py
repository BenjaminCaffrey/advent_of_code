from typing import List, Union


class Part1():
    TreePatchType = List[List[List[Union[int, bool]]]]

    def pprint(self, tree_patch: TreePatchType):
        for row in tree_patch:
            print(row)

    def parse_input(self) -> TreePatchType:
        tree_patch = []
        with open ("8-input.txt") as f:
            for line in f.readlines():
                tree_patch.append([[int(x), False] for x in list(line.strip())])
        return tree_patch

    # All trees are initialized to visible = False, but check each direction
    # for visibility and mark them as appropriate
    def mark_hidden_trees(self, tree_patch) -> None:
        # From left
        for row in tree_patch:
            cur_min = -1
            for tree in row:
                if tree[0] > cur_min:
                    tree[1] = True
                    cur_min = tree[0]

        # From right
        for row in tree_patch:
            cur_min = -1
            for tree in row[::-1]:
                if tree[0] > cur_min:
                    tree[1] = True
                    cur_min = tree[0]

        # From top
        for i in range(0, len(tree_patch[0])):
            cur_min = -1
            for j in range(0, len(tree_patch)):
                tree = tree_patch[j][i]
                if tree[0] > cur_min:
                    tree[1] = True
                    cur_min = tree[0]

        # From bottom
        for i in range(0, len(tree_patch[0])):
            cur_min = -1
            for j in range(len(tree_patch) - 1, -1, -1):
                tree = tree_patch[j][i]
                if tree[0] > cur_min:
                    tree[1] = True
                    cur_min = tree[0]

    def count_visible_trees(self, tree_patch) -> int:
        num_visible = 0
        for row in tree_patch:
            for tree in row:
                if tree[1]:
                    num_visible += 1
        return num_visible


class Part2():
    class TreeType():
        def __init__(self, height: int):
            self.height = height
            self.trees_left: int = 0
            self.trees_right: int = 0
            self.trees_up: int = 0
            self.trees_down: int = 0
        def __repr__(self):
            return f"_{self.height}_ |{self.trees_left}|{self.trees_right}|{self.trees_up}|{self.trees_down}|"

    TreePatchType = List[List[TreeType]]

    def pprint(self, tree_patch: TreePatchType):
        for row in tree_patch:
            print(row)

    def parse_input(self) -> TreePatchType:
        tree_patch = []
        with open ("8-input.txt") as f:
            for line in f.readlines():
                tree_patch.append([self.TreeType(int(x)) for x in list(line.strip())])
        return tree_patch

    def count_visible_trees(self, tree_patch: TreePatchType):
        # left
        for row in tree_patch:
            for index, cur_tree in enumerate(row):
                trees_visible_to_edge = 0
                compare_index = index - 1
                while compare_index >= 0 and row[compare_index].height < cur_tree.height:
                    trees_visible_to_edge += 1
                    compare_index -= 1
                # Final tree blocking further view
                if compare_index >= 0:
                    trees_visible_to_edge += 1
                cur_tree.trees_left = trees_visible_to_edge

        # right
        for row in tree_patch:
            row = row[::-1]
            for index, cur_tree in enumerate(row):
                trees_visible_to_edge = 0
                compare_index = index - 1
                while compare_index >= 0 and row[compare_index].height < cur_tree.height:
                    trees_visible_to_edge += 1
                    compare_index -= 1
                # Final tree blocking further view
                if compare_index >= 0:
                    trees_visible_to_edge += 1
                cur_tree.trees_right = trees_visible_to_edge

        # up
        for i in range(0, len(tree_patch[0])): # for each column
            for j in range(0, len(tree_patch)): # for each row in that column
                index = j
                cur_tree = tree_patch[j][i]
                trees_visible_to_edge = 0
                compare_index = index - 1
                while compare_index >= 0 and tree_patch[compare_index][i].height < cur_tree.height:
                    trees_visible_to_edge += 1
                    compare_index -= 1
                # Final tree blocking further view
                if compare_index >= 0:
                    trees_visible_to_edge += 1
                cur_tree.trees_up = trees_visible_to_edge

        # down
        for i in range(0, len(tree_patch[0])): # for each column
            for j in range(len(tree_patch) - 1, -1, -1): # for each row in that column
                index = j
                cur_tree = tree_patch[j][i]
                trees_visible_to_edge = 0
                compare_index = index + 1
                while compare_index < len(tree_patch) and tree_patch[compare_index][i].height < cur_tree.height:
                    trees_visible_to_edge += 1
                    compare_index += 1
                # Final tree blocking further view
                if compare_index < len(tree_patch):
                    trees_visible_to_edge += 1
                cur_tree.trees_down = trees_visible_to_edge

    def calc_greatest_scenic_score(self, tree_patch: TreePatchType):
        max_scenic_score = 0
        for row in tree_patch:
            for tree in row:
                scenic_score = tree.trees_left * tree.trees_right * tree.trees_up * tree.trees_down
                max_scenic_score = max(max_scenic_score, scenic_score)
        return max_scenic_score
if __name__ == "__main__":
    ## Part 1
    # pt1 = Part1()
    # tree_patch = pt1.parse_input()
    # pt1.pprint(tree_patch)

    # pt1.mark_hidden_trees(tree_patch)
    # print("")

    # pt1.pprint(tree_patch)

    # print(pt1.count_visible_trees(tree_patch))

    ## Part 2
    pt2 = Part2()
    tree_patch = pt2.parse_input()
    pt2.pprint(tree_patch)

    pt2.count_visible_trees(tree_patch)
    print("")
    pt2.pprint(tree_patch)

    print(pt2.calc_greatest_scenic_score(tree_patch))

    