import pandas as pd 


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult_data.csv')
    print(df.loc[df['workclass'] == 'Prof-specialty'])

calculate_demographic_data()
