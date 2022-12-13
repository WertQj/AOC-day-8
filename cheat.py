# %% [markdown]
# ## --- Day 8: Treetop Tree House ---
#
# The expedition comes across a peculiar patch of tall trees all planted
# carefully in a grid. The Elves explain that a previous expedition planted
# these trees as a reforestation effort. Now, they're curious if this would be a
# good location for a [tree house](https://en.wikipedia.org/wiki/Tree_house).
#
# First, determine whether there is enough tree cover here to keep a tree house
# **hidden**. To do this, you need to count the number of trees that are
# **visible from outside the grid** when looking directly along a row or column.
#
# The Elves have already launched a
# [quadcopter](https://en.wikipedia.org/wiki/Quadcopter) to generate a map with
# the height of each tree (your puzzle input). For example:
#
# ```
# 30373
# 25512
# 65332
# 33549
# 35390
# ```
#
# Each tree is represented as a single digit whose value is its height, where
# `0` is the shortest and `9` is the tallest.
#
# A tree is **visible** if all of the other trees between it and an edge of the
# grid are **shorter** than it. Only consider trees in the same row or column;
# that is, only look up, down, left, or right from any given tree.
#
# All of the trees around the edge of the grid are **visible** - since they are
# already on the edge, there are no trees to block the view. In this example,
# that only leaves the **interior nine trees** to consider:
#
# - The top-left `5` is **visible** from the left and top. (It isn't visible
#   from the right or bottom since other trees of height `5` are in the way.)
# - The top-middle `5` is **visible** from the top and right.
# - The top-right `1` is not visible from any direction; for it to be visible,
#   there would need to only be trees of height **0** between it and an edge.
# - The left-middle `5` is **visible**, but only from the right.
# - The center `3` is not visible from any direction; for it to be visible,
#   there would need to be only trees of at most height `2` between it and an
#   edge.
# - The right-middle `3` is **visible** from the right.
# - In the bottom row, the middle `5` is **visible**, but the `3` and `4` are
#   not.
#
# With 16 trees visible on the edge and another 5 visible in the interior, a
# total of **`21`** trees are visible in this arrangement.
#
# Consider your map; **how many trees are visible from outside the grid?**
#


# %%
from math import prod

def three_dimensional_array(
    rows: int, columns: int, element_size: int
) -> list[list[list[int]]]:
    return [
        [[0 for _ in range(element_size)] for _ in range(columns)] for _ in range(rows)
    ]

def open_input(filename):
    return open(filename, "r", encoding="utf-8").read()


test = """30373
25512
65332
33549
35390"""


def array_grid(grid):
    n = grid.find("\n")
    # entire_grid_size = n**2
    # interior_grid_size = (n - 2) ** 2
    # perimeter_length = n**2 - interior_grid_size
    return [list(map(int, str(x))) for x in grid.splitlines()]


def part_one(grid: str, verbose=False) -> int:
    n = grid.find("\n")
    interior_grid_size = (n - 2) ** 2
    perimeter_length = n**2 - interior_grid_size
    visible = perimeter_length
    array = [list(map(int, str(x))) for x in grid.splitlines()]
    interior_range = range(1, n - 1)

    for y in interior_range:
        for x in interior_range:

            up = max(col[x] for col in array[:y])
            left = max(array[y][:x])

            down = max(col[x] for col in array[y + 1 :])
            right = max(array[y][x + 1 :])

            current_position = array[y][x]

            if any(current_position > quadrant for quadrant in [up, left, down, right]):
                visible += 1

                if verbose:
                    print("Visible")

            elif verbose:
                print("Not visible")

            if verbose:
                pprint.pprint(array)
                print(y, x)
                print(f"  {up}\n{left} {current_position} {right}\n  {down}")
                print()

    return visible


# %%
print(part_one(test))

# %%
input_08 = open_input("input_08.txt")

# %%
# %%time
print(part_one(input_08))