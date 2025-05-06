# data-science-US-educational-attainment

## Project Overview

This project analyzes U.S. educational attainment data from 1995, 2005, and 2015. It ingests the raw CSV, cleans and reshapes the data, computes summary statistics, visualizes trends, and applies PCA with clustering to reveal patterns across age ranges and sex.

## Folder Structure

```
project-root/
├── data/
│   ├── raw/                # Raw input files (1995_2015.csv, 2005.xls, 2015.xlsx)
│   └── processed/          # Cleaned and transformed CSVs
├── outputs/
│   ├── stats/              # Summary tables (CSV)
│   └── figures/            # Charts and plots (PNG)
├── scripts/                # Analysis pipeline scripts
│   ├── 01_ingest.py        # Load and save raw data
│   ├── 02_preprocess.py    # Clean, reshape, compute percentages
│   ├── 03_analysis.py      # Compute summary statistics
│   ├── 04_visualization.py # Generate trend and bar charts
│   └── 05_modeling.py      # PCA and clustering analysis
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Usage

1. **Setup the Project:**

   * Clone the repository.
   * Ensure you have Python installed.
   * Install required dependencies using the requirements.txt file.

   ```bash
   pip install -r requirements.txt
   ```

2. **Ingest Raw Data:**

   ```bash
   python scripts/01_ingest.py
   ```

3. **Preprocess Data:**

   ```bash
   python scripts/02_preprocess.py
   ```

4. **Compute Analytics:**

   ```bash
   python scripts/03_analysis.py
   ```

5. **Generate Visualizations:**

   ```bash
   python scripts/04_visualization.py
   ```

6. **Run Modeling Pipeline:**

   ```bash
   python scripts/05_modeling.py
   ```

