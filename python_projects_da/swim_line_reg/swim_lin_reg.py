import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.DataFrame({
    'Promedio de altura': [1.88, 1.91, 1.91, 1.94, 1.93, 1.93, 1.92, 1.92, 1.94, 1.91],
    'Promedio 50 libre': [22.74, 22.38, 22.46, 22.18, 22.11, 21.56, 21.68, 21.67, 21.60, 21.51],
    'Year':[1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2021, 2024]
    })
    
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,10))
    lab = 1988
    idx = 0
    for i in range(0,10): 
        if lab == 2016:
            ax.scatter(df['Promedio 50 libre'].iloc[idx], df['Promedio de altura'].iloc[idx], label = str(lab))
            lab += 5
            idx += 1
        elif lab == 2021:
            ax.scatter(df['Promedio 50 libre'].iloc[idx], df['Promedio de altura'].iloc[idx], label = str(lab))
            lab += 3
            idx += 1
        else: 
            ax.scatter(df['Promedio 50 libre'].iloc[idx], df['Promedio de altura'].iloc[idx], label = str(lab))
            lab += 4
            idx += 1

    # Create line of best fit
    sl, intercept, r, p ,se = linregress(df['Promedio 50 libre'], df['Promedio de altura'])
    ax.plot(range(0,24), [sl*(int(i)) + intercept for i in range(0,24 )], 'r')

    # Add labels and title
    ax.set(xlabel= 'Promedio 50 libre (segundos)', ylabel= 'Promedio de altura (metros)')
    plt.xlim([21, 23])
    plt.ylim([1.85, 2.00])
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('swim_line.png')
    
    return plt.gca()

draw_plot()


