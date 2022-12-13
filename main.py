tree_range = []

with open('input.txt', mode='r', encoding='UTF-8') as trees:
    a = trees.readlines()
    for _ in a:
        tree_range.append(_.replace('\n', ''))


def flip(arr):
    flipped = []
    i = 0
    while i < len(arr[0]):
        alpha = ''
        for y in arr:
            alpha += y[i]
        flipped.append(alpha)
        i += 1
    return flipped


new_arr = flip(tree_range)


def beg(arr, y, x):
    try:
        if y == 0 or x == 0 or x == (len(arr[0])-1) or y == (len(arr[0])-1):
            return True
        if arr[y][x] > max(arr[y][:x]) or arr[y][x] > max(arr[y][x + 1:]):
            return True
        if new_arr[x][y] > max(new_arr[x][:y]) or new_arr[x][y] > max(new_arr[x][y+1:]):
            return True
        return False
    except ValueError:
        print(y, x, 'GG')
        raise ValueError


answer = 0

for a in range(len(tree_range[0])):
    for b in range(len(tree_range[0])):
        print(beg(tree_range, a, b), a, b)
        if beg(tree_range, a, b):
            answer += 1

print(answer)


def line_check(t, *lines):
    ml, total = 0, 1
    for line in lines:
        try:
            for tree in line:
                if t > tree:
                    ml += 1
                if t <= tree:
                    ml += 1
                    break
            total, ml = total*ml, 0
        except IndexError:
            total, ml = total*ml, 0
    return total


def sc(arr, y, x):
    t = arr[y][x]
    line_rx = list(arr[y][x+1:])
    line_lx = list(reversed(arr[y][:x]))
    line_by = list(new_arr[x][y+1:])
    line_ty = list(reversed(new_arr[x][:y]))
    return line_check(t, line_lx, line_rx, line_ty, line_by)


max_sc = 0

for a in range(len(tree_range[0])):
    for b in range(len(tree_range[0])):
        current_sc = sc(tree_range, a, b)
        if current_sc > max_sc:
            max_sc = current_sc

print(max_sc)
