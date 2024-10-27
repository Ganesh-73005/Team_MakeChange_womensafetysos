### video link
## (https://drive.google.com/file/d/11TicyNKWkvhu1ccr1D0YBzNtVjomxPtw/view?usp=drive_link)
### SS3 - saferoute prediction with gmm, kmeans clustering (red marks indicate tasmacs)

![Feature 1 Image](https://i.ibb.co/xLLs4b4/Screenshot-2024-10-27-161707.png)
Here's a sample README.md for your K-Means Clustering project. You can modify it according to your specific project details and requirements.

```markdown
# K-Means Clustering Project

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Example](#example)
- [Results](#results)
- [Dependencies](#dependencies)
- [License](#license)

## Introduction

K-Means Clustering is an unsupervised machine learning algorithm used to partition a dataset into K distinct clusters based on feature similarity. This project implements the K-Means algorithm to analyze and visualize clustering patterns in data.

## Installation

To run this project, ensure you have Python installed on your machine. You can install the necessary dependencies using pip:

```bash
pip install numpy pandas matplotlib scikit-learn
```

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/k-means-clustering.git
    cd k-means-clustering
    ```

2. Place your dataset (CSV format) in the project directory.

3. Modify the `main.py` file to specify the path to your dataset and the number of clusters.

4. Run the program:
    ```bash
    python main.py
    ```

## How It Works

1. **Data Loading**: The dataset is loaded into a Pandas DataFrame.
2. **Preprocessing**: The data is normalized to ensure all features contribute equally to the distance calculations.
3. **K-Means Algorithm**:
   - Randomly initialize K centroids.
   - Assign each data point to the nearest centroid.
   - Recalculate the centroids based on the assigned points.
   - Repeat the assignment and update steps until convergence (centroids no longer change significantly).
4. **Visualization**: The final clusters and centroids are visualized using Matplotlib.

## Example

Below is an example of how to use the K-Means clustering algorithm on a sample dataset:

```python
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('your_dataset.csv')

# Preprocess data (normalization can be added here)

# Initialize KMeans
kmeans = KMeans(n_clusters=3, random_state=0)

# Fit the model
kmeans.fit(data)

# Predict clusters
data['Cluster'] = kmeans.predict(data)

# Plotting
plt.scatter(data['Feature1'], data['Feature2'], c=data['Cluster'])
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
```

## Results

After running the algorithm, the data points are clustered into distinct groups. The centroids of the clusters are displayed in the visualization.

## Dependencies

- Python 3.x
- numpy
- pandas
- matplotlib
- scikit-learn




Feel free to customize this README to reflect your specific project details, including any additional features, data sources, or examples you may have!
### SS2 front end - figma design

![Feature 2 Image](https://i.ibb.co/VCfB0Br/Screenshot-2024-10-27-161140.png)

### SS1 - figma design

![Feature 3 Image](https://i.ibb.co/kV7MtDz/Screenshot-2024-10-27-161152.png)

### Features:
## Sos alerts 

![sos button to fetch current location](https://i.ibb.co/dKdbbt4/Screenshot-2024-10-27-165858.png)
## Safestroutes
## fake alerts detection 

# used db techniques to find fake alerts (repeated sos from same location , in recent days)
![](https://i.ibb.co/7nk0j4k/Screenshot-2024-10-27-165929.png)

