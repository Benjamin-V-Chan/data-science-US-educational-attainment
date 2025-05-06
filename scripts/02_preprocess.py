import pandas as pd

def preprocess(df):
    df = df.rename(columns={
        'Year': 'year',
        'Age_Range': 'age_range',
        'Sex': 'sex'
    })
    value_vars = [
        'No_HS_Diploma', 'HS_Diploma',
        'Some_College_No_Degree', 'Associate',
        'Bachelor', 'Advanced'
    ]
    df_long = df.melt(
        id_vars=['year', 'age_range', 'sex', 'Total'],
        value_vars=value_vars,
        var_name='education_level',
        value_name='count'
    )
    df_long['percentage'] = df_long['count'] / df_long['Total'] * 100
    return df_long

def main():
    df = pd.read_csv('data/processed/raw_data.csv')
    clean = preprocess(df)
    clean.to_csv('data/processed/education_data_clean.csv', index=False)
    print('Processed data saved to data/processed/education_data_clean.csv')

if __name__ == '__main__':
    main()
