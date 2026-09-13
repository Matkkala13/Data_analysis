import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] =  df['weight'] / (df['height']/100)**2 
df.loc[df['overweight'] <= 25,'overweight' ] = 0
df.loc[df['overweight'] > 25,'overweight' ] = 1
df['overweight'] = df['overweight'].astype(int)

# 3
df.loc[df['cholesterol'] == 1,'cholesterol' ] = 0
df.loc[df['cholesterol'] > 1,'cholesterol' ] = 1
df.loc[df['gluc'] == 1,'gluc' ] = 0
df.loc[df['gluc'] > 1,'gluc' ] = 1

# 4
def draw_cat_plot():
    #5
    df_cat = df.melt(id_vars = 'cardio' ,value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight','cardio'])
    # 6
    df_cat['total'] = 1
    df_cat= df_cat.groupby(['cardio','variable','value'], as_index= False).count()

    # 7

    # 8
    fig = sns.catplot(data=df_cat,x='variable',y='total', hue= 'value',col='cardio', kind='bar').fig


    # 9
    fig.savefig('catplot.png')
    return fig


    
draw_cat_plot()
# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[
    (df['ap_lo'] <= df['ap_hi']) & 
    (df['height'] >= df['height'].quantile(0.025)) & 
    (df['height'] <= df['height'].quantile(0.975)) & 
    (df['weight'] >= df['weight'].quantile(0.025)) & 
    (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr( method='pearson')

    # 13
    mask = np.triu(corr)

    # 14
    fig, ax = plt.subplots(figsize=(12,12))

    # 15
    sns.heatmap(corr,annot=True, square=True,mask=mask, fmt= '.1f', ax=ax)

    # 16
    fig.savefig('heatmap.png')
    plt.show()
    return fig

draw_heat_map()