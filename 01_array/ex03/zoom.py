from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    """
    This is the main function of the program.
    The program will load an image from a file,
    then make a zoom using a slicing method, turning
    it to gray color and will display it.
    """
    try:
        path = "animal.jpeg"
        img = ft_load(path)
        if img is None:
            exit(1)

        print(img)

        zoomed_img = img[200:600, 400:800, :1]

        to_print = np.array(zoomed_img)
        print(f"New shape after slicing: {to_print.shape}")
        print(np.array(to_print))
        plt.imshow(zoomed_img, cmap='gray')
        plt.axis('on')
        plt.show()

    except AssertionError as e:
        print(AssertionError.__name__, ":", e)
        exit(1)


if __name__ == "__main__":
    main()
