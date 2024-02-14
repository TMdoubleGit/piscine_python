from load_image import ft_load
from PIL import Image
import numpy as np

def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    image = 255 - array
    Image.fromarray(image).show()
    print(image)
    return (image)

def ft_red(array) -> np.ndarray:
    """
    Applies a red filter on the image received.
    """
    image = array.copy()
    image[:, :, 1] = 0
    image[:, :, 2] = 0
    Image.fromarray(image).show()
    print(image)
    return image


def ft_green(array) -> np.ndarray:
    """
    Applies a green filter on the image received.
    """
    image = array.copy()
    image[:, :, 0] = 0
    image[:, :, 2] = 0
    Image.fromarray(image).show()
    print(image)
    return image

def ft_blue(array) -> np.ndarray:
    """
    Applies a blue filter on the image received.
    """
    image = array.copy()
    image[:, :, 0] = 0
    image[:, :, 1] = 0
    Image.fromarray(image).show()
    print(image)
    return image

def ft_grey(array) -> np.ndarray:
    """
    Applies a blue filter on the image received.
    """
    image = np.dot(array[..., :3], [0.299, 0.587, 0.114])
    image = image.astype(np.uint8)
    image = np.stack((image, image, image), axis=-1)
    print(image)
    Image.fromarray(image).show()
    return image


array = ft_load("landscape.jpg")

ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)

print(ft_invert.__doc__)