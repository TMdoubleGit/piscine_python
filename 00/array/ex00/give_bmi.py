def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI based on height and weight.

    :param height: List of heights in meters (int or float).
    :param weight: List of weights in kilograms (int or float).
    :return: List of calculated BMIs
    """

    bmi_list = []

    for h, w in zip(height, weight):
        if h <= 0 or w <= 0:
            bmi_list.append(float('NaN'))
        else:
            bmi = w / (h ** 2)
            bmi_list.append(bmi)
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Defines if bmi.item exceeds the limit or not.

    :param bmi: List of bmi (int or float).
    :return: List of bool, giving True if the bmi.item is above limit.
    """
    bool_list = []

    for item in bmi:
        if item != item:
            raise AssertionError("AssertionError: an item within the BMI list is incorrect")
        else:
            bool_list.append(item > limit)
    return bool_list

height = [2.71, 1.15]
weight = [165.3, -2]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
