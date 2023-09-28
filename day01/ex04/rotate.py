import numpy as np
from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt


def get_num_channels(img):
    """
    Dictionnary mapping image modes to number of channels.
    """
    mode_to_channels = {
        "L": 1,       # Grayscale
        "RGB": 3,     # Red, Green, Blue
        "RGBA": 4     # Red, Green, Blue, Alpha (transparency)
        # Vous pouvez ajouter d'autres modes si nécessaire
    }
    return mode_to_channels.get(img.mode, "Unknown mode")


def display_info(img_array: np.array, channel):
    height, width = img_array.shape
    print(f"The shape of image is: ({height}, {width}, {channel}) or"
          f" ({height}, {width})")
    flattened_img = img_array.reshape(-1, 1)
    print(flattened_img)


def display_info_new(img_array: np.array, channel):
    height, width = img_array.shape
    print(f"The shape of image is: ({height}, {width}, {channel}) or"
          f" ({height}, {width})")
    print(img_array)

def display_img(zoomed_img: np.array, channel):
    """
    Display the image.
    Display detail information about the image.
    """
    zoomed_img = zoomed_img.squeeze()
    display_info_new(zoomed_img, channel)

    # grayscale_img = np.mean(zoomed_img, axis=-1).astype(np.uint8)
    #plt.imshow(zoomed_img, cmap='gray')
    plt.imshow(zoomed_img, cmap='gray')

    y_ticks = range(0, zoomed_img.shape[0]+1, zoomed_img.shape[0]//10)
    x_ticks = range(0, zoomed_img.shape[1]+1, zoomed_img.shape[1]//10)

    plt.yticks(y_ticks, labels=[str(i) for i in y_ticks])
    plt.xticks(x_ticks, labels=[str(i) for i in x_ticks])
    plt.show()


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
    height, width = image_array.shape
    transposed = np.zeros((width, height), dtype=image_array.dtype)
    for i in range(height):
        for j in range(width):
            transposed[j][i] = image_array[i][j]
    return transposed


def main():
    try:
        img_array = ft_load("animal.jpeg")
        # sup le print dans ft_load
        print("test ")
        if img_array.shape[0] < 400 or img_array.shape[1] < 400:
            raise ValueError("Image is too small")

        img = Image.open("animal.jpeg")

        x, y = zoom_image(img_array, (400, 400))
        img_cro = img.crop((y, x, y + 400, x + 400))
        grayscale_image = img_cro.convert("L")

        channels = get_num_channels(grayscale_image)
        gray_arr = np.array(grayscale_image)
        display_info(gray_arr, channels)

        gray_arr = ft_transpose(gray_arr)
        display_img(gray_arr, channels)
    except Exception as e:
        print(f"Error: {e}")
        exit()


if __name__ == "__main__":
    main()
