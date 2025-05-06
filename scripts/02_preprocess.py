# scripts/02_preprocess.py

# Read raw_data.csv, clean column names, melt to long form, compute percentages, save clean CSV.

# Import pandas
# Define preprocess(df):
#   rename columns to lowercase
#   melt wide→long for education columns
#   compute percentage = count / Total * 100
#   return long DataFrame
# In main():
#   df = pd.read_csv('data/processed/raw_data.csv')
#   clean = preprocess(df)
#   clean.to_csv('data/processed/education_data_clean.csv', index=False)
#   print confirmation
# if __name__ == '__main__': main()
