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
    df = load("population_total.csv")

    france = df.set_index('country').loc['France'][:251].apply(clean_data)
    belgium = df.set_index('country').loc['Belgium'][:251].apply(clean_data)

    years = france.index

    plt.plot(years, france, color='g', label='France')
    plt.plot(years, belgium, color='b', label='Belgium')

    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Projections')
    plt.legend(loc='lower right')
    plt.xticks(years[::40])
    plt.yticks([20, 40, 60], ['20M', '40M', '60M'])

    plt.show()


if __name__ == "__main__":
    main()
