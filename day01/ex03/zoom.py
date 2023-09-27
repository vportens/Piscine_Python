import numpy as np
from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt


def get_num_channels(img):
    mode_to_channels = {
        "L": 1,       # Grayscale
        "RGB": 3,     # Red, Green, Blue
        "RGBA": 4     # Red, Green, Blue, Alpha (transparency)
        # Vous pouvez ajouter d'autres modes si nécessaire
    }
    return mode_to_channels.get(img.mode, "Unknown mode")


def display_img(zoomed_img: np.array, channel):
    """
    Display the image.
    """

    # grayscale_img = np.mean(zoomed_img, axis=-1).astype(np.uint8)
    grayscale_img = zoomed_img

    # Afficher la forme et le nombre de canaux
    height, width = grayscale_img.shape
    print(f"New shape after slicing: ({height}, {width}, {channel}) or"
          f"({height}, {width})")
    flattened_img = grayscale_img.reshape(-1, 1)
    print(flattened_img)

    plt.imshow(grayscale_img, cmap='gray')

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    y_ticks = range(0, zoomed_img.shape[0]+1, zoomed_img.shape[0]//10)
    x_ticks = range(0, zoomed_img.shape[1]+1, zoomed_img.shape[1]//10)

    plt.yticks(y_ticks, labels=[str(i) for i in y_ticks])
    plt.xticks(x_ticks, labels=[str(i) for i in x_ticks])
    plt.show()


def zoom_image(img_array: np.array, new_shape: tuple):
    """
    Returns a "zoomed" (cropped) version of the image to the given new_shape.
    """
    y, x, _ = img_array.shape
    start_y = y//2 - new_shape[0]//2
    start_x = x//2 - new_shape[1]//2

    return start_y, start_x


def main():
    try:
        img_array = ft_load("animal.jpeg")
        print(img_array)

        img = Image.open("animal.jpeg")

        x, y = zoom_image(img_array, (400, 400))
        img_cro = img.crop((y, x, y + 400, x + 400))
        grayscale_image = img_cro.convert("L")

        channels = get_num_channels(grayscale_image)
        gray_arr = np.array(grayscale_image)
        display_img(gray_arr, channels)
    except Exception:
        raise Exception("Error loading image")


if __name__ == "__main__":
    main()
