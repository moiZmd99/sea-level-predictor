import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

def draw_plot():
    data = pd.read_csv("epa-sea-level.csv")

    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    slope, intercept, *_ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_all = pd.Series(range(int(data['Year'].min()), 2051))
    line_all = intercept + slope * years_all
    plt.plot(years_all, line_all, color='red', label='Fit: All Years')

    data_2000 = data[data['Year'] >= 2000]
    slope2, intercept2, *_ = linregress(data_2000['Year'], data_2000['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    line_recent = intercept2 + slope2 * years_recent
    plt.plot(years_recent, line_recent, color='green', label='Fit: 2000 onwards')

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.grid(True)

    if not os.path.exists("images"):
        os.makedirs("images")
    plt.savefig("images/sea_level_plot.png")
    plt.show()
