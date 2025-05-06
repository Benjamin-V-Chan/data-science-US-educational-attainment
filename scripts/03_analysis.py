# scripts/03_analysis.py

# Load the clean data, compute summary stats by year, by age/sex, and year-over-year changes, save CSVs.

# Import pandas
# Define compute_summary(df):
#   by_year = average percentage per year
#   pct_change = pivot education_level × year and diff across columns
#   by_age_sex = group by year, age_range, sex
#   return dict of DataFrames
# In main():
#   df = pd.read_csv('data/processed/education_data_clean.csv')
#   summary = compute_summary(df)
#   summary[...]→outputs/stats/*.csv
#   print confirmation
# if __name__ == '__main__': main()
