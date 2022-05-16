import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x_prediction = pd.Series(i for i in range(1880,2051))
    y_prediction = res.slope*x_prediction + res.intercept
    plt.plot(x_prediction,y_prediction, color = 'r')

    # Create second line of best fit
    df2 = df[df['Year']>=2000]

    x_df2 = df2['Year']
    y_df2 = df2['CSIRO Adjusted Sea Level']

    res2 = linregress(x_df2, y_df2)

    x_prediction2 = pd.Series(i for i in range(2000,2051))
    y_prediction2 = res2.slope*x_prediction2 + res2.intercept
    plt.plot(x_prediction2,y_prediction2, color = 'g')



    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()