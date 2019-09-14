def rotate_array(arr: list, rot: int) -> list:
    split = rot % len(arr)
    index = len(arr) - split
    return arr[index:] + arr[:index]
