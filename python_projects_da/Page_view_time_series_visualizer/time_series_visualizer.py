import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df.index = df['date']
df.drop(columns = 'date', inplace=True)
df.index.name = None

# Clean data
df = df.loc[
    (df['value'] >= df['value'].quantile(0.025)) & 
    (df['value'] <= df['value'].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(19,6))
    ax.plot(df.index, df['value'], color = 'red')

    ax.set(xlabel= 'Date', ylabel='Page Views', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    
    ax.grid(False)
    custom_ticks= ['2016-07-01','2017-01-01','2017-07-01','2018-01-01','2018-07-01','2019-01-01','2019-07-01','2020-01-01']
    custom_labels=['2016-07','2017-01','2017-07','2018-01','2018-07','2019-01','2019-07','2020-01']
    plt.xticks(custom_ticks, custom_labels)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    year = []
    month = []
    value = list(df['value'])

    value1 = [0 for _ in range(0,120) ]
    year1 = ['2016' for _ in range(0,120)]
    month1 = ['January' for _ in range(0,30)] + ['February' for _ in range(0,30)] + ['March' for _ in range(0,30)]+ ['April' for _ in range(0,30)]

    for date in df.index:
        year.append(date[0:4])

    for date in df.index:
        month.append(date[5:7])
        
    df_bar = pd.DataFrame({
        'value': value1 + value,
        'year':year1 + year,
        'month':month1 + month, 
    })

    df_bar.loc[df_bar['month']=='01', 'month'] = 'January'
    df_bar.loc[df_bar['month']=='02', 'month'] = 'February'
    df_bar.loc[df_bar['month']=='03', 'month'] = 'March'
    df_bar.loc[df_bar['month']=='04', 'month'] = 'April'
    df_bar.loc[df_bar['month']=='05', 'month'] = 'May'
    df_bar.loc[df_bar['month']=='06', 'month'] = 'June'
    df_bar.loc[df_bar['month']=='07', 'month'] = 'July'
    df_bar.loc[df_bar['month']=='08', 'month'] = 'August'
    df_bar.loc[df_bar['month']=='09', 'month'] = 'September'
    df_bar.loc[df_bar['month']=='10', 'month'] = 'October'
    df_bar.loc[df_bar['month']=='11', 'month'] = 'November'
    df_bar.loc[df_bar['month']=='12', 'month'] = 'December'
        
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10,10)) 

    w = 0.05
    
    bar1 = [i for i in range(0,4)]
    bar2 = [i+w for i in bar1]
    bar3 = [i+w for i in bar2]
    bar4 = [i+w for i in bar3]
    bar5 = [i+w for i in bar4]
    bar6 = [i+w for i in bar5]
    bar7 = [i+w for i in bar6]
    bar8 = [i+w for i in bar7]
    bar9 = [i+w for i in bar8]
    bar10 = [i+w for i in bar9]
    bar11 = [i+w for i in bar10]
    bar12 = [i+w for i in bar11]

    monthlst = []

    months2 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    y = ['2016', '2017', '2018', '2019']

    for i in y:
        for _ in months2:
            avglst = df_bar.loc[(df_bar['month'] == _ ) & (df_bar['year'] == i)]
            monthlst.append(round(avglst['value'].mean(), 2))
    

    plt.bar(bar1, monthlst[0:48:12] , w,label = 'January')
    plt.bar(bar2, monthlst[1:48:12], w, label='February')
    plt.bar(bar3, monthlst[2:48:12] , w,label = 'March')
    plt.bar(bar4, monthlst[3:48:12], w, label='April')
    plt.bar(bar5, monthlst[4:48:12] , w,label = 'May')
    plt.bar(bar6, monthlst[5:48:12], w, label='June')
    plt.bar(bar7, monthlst[6:48:12] , w,label = 'July')
    plt.bar(bar8, monthlst[7:48:12], w, label='August')
    plt.bar(bar9, monthlst[8:48:12] , w,label = 'September')
    plt.bar(bar10, monthlst[9:48:12], w, label='October')
    plt.bar(bar11, monthlst[10:48:12] , w,label = 'November')
    plt.bar(bar12, monthlst[11:48:12], w, label='December')
    
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.xticks(bar6, y)
    plt.legend(title='Months')
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    
    return fig



def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    year = []
    month = []
    value = list(df['value'])

    value1 = [0 for _ in range(0,120) ]
    year1 = ['2016' for _ in range(0,120)]
    month1 = ['January' for _ in range(0,30)] + ['February' for _ in range(0,30)] + ['March' for _ in range(0,30)]+ ['April' for _ in range(0,30)]

    for date in df.index:
        year.append(date[0:4])

    for date in df.index:
        month.append(date[5:7])
        
    df_bar = pd.DataFrame({
        'value': value1 + value,
        'year':year1 + year,
        'month':month1 + month, 
    })

    df_bar.loc[df_bar['month']=='01', 'month'] = 'January'
    df_bar.loc[df_bar['month']=='02', 'month'] = 'February'
    df_bar.loc[df_bar['month']=='03', 'month'] = 'March'
    df_bar.loc[df_bar['month']=='04', 'month'] = 'April'
    df_bar.loc[df_bar['month']=='05', 'month'] = 'May'
    df_bar.loc[df_bar['month']=='06', 'month'] = 'June'
    df_bar.loc[df_bar['month']=='07', 'month'] = 'July'
    df_bar.loc[df_bar['month']=='08', 'month'] = 'August'
    df_bar.loc[df_bar['month']=='09', 'month'] = 'September'
    df_bar.loc[df_bar['month']=='10', 'month'] = 'October'
    df_bar.loc[df_bar['month']=='11', 'month'] = 'November'
    df_bar.loc[df_bar['month']=='12', 'month'] = 'December'

    months2 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    df_box = df_bar.copy()

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(25,8))

    sns.boxplot(data = df_box, x='year', y='value', ax=ax1)
    sns.boxplot(data = df_box, x='month', y='value', ax=ax2)


    #ax1.boxplot(dat1, widths=0.8, tick_labels=['2016', '2017', '2018', '2019'], patch_artist=True)
    ax1.set(xlabel='Year', ylabel='Page Views', title='Year-wise Box Plot (Trend)')
    ax1.set_yticks(range(0,220000, 20000))

    #ax2.boxplot(dat2, widths=0.8, tick_labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], patch_artist=True)
    ax2.set(xlabel='Month', ylabel='Page Views', title='Month-wise Box Plot (Seasonality)') 
    ax2.set_xticks(months2, labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax2.set_yticks(range(0,220000, 20000))
    # Save image and return fig (don't change this part)
    
    fig.savefig('box_plot.png')
    
    return fig
