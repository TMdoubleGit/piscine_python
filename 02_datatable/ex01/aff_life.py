from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    This program loads the French life expectancy from 1800
    and makes projections until 2100.
    """
    df = load("life_expectancy.csv")

    france_data = df[df['country'] == 'France']
    years = france_data.columns[1:]
    life_expectancy = france_data.values[0][1:]

    plt.plot(years, life_expectancy)

    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title('France Life expectancy Projections')
    plt.xticks(years[::40])

    plt.show()


if __name__ == "__main__":
    main()
