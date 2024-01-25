def callLimit(limit: int):
    """
    Un décorateur qui limite le nombre de fois qu'une fonction peut être
    appelée.

    Args:
        limit (int): Le nombre maximal d'appels autorisés pour la fonction
        décorée.

    Returns:
        Callable: Un décorateur qui applique la limite d'appel à une fonction
        donnée.

    Exemple:
        @callLimit(3)
        def ma_fonction():
            ...
    """
    count = 0

    def callLimiter(function):
        """
        Un décorateur interne qui applique la limite d'appel à la fonction
        spécifiée.

        Args:
            function (Callable): La fonction à laquelle la limite d'appels sera
            appliquée.

        Returns:
            Callable: La fonction modifiée avec la logique de limitation
            d'appel.
        """
        def limit_function(*args, **kwds):
            """
            La fonction modifiée qui inclut la logique de limitation d'appel.

            Incrémente un compteur à chaque appel et compare ce compteur à la
            limite spécifiée.
            Si la limite est atteinte, une exception est levée. Sinon, la
            fonction originale est appelée avec les arguments fournis.

            Args:
                *args: Arguments positionnels passés à la fonction originale.
                **kwds: Arguments nommés passés à la fonction originale.

            Returns:
                Any: Le résultat de la fonction originale, si la limite n'est
                pas atteinte.

            Raises:
                Exception: Si le nombre d'appels dépasse la limite spécifiée.
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                raise Exception(f"Error: {function} call too many times")

        return limit_function

    return callLimiter
