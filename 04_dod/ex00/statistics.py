def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    This function takes in *args a quantity of unknown
    number and make the mean, median, quartile, standard
    deviation and variance according to the **kwargs ask.
    """
    try:
        for val in kwargs.values():
            if len(args) == 0:
                print("ERROR")
                continue
            s_arg = sorted(args)
            if val == "mean":
                res = sum(s_arg) / len(args)
                print("mean: ", res)
            elif val == "median":
                res = s_arg[len(args) // 2] \
                    if len(args) % 2 == 1 else s_arg[len(args) // 2 + 1]
                print("median: ", res)
            elif val == "quartile":
                q25 = s_arg[int(0.25 * len(args))]
                q75 = s_arg[int(0.75 * len(args))]
                res = [float(q25), float(q75)]
                print("quartile: ", res)
            elif val == "var" or val == "std":
                mean = sum(s_arg) / len(args)
                var = sum(pow(x - mean, 2) for x in s_arg) / len(args)
                if val == "var":
                    res = var
                    print("var: ", res)
                else:
                    res = var ** 0.5
                    print("std: ", res)
    except Exception as e:
        print(f"ERROR: {e}")
