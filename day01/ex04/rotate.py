import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def display_img_inf(img_array: np.array):
    """
    Display image information.
    """
    height, width, channels = img_array.shape
    print(f"The shape of image is: ({height}, {width}, {channels})"
          " or {height} {width}")
    return img_array


def turn_grey(img_array: np.array):
    """
    Turn image to grey.
    """
    gray_sub_img = np.dot(img_array[..., :3], [0.299, 0.587, 0.114])
    gray_sub_img = np.round(gray_sub_img).astype(int)
    gray_sub_img = gray_sub_img[:, :, np.newaxis]
    return gray_sub_img


def zoom_image(img_array: np.array, new_shape: tuple):
    """
    Returns position y, x of crop image.
    """
    y, x, _ = img_array.shape
    start_y = y//2 - new_shape[0]//2
    start_x = x//2 - new_shape[1]//2

    return start_y, start_x


def ft_transpose(image_array: np.array):
    """
    Transpose the image.
    """
    image_array = image_array.squeeze()
    height, width = image_array.shape
    transposed = np.zeros((width, height), dtype=image_array.dtype)
    for i in range(height):
        for j in range(width):
            transposed[j][i] = image_array[i][j]
    return transposed


def main():
    """
    This function will zoom on animal.jpeg and turn it to grey.
    Then rotate it.
    """
    try:
        img = Image.open("animal.jpeg")
        img_array = np.array(img)
        # need to get a new shape (zoom image)
        if img_array.shape[0] < 400 or img_array.shape[1] < 400:
            raise ValueError("Image is too small")

        x, y = zoom_image(img_array, (400, 400))
        sub_img = img_array[x:x+400, y:y+400]
        gray_sub_img = turn_grey(sub_img)
        display_img_inf(gray_sub_img)
        print(gray_sub_img)
        gray_arr = ft_transpose(gray_sub_img)
        print(f"New shape after Transpose: ({gray_arr.shape[0]},"
              f" {gray_arr.shape[1]})")
        print(gray_arr)
        plt.imshow(gray_arr, cmap='gray')
        plt.show()

    except Exception as e:
        print(f"Error: {e}")
        exit()


if __name__ == "__main__":
    main()
