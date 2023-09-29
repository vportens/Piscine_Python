import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def zoom_image(img_array: np.array, new_shape: tuple):
    """
    Returns position y, x of crop image.
    """
    y, x, _ = img_array.shape
    start_y = y//2 - new_shape[0]//2
    start_x = x//2 - new_shape[1]//2

    return start_y, start_x


def turn_grey(img_array: np.array):
    """
    Turn image to grey.
    """
    gray_sub_img = np.dot(img_array[..., :3], [0.299, 0.587, 0.114])
    gray_sub_img = np.round(gray_sub_img).astype(int)
    gray_sub_img = gray_sub_img[:, :, np.newaxis]
    return gray_sub_img


def main():
    """
    This function take an image and zoom in it and turn it grey.
    """
    try:
        img_array = ft_load("animal.jpeg")
        print(img_array)
        # need to get a new shape (zoom image)
        if img_array.shape[0] < 400 or img_array.shape[1] < 400:
            raise ValueError("Image is too small")

        x, y = zoom_image(img_array, (400, 400))
        sub_img = img_array[x:x+400, y:y+400]
        gray_sub_img = turn_grey(sub_img)

        plt.imshow(gray_sub_img, cmap='gray')
        print("New shape after slicing:", gray_sub_img.shape,
              f"or {gray_sub_img.shape[0]} {gray_sub_img.shape[1]}")
        print(gray_sub_img)
        plt.show()

    except Exception as e:
        print(f"Error: {e}")
        exit()


if __name__ == "__main__":
    main()
