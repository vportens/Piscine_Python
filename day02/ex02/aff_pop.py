from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        data = load('../data python piscine/life_expectancy_years.csv')
        if (data is None):
            print("test")
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

    except Exception as e:
        print(e)
        return


if __name__ == '__main__':
    main()
