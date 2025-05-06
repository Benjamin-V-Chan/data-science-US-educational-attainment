import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def prepare_features(df):
    pivot = df.pivot_table(
        index=['age_range', 'sex'],
        columns='year',
        values='percentage'
    ).fillna(0)
    scaler = StandardScaler()
    features = scaler.fit_transform(pivot)
    return features, pivot.index

def apply_pca(features):
    pca = PCA(n_components=2, random_state=42)
    return pca.fit_transform(features), pca

def cluster_data(features, n_clusters=3):
    km = KMeans(n_clusters=n_clusters, random_state=42)
    labels = km.fit_predict(features)
    return labels, km

def plot_clusters(coords, labels, index):
    plt.scatter(coords[:, 0], coords[:, 1], c=labels)
    for i, (age, sex) in enumerate(index):
        plt.annotate(f'{age}-{sex}', (coords[i, 0], coords[i, 1]))
    plt.title('PCA + KMeans Clusters')
    plt.savefig('outputs/figures/pca_clusters.png')
    plt.clf()

def main():
    df = pd.read_csv('data/processed/education_data_clean.csv')
    features, index = prepare_features(df)
    coords, _ = apply_pca(features)
    labels, _ = cluster_data(features)
    results = pd.DataFrame({
        'age_range': [a for a, s in index],
        'sex': [s for a, s in index],
        'cluster': labels
    })
    results.to_csv('outputs/stats/cluster_results.csv', index=False)
    plot_clusters(coords, labels, index)
    print('Modeling results saved to outputs/stats/ and outputs/figures/')

if __name__ == '__main__':
    main()
