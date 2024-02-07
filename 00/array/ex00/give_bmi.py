import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI based on height and weight.

    :param height: List of heights in meters (int or float).
    :param weight: List of weights in kilograms (int or float).
    :return: List of calculated BMIs
    """
    try:
        assert len(height) > 0 and len(weight) > 0, \
            "AssertionError: a list is composed of at least one item"
        assert len(height) == len(weight), \
            "AssertionError: len of lists should be equal"
        assert all(isinstance(h, (int, float)) for h in height), \
            "AssertionError: arguments needs to be lists of int or float"
        assert all(isinstance(w, (int, float)) for w in weight), \
            "AssertionError: arguments needs to be lists of int or float"
        assert all(h > 0 and w > 0 for h, w in zip(height, weight)), \
            "AssertionError: elements of list should be positive"

        bmi_list = []

        for h, w in zip(height, weight):
            bmi = w / (h ** 2)
            bmi_list.append(bmi)
        return bmi_list
    except AssertionError as e:
        print(e)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Defines if bmi.item exceeds the limit or not.

    :param bmi: List of bmi (int or float).
    :return: List of bool, giving True if the bmi.item is above limit.
    """
    bool_list = []

    try:
        assert len(bmi) > 0, \
            "AssertionError: a list is composed of at least one item"
        assert all(isinstance(b, (int, float)) for b in bmi), \
            "AssertionError: arguments needs to be lists of int or float"
        assert all(b > 0 or not np.isnan(b) for b in bmi), \
            "AssertionError: an item within the list is incorrect (< 0 or NaN)"
        for item in bmi:
            bool_list.append(item > limit)
        return bool_list
    except AssertionError as e:
        print(e)
        return []


