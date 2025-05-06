# scripts/05_modeling.py

# Load clean data, pivot to get one row per (age_range, sex) with percentages across years as features,
# standardize, apply PCA→2D, cluster via KMeans, save cluster labels and a PCA+cluster scatter plot.

# Import pandas, numpy, sklearn PCA, KMeans, StandardScaler, matplotlib.pyplot
# Define prepare_features(df):
#   pivot index=['age_range','sex'], columns=year, values=percentage
#   fill NA, scale, return features array + index
# Define apply_pca(features): return PCA coords + model
# Define cluster_data(features): return labels + model
# Define plot_clusters(coords, labels, index):
#   scatter + annotate, save to outputs/figures/pca_clusters.png
# In main():
#   df = pd.read_csv(...)
#   features,index = prepare_features(df)
#   coords,_ = apply_pca(features)
#   labels,_ = cluster_data(features)
#   results.to_csv('outputs/stats/cluster_results.csv')
#   plot_clusters(coords, labels, index)
#   print confirmation
# if __name__ == '__main__': main()
