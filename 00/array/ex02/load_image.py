import os

def ft_load(path: str) -> array:
    """
    This function loads an image and prints
    its format and its pixels content in RGB format.
    """
    try:
        array = []
        assert isinstance(path, str), "AssertionError: path is not a string"
        assert path, "AssertionError: path is empty"
        assert os.path.exists(path), "AssertionError: path does not exist"
        assert path.endswith('.jpg') or path.endswith('.jpeg'), "AssertionError: path is not a valid image"

    except AssertionError as e:
        print(e)
        print("Returning an empty array")
        return array