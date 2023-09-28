from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Loads an image, prints its format,
    and returns its pixels content in RGB format.
    """
    try:
        # Open the image file
        img = Image.open(path)

        # Ensure the image is in RGB format
        img_rgb = img.convert("RGB")

        # Convert the image to a numpy array
        img_array = np.array(img_rgb)

        # Print image information
        height, width, channels = img_array.shape
        print(f"The shape of image is: ({height}, {width}, {channels})")

        return img_array
    except Exception as e:
        raise Exception(f"Error loading image {e}")
