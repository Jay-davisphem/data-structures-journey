def reverse_array(arr: list[int]) -> list[int]:
    if len(arr) < 2: return arr
    new = reverse_array(arr[1:])
    new.append(arr[0])
    return new

def reversed_array(arr: list[int]) -> None:
    n = len(arr)
    j = 0
    def reverse(arr: list[int], i: int):
        nonlocal j
        j += 1
        if i >= n//2: return
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
        reverse(arr, i + 1)

    reverse(arr, 0)
    print(j, 'count')
def isPalindrome(s: str) -> bool:
    if len(s) < 2: return True
    if s[0] != s[-1]: return False
    return isPalindrome(s[1:-1])

arr = [1,2,3,4,5,6,7,8]
str = ''
print(reverse_array(arr))
print(isPalindrome(str))
reversed_array(arr)
print(arr)
