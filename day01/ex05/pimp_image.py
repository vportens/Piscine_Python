import matplotlib.pyplot as plt


def ft_invert(array):
    # Vérifiez si l'image est en niveaux de gris ou en couleur
    # Image en couleur
    inverted_array = 255 - array

    # Afficher les images côte à côte pour comparer
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(array, cmap='gray' if len(array.shape) == 2 else None)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Inverted Image')
    plt.imshow(inverted_array, cmap='gray' if len(array.shape) == 2 else None)
    plt.axis('off')

    plt.show()

    return inverted_array


def ft_red(array):

    red_copy = array.copy()
    if len(array.shape) == 2:
        return array
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(array, cmap='gray' if len(array.shape) == 2 else None)
    plt.axis('off')

    red_copy[:, :, 1] *= 0  # Mettre à zéro le canal vert
    red_copy[:, :, 2] *= 0  # Mettre à zéro le canal bleu

    plt.subplot(1, 2, 2)
    plt.title('Red Image')
    plt.imshow(red_copy, cmap='gray' if len(array.shape) == 2 else None)
    plt.axis('off')

    plt.show()
    return (red_copy)


def ft_bleu(array):
    # Si l'image est en niveau de gris, elle n'a pas de canaux distincts,
    # donc nous retournons simplement l'image.
    bleu_copy = array.copy()

    if len(array.shape) == 2:
        return array

    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(array, cmap='gray' if len(array.shape) == 2 else None)
    plt.axis('off')

    # Mettre à zéro les canaux rouge et vert
    bleu_copy[:, :, 0] = 0  # Canal rouge
    bleu_copy[:, :, 1] = 0  # Canal vert

    plt.subplot(1, 2, 2)
    plt.title('Bleu Image')
    plt.imshow(bleu_copy, cmap='gray' if len(array.shape) == 2 else None)
    plt.axis('off')
    plt.show()

    return bleu_copy


def ft_green(array):
    # Si l'image est en niveau de gris, elle n'a pas de canaux distincts,
    # donc nous retournons simplement l'image.
    green_copy = array.copy()

    if len(array.shape) == 2:
        return array

    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(array, cmap='gray' if len(array.shape) == 2 else None)
    plt.axis('off')

    # Mettre à zéro les canaux rouge et vert
    green_copy[:, :, 0] = 0  # Canal rouge
    green_copy[:, :, 2] = 0  # Canal bleu

    plt.subplot(1, 2, 2)
    plt.title('Green Image')
    plt.imshow(green_copy, cmap='gray' if len(array.shape) == 2 else None)
    plt.axis('off')
    plt.show()

    return green_copy


def ft_grey(array):
    # Si l'image est déjà en niveau de gris, elle n'a pas de canaux distincts,
    # donc nous retournons simplement l'image.

    grey_copy = array.copy()

    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(array, cmap='gray' if len(array.shape) == 2 else None)
    plt.axis('off')

    if len(array.shape) == 2:
        return array

    # Créer une copie de l'array original

    # Mettre la valeur de rouge partout,
    # on ne peut utiliser que l'operateur = et /.
    # On aurait pu mettre la valeur de vert ou de bleu a la place de rouge
    grey_copy[:, :, 1] = grey_copy[:, :, 0]
    grey_copy[:, :, 2] = grey_copy[:, :, 0]

    plt.subplot(1, 2, 2)
    plt.title('Grey Image')
    plt.imshow(grey_copy, cmap='gray' if len(array.shape) == 2 else None)
    plt.axis('off')
    plt.show()

    return grey_copy
