import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

#import data using pandas
data = pd.read_csv("epa-sea-level.csv")

#create scatter plot using matplotlib
plt.scatter(data["Year"], data["CSIRO Adjusted Sea Level"])

#get the line of best fit using linregress
slope, intercept, r_value, p_value, std_err = linregress(data["Year"], data["CSIRO Adjusted Sea Level"])

#plot the line of best fit for the entire dataset
x = [1880, 2050]
y = [intercept + slope * x[0], intercept + slope * x[1]]
plt.plot(x, y, color='red', label='Line of best fit')

#get the line of best fit using only data from 2000 onwards
data_2000 = data[data["Year"] >= 2000]
slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(data_2000["Year"], data_2000["CSIRO Adjusted Sea Level"])

#plot the line of best fit for the data from 2000 onwards
x_2000 = [2000, 2050]
y_2000 = [intercept_2000 + slope_2000 * x_2000[0], intercept_2000 + slope_2000 * x_2000[1]]
plt.plot(x_2000, y_2000, color='green', label='Line of best fit (2000 onwards)')

#add labels and title to the plot
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")
plt.legend()
plt.show()
