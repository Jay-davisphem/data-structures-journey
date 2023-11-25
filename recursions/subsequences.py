def print_sub_r(i: int, ds: list[object], arr: list[object]):
    s = "\t" * i
    if i == len(arr):
        print(f"{s}r({i}, {ds}, {arr}) -><- ")
        print(ds)
        return
    print(f"{s}r({i}, {ds}, {arr}) -> ")
    ds.append(arr[i])
    print_sub_r(i + 1, ds, arr)

    ds.pop()
    print(f"{s}r({i}, {ds}, {arr}) <- ")
    print_sub_r(i + 1, ds, arr)


def sub_sequences_r(arr: list[object]) -> list[list[object]]:
    # Space complexity: O(2^n)
    # Time complexity: O(2^n)
    if len(arr) == 0:
        return [[]]
    else:
        sub_seqs = sub_sequences_r(arr[1:])
        return [[arr[0]] + sub_seq for sub_seq in sub_seqs] + sub_seqs


def sub_sequences_r1(arr: list[object], i: int = 0) -> list[list[object]]:
    # Space complexity: O(2^n)
    # Time complexity: O(2^n)
    if i == len(arr):
        return [[]]
    sub_sequences = sub_sequences_r1(arr, i + 1)
    #  return [[arr[i]] + sub_sequence for sub_sequence in sub_sequences] + sub_sequences

    temp = []
    for sub_seq in sub_sequences:
        temp.append([arr[i]] + sub_seq)
    return temp + sub_sequences


print(sub_sequences_r1([3, 1, 2], 0))

# print_sub_r(0, [], [3, 1, 4])
