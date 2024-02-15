def count_in_list(lst: list, to_count) -> int:
    count = 0
    for item in lst:
        if item == to_count:
            count += 1
    return (count)
