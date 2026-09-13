import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,10))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit
    sl, intercept, r, p ,se = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax.plot(range(df['Year'].iloc[0], 2051), [sl*(int(i)) + intercept for i in range(df['Year'].iloc[0],2051)], 'r')

    # Create second line of best fit
    sl1, intercept1, r, p ,se = linregress(df.loc[df['Year']>=2000, 'Year'], df.loc[df['Year']>= 2000, 'CSIRO Adjusted Sea Level'])
    ax.plot(range(2000, 2051), [sl1*(int(i)) + intercept1 for i in range(2000,2051)], 'r')

    # Add labels and title
    ax.set(xlabel= 'Year', ylabel= 'Sea Level (inches)', title= 'Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    
    return plt.gca()

draw_plot()