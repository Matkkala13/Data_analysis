import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df.index = df['date']
df.drop(columns = 'date', inplace=True)
df.index.name= None
string = 'hola'
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    year = []
    month = []

    for date in df.index:
        year.append(date[0:4])

    for date in df.index:
        month.append(date[5:7])
    
    df['year'] = None
    df['month'] = None
            
    df_bar = None
    return df

label_map= {
        '01': 'January', '02':'February', '03':'March', 
        '04': 'April', '05':'May', '06':'June', 
        '07': 'July', '08':'August', '09':'September',
        '10': 'October', '11':'November', '12':'December'
        }
