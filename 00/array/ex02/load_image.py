import os
import numpy as np
from PIL import Image


def ft_load(path: str) -> str:
    """
    This function loads an image and prints
    its format and its pixels content in RGB format.
    """
    try:
        img = []
        assert isinstance(path, str), "AssertionError: path is not a string"
        assert path, "AssertionError: path is empty"
        assert os.path.exists(path), "AssertionError: path does not exist"
        assert path.endswith('.jpg') or path.endswith('.jpeg'), \
            "AssertionError: path is not a valid image"

        image = Image.open(path)
        img = np.array(image)
        print(f"The shape of image is : {img.shape}")

        return img

    except AssertionError as e:
        print(e)
        img = "Returning an error message"
        return img
