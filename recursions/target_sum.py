def target_sum(arr: list[int], target: int):
    res = []

    def t_sum(arr: list[int], target: int, i=0, _sum=0, ds=[]) -> list[list[int]]:
        if i == len(arr):
            if target == _sum:
                # res.append(ds)
                # print(ds)
                # print(res, i)
                return [ds]
            return

        sub = t_sum(arr, target)
        ds.append(arr[i])
        _sum += arr[i]
        t_sum(arr, target, i + 1, _sum, ds)

        ds.pop()
        _sum -= arr[i]
        t_sum(arr, target, i + 1, _sum, ds)

    a = t_sum(arr, target)
    return res


arr = [1, 2, 3, 4, 5, 6]
print(target_sum(arr, 5))
