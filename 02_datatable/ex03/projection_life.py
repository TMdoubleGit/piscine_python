from load_csv import load
import matplotlib.pyplot as plt


def clean_data(data):
    """
    This function turns all data contained in
    population_total.csv in Million (currently in
    k or M).
    """
    if (data[-1] == "M"):
        return float(data[:-1])
    elif (data[-1] == "k"):
        return float(data[:-1]) / 1000
    else:
        return float(0)


def main():
    """
    This program loads data from life_excpectancy.csv and
    income_per_person_gdppercapita_ppp_inflation_adjusted.csv. It
    displays the projection of life expectancy regarding GDP per
    capita in 1900.
    """
    df_life = load("life_expectancy_years.csv")
    df_gdp =\
        load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    value_life = df_life['1900']
    value_gdp = df_gdp['1900']

    plt.scatter(value_gdp, value_life)

    plt.xlabel('Gross domestic product')
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])

    plt.ylabel('Life Expectancy')
    plt.yticks(range(20, 56, 5))

    plt.title('1900')

    plt.show()


if __name__ == "__main__":
    main()
