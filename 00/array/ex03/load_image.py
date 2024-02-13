import os
from PIL import Image


def ft_load(path: str) -> str:
    """
    This function loads an image and prints
    its format and its pixels content in RGB format.
    """
    try:
        pixels = []
        assert isinstance(path, str), "AssertionError: path is not a string"
        assert path, "AssertionError: path is empty"
        assert os.path.exists(path), "AssertionError: path does not exist"
        assert path.endswith('.jpg') or path.endswith('.jpeg'), \
            "AssertionError: path is not a valid image"

        image = Image.open(path)
        mode = image.mode
        print("The shape of image is : (", image.size[1],
              ", ", image.size[0], ", ", len(mode), ")")

        pixels = list(image.getdata())
        pixel_strings = [' '.join(map(str, pixel)) for pixel in pixels]

        pixels_string = '['
        for i, pixel_string in enumerate(pixel_strings):
            if i != 0:
                pixels_string += '\n'
            pixels_string += '[' + pixel_string + ']'
        pixels_string += ']\n'

        lines = pixels_string.split('\n')

        first = '\n'.join(lines[:3])
        last = '\n'.join(lines[-4:])

        to_print = first + '\n' + "    ...    " + '\n' + last

        return to_print

    except AssertionError as e:
        print(e)
        pixels = "Returning an error message"
        return pixels


print(ft_load("animal.jpeg"))