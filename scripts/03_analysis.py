import pandas as pd

def compute_summary(df):
    by_year = df.groupby('year')['percentage'].mean().reset_index()
    pct_change = df.pivot_table(
        index='education_level',
        columns='year',
        values='percentage'
    ).diff(axis=1)
    by_age_sex = df.groupby(['year', 'age_range', 'sex'])['percentage'].mean().reset_index()
    return {
        'by_year': by_year,
        'pct_change': pct_change,
        'by_age_sex': by_age_sex
    }

def main():
    df = pd.read_csv('data/processed/education_data_clean.csv')
    summary = compute_summary(df)
    summary['by_year'].to_csv('outputs/stats/education_by_year.csv', index=False)
    summary['pct_change'].to_csv('outputs/stats/education_pct_change.csv')
    summary['by_age_sex'].to_csv('outputs/stats/education_by_age_sex.csv', index=False)
    print('Analysis results saved to outputs/stats/')

if __name__ == '__main__':
    main()
