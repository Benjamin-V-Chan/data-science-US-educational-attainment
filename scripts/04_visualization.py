# scripts/04_visualization.py

# Load clean data, plot trends for each education level over time (separated by sex), 
# then bar-chart comparisons by age for each year; save PNGs.

# Import pandas, matplotlib.pyplot
# Define plot_trends(df):
#   for each education_level:
#     for each sex: plt.plot(year, percentage)
#     decorate and save as outputs/figures/trend_{level}.png
# Define plot_age_comparison(df, year):
#   pivot age_range × education_level
#   plot bar, save outputs/figures/age_comparison_{year}.png
# In main():
#   df = pd.read_csv(...)
#   plot_trends(df)
#   for yr in unique years: plot_age_comparison(df, yr)
#   print confirmation
# if __name__ == '__main__': main()
