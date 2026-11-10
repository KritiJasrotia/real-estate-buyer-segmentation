# Real Estate Buyer Segmentation Using Machine Learning

## About the Project

This project focuses on analyzing real estate buyer behaviour and identifying different buyer segments using Machine Learning techniques.

It uses Python for data cleaning, data analysis, visualization, and clustering. K-Means and Hierarchical Clustering algorithms are implemented to group buyers based on their characteristics and property-related behaviour.

An interactive dashboard is also developed using Streamlit to visualize buyer segmentation, investment behaviour, geographical distribution, and other important insights.

## Project Objectives

- To clean and preprocess real estate client and property datasets.
- To perform Exploratory Data Analysis (EDA).
- To analyze buyer demographics and purchasing behaviour.
- To identify buyer segments using Machine Learning algorithms.
- To compare K-Means and Hierarchical Clustering.
- To analyze home-buying and investment behaviour.
- To develop an interactive Streamlit dashboard.
- To generate useful insights for real estate market analysis.

## Dataset Description

This project uses two datasets:

### 1. Clients Dataset

- File Name: `clients.csv`
- Total Records: 2,000
- Total Columns: 12

Important attributes include:
- Client ID
- Client Type
- Gender
- Country
- Region
- Date of Birth
- Acquisition Purpose
- Loan Applied
- Referral Channel
- Satisfaction Score

### 2. Properties Dataset

- File Name: `properties.csv`
- Total Records: 10,000
- Total Columns: 9

Important attributes include:
- Listing ID
- Transaction Date
- Unit Category
- Floor Area
- Sale Price
- Listing Status
- Client Reference

Both datasets are used together to analyze buyer characteristics and property-related information.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming |
| Jupyter Notebook | Development Environment |
| Pandas | Data Analysis |
| NumPy | Numerical Operations |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Scikit-learn | Machine Learning |
| SciPy | Hierarchical Clustering |
| Streamlit | Interactive Dashboard |
| Plotly | Interactive Charts |

## Project Workflow

### 1. Data Collection
- Loaded client and property datasets using Pandas.
- Inspected dataset structure, columns, and data types.

### 2. Data Cleaning and Preprocessing
- Checked missing values and duplicate records.
- Removed duplicate client and property IDs.
- Standardized categorical values.
- Converted date columns into datetime format.
- Converted sale prices into numerical values.
- Calculated buyer age.
- Handled missing values.

### 3. Exploratory Data Analysis (EDA)

Performed analysis on:
- Gender distribution.
- Country-wise buyer distribution.
- Region-wise buyer distribution.
- Individual and company clients.
- Home and investment acquisition purposes.
- Loan application behaviour.
- Property sale prices.
- Buyer satisfaction scores.

### 4. Feature Engineering and Encoding
- Selected relevant numerical and categorical features.
- Applied One-Hot Encoding to categorical features.
- Applied StandardScaler to numerical features.
- Prepared the final dataset for clustering.

### 5. Machine Learning Algorithms

**K-Means Clustering**

K-Means was used to group buyers based on similarities in their characteristics. The Elbow Method and Silhouette Score were used to evaluate the number of clusters.

**Hierarchical Clustering**

Agglomerative Hierarchical Clustering with Ward linkage was implemented to identify buyer groups based on similarities.

### 6. Model Evaluation

The Silhouette Score was used to compare the clustering algorithms.

### 7. Dashboard Development

An interactive dashboard was created using Streamlit and Plotly to present the results of the analysis.

## Model Results

Two clusters were selected for both algorithms.

| Algorithm | Number of Clusters | Silhouette Score |
|---|---:|---:|
| K-Means | 2 | 0.1422 |
| Hierarchical Clustering | 2 | 0.1330 |

### K-Means Cluster Distribution

| Cluster | Number of Buyers |
|---|---:|
| Cluster 0 | 807 |
| Cluster 1 | 1,193 |
| Total | 2,000 |

K-Means achieved a slightly higher Silhouette Score than Hierarchical Clustering.

However, both scores indicate relatively weak separation between the clusters. The identified groups should therefore be considered exploratory buyer segments.

### Cluster Analysis

| Parameter | Cluster 0 | Cluster 1 |
|---|---:|---:|
| Number of Buyers | 807 | 1,193 |
| Average Age | 55.63 | 57.02 |
| Average Satisfaction | 3.05 | 3.02 |
| Average Linked Properties | 3.47 | 3.77 |
| Average Sale Price | 414,534.61 | 301,467.30 |

These results provide a comparison of buyer characteristics and property-related information across the two clusters.

## Streamlit Dashboard Features

The project includes an interactive dashboard with the following sections:

### 1. Buyer Segmentation Overview
- Total number of buyers.
- Investment buyer distribution.
- Average buyer age.
- Number of identified clusters.
- Buyer distribution visualizations.

### 2. Investor Behaviour Dashboard
- Home versus investment acquisition purpose.
- Property-related buyer information.
- Sale price analysis.
- Investment behaviour visualizations.

### 3. Geographic Buyer Analysis
- Country-wise buyer distribution.
- Region-wise buyer distribution.
- Geographical analysis of buyers.

### 4. Segment Insights Panel
- Cluster-wise buyer profiles.
- Comparison of buyer segments.
- Buyer information and insights.

### Interactive Filters

The dashboard provides filters for:
- Country
- Region
- Acquisition Purpose
- Client Type
- K-Means Cluster

It also includes interactive charts, buyer records, and CSV download functionality.

## Project Structure

```text
real-estate-buyer-segmentation/
│
├── Real_Estate_Buyer_Segmentation.ipynb
├── clients.csv
├── properties.csv
├── buyer_segmentation_results.csv
├── cluster_profile.csv
├── cluster_category_analysis.csv
├── app.py
├── README.md
└── .gitignore
```

## How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/real-estate-buyer-segmentation.git
```

### Step 2: Open the Project Folder

```bash
cd real-estate-buyer-segmentation
```

### Step 3: Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy streamlit plotly jupyter
```

### Step 4: Run Jupyter Notebook

```bash
jupyter notebook
```

Open the project notebook and run the cells in sequence.

### Step 5: Run the Streamlit Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your web browser.

**Note:** The required CSV datasets must be available in the project folder before running the notebook or dashboard.

## Key Insights

The project helps to:
- Understand real estate buyer demographics.
- Analyze geographical buyer distribution.
- Compare home and investment acquisition purposes.
- Explore loan application behaviour.
- Examine property-related buyer activity.
- Identify exploratory buyer groups using clustering.
- Present analytical results through an interactive dashboard.

## Limitations

- The datasets do not contain buyer income information.
- Some property records have missing client references.
- Both clustering algorithms produced relatively low Silhouette Scores.
- Available features may not capture every factor influencing buyer decisions.
- Results depend on the quality and characteristics of the supplied datasets.

## Future Scope

- Include additional buyer attributes such as income and investment budget.
- Explore additional clustering algorithms.
- Improve cluster separation through feature selection and model evaluation.
- Use larger and more diverse real estate datasets.
- Add advanced visualizations and dashboard features.
- Explore predictive models for real estate market analysis.

## Author

**Kriti Jasrotia**

B.Tech – Computer Science and Engineering

Maharishi Dayanand University, Rohtak

## Acknowledgement

This project was completed as part of the Data Analysis Internship at Unified Mentor.

It provided practical experience in Python programming, data cleaning, exploratory data analysis, Machine Learning, clustering techniques, and interactive dashboard development.
