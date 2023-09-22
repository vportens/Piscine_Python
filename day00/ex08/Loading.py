import sys


def ft_tqdm(iterable, unit='it', desc='', total=None):
    total = total or len(iterable)

    for i, item in enumerate(iterable, 1):
        yield item
        progress = i / total
        bar_length = 63
        filled_length = int(bar_length * progress)
        bar = ('=' * filled_length +
               '>' + '.' * (bar_length - filled_length - 1))
        percent = progress * 100

        sys.stdout.write(f'\r{percent:.1f}%|[{bar}]| {i}/{total}')
        sys.stdout.flush()

    sys.stdout.write('\n')
    sys.stdout.flush()


# Utilisation de ft_tqdm dans un main
def main():
    for _ in ft_tqdm(range(333)):
        pass  # Simuler un traitement


if __name__ == "__main__":
    main()
