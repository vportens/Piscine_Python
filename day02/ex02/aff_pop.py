from load_csv import load
import matplotlib.pyplot as plt


def main():
    data = load('../data python piscine/life_expectancy_years.csv')
    if (data is None):
        return
    # recuperation des pays dans une liste
    France = data[data['country'] == 'France']
    France = France.drop(columns=['country'])

    Brazil = data[data['country'] == 'Brazil']
    Brazil = Brazil.drop(columns=['country'])

    cols_to_keep = [str(i) for i in range(1800, 2051)]

    # recuperation des anneés dans une liste
    France = France[cols_to_keep]
    Brazil = Brazil[cols_to_keep]

    xf = France.columns.tolist()
    yf = France.iloc[0].values.tolist()
    xb = Brazil.columns.tolist()
    yb = Brazil.iloc[0].values.tolist()

    plt.figure(figsize=(15, 5))  # Pour agrandir le graphique

    # Tracer la courbe pour la France
    plt.plot(xf, yf, label='France', color='blue')

    # Tracer la courbe pour le Brésil
    plt.plot(xb, yb, label='Brazil', color='green')

    plt.title('Evolution population in France and Brazil')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xticks(xf[::50], rotation=45)
    plt.legend()  # Pour ajouter la légende au graphique
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()

    # # taille du graphique
    # plt.figure(figsize=(15, 5))

    # # label c'est le titre, linestyle c'est pour avoir une ligne continue
    # plt.plot(x, y, label='France', linestyle='-')

    # # description du graphique
    # plt.title('France Life expectancy Projections')
    # plt.xlabel('Year')
    # plt.ylabel('Life expectancy')

    # je precise que j'affiche les anneés tous les 50 ans
    # plt.xticks(x[::50], rotation=45)
    # plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    # plt.tight_layout()
    # plt.show()


if __name__ == '__main__':
    main()
