import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



#


df = pd.read_csv('medical_examination.csv')



df['overweight'] =  df['weight'] / (df['height']/100)**2 
df.loc[df['overweight'] <= 25,'overweight' ] = 0
df.loc[df['overweight'] > 25,'overweight' ] = 1
df['overweight'] = df['overweight'].astype(int)

# 3
df.loc[df['cholesterol'] == 1,'cholesterol' ] = 0
df.loc[df['cholesterol'] > 1,'cholesterol' ] = 1
df.loc[df['gluc'] == 1,'gluc' ] = 0
df.loc[df['gluc'] > 1,'gluc' ] = 1

df_cat = df.melt(id_vars = 'cardio' ,value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight','cardio'])
df_cat['Total'] = 1
df_cat= df_cat.groupby(['cardio','variable','value'],as_index=False).count()

df = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]
print(df)
