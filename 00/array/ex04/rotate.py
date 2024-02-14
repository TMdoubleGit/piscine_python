from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def main():
    """
    This is the main function of the program.
    The program will load an image from a file,
    then make a zoom using a slicing method, turning
    it to gray color, transposes it and will display it.
    """
    try:
        path = "animal.jpeg"
        img = ft_load(path)
        if img is None:
            raise FileNotFoundError("File not found.")

        print (img)

        new_img = img[200:600, 400:800]
        new_img = np.array(list(zip(*new_img)))
        new_img = Image.fromarray(new_img).convert("L")
        print(f"New shape after slicing: {new_img.size}")
        print(np.array(new_img))
        plt.imshow(new_img, cmap='gray')
        plt.axis('on')
        plt.show()
    
    except FileNotFoundError as e:
        print(f"{e}")
        exit(1)

if __name__ == "__main__":
    main()