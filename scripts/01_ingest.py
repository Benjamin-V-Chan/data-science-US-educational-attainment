import pandas as pd

def load_data(input_path):
    return pd.read_csv(input_path)

def save_data(df, output_path):
    df.to_csv(output_path, index=False)

def main():
    raw_df = load_data('data/raw/1995_2015.csv')
    save_data(raw_df, 'data/processed/raw_data.csv')
    print(f'Raw data saved to data/processed/raw_data.csv with {len(raw_df)} records.')

if __name__ == '__main__':
    main()
