from load_csv import load
import matplotlib.pyplot as plt
import matplotlib as mplt
mplt.use("TkAgg")

def main():
    try:
        data = load('life_expectancy_years.csv')
        if (data is None):
            return
        France = data[data['country'] == 'France']

        France = France.drop(columns=['country'])

        # recuperation des anneés dans une liste
        x = France.columns.tolist()

        # recuperation des valeurs dans une liste
        y = France.iloc[0].values.tolist()

        # taille du graphique
        plt.figure(figsize=(15, 5))

        # label c'est le titre, linestyle c'est pour avoir une ligne continue
        plt.plot(x, y, label='France', linestyle='-')

        # description du graphique
        plt.title('France Life expectancy Projections')
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')

        # je precise que j'affiche les anneés tous les 50 ans
        plt.xticks(x[::50], rotation=45)
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(e)
        return


if __name__ == '__main__':
    main()
