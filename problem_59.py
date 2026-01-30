# Problem 59: Rotate list by k positions
 def rotate_list(lst, k):
    n = len(lst)
    k = k % n  # handle k > n
    return lst[-k:] + lst[:-k]  # right rotation

numbers = [1, 2, 3, 4, 5]
print(f"Rotated by 2: {rotate_list(numbers, 2)}")
