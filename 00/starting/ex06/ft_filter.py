def ft_filter(function, initial_list):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable
    for which function(item) is true.
    If function is None, return the items that are true.
    """
    filtered_list = [x for x in initial_list if function(x)]
    return (filtered_list)
