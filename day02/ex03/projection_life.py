from load_csv import load
import matplotlib.pyplot as plt
import matplotlib as mplt
mplt.use("TkAgg")


def main():
    try:
        path2 = ("./income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        path1 = ("./life_expectancy_years.csv")
        data_life_time = load(path1)
        data_gdp = load(path2)
        if (data_life_time is None or data_gdp is None):
            return

        # recuperation de l'anneé 1900 et des contries
        dft_year = data_life_time[['country', str(1900)]]
        dgdp_year = data_gdp[['country', str(1900)]]
        dft_year = dft_year.dropna()
        dgdp_year = dgdp_year.dropna()

        # merge des deux dataframes
        merged_data = dft_year.merge(dgdp_year, on='country',
                                     suffixes=('_life', '_gdp'))

        plt.figure(figsize=(10, 6))
        plt.scatter(merged_data['1900_gdp'], merged_data['1900_life'],
                    alpha=0.5)
        plt.title('Life Expectancy vs GDP in 1900')
        plt.xlabel('GDP in 1900')
        plt.ylabel('Life Expectancy in 1900')
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(e)
        return


if __name__ == '__main__':
    main()
