import pandas as pd
import matplotlib.pyplot as plt

def plot_trends(df):
    for level in df['education_level'].unique():
        subset = df[df['education_level'] == level]
        for sex in subset['sex'].unique():
            data = subset[subset['sex'] == sex]
            plt.plot(data['year'], data['percentage'], marker='o', label=sex)
        plt.title(f'{level} Percentage Over Time')
        plt.xlabel('Year')
        plt.ylabel('Percentage')
        plt.legend()
        plt.savefig(f'outputs/figures/trend_{level}.png')
        plt.clf()

def plot_age_comparison(df, year):
    subset = df[df['year'] == year]
    pivot = subset.pivot_table(
        index='age_range',
        columns='education_level',
        values='percentage'
    )
    pivot.plot(kind='bar')
    plt.title(f'Education Distribution by Age in {year}')
    plt.xlabel('Age Range')
    plt.ylabel('Percentage')
    plt.tight_layout()
    plt.savefig(f'outputs/figures/age_comparison_{year}.png')
    plt.clf()

def main():
    df = pd.read_csv('data/processed/education_data_clean.csv')
    plot_trends(df)
    for yr in sorted(df['year'].unique()):
        plot_age_comparison(df, yr)
    print('Figures saved to outputs/figures/')

if __name__ == '__main__':
    main()
