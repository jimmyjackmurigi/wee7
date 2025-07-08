import pandas as pd
import matplotlib.pyplot as plt
from aif360.datasets import CompasDataset
from aif360.metrics import BinaryLabelDatasetMetric, ClassificationMetric
from aif360.algorithms.preprocessing import Reweighing
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings("ignore")

# Load COMPAS dataset from aif360
dataset = CompasDataset()

# Show basic stats
print(f"Features: {dataset.features.shape}")
print(f"Label distribution: {dataset.labels}")

# Check bias - using BinaryLabelDatasetMetric
metric = BinaryLabelDatasetMetric(dataset,
                                   unprivileged_groups=[{'race': 1}],
                                   privileged_groups=[{'race': 0}])
print("Disparate Impact:", metric.disparate_impact())
print("Mean Difference:", metric.mean_difference())

# Visualize
dataset.features[:, dataset.feature_names.index('age')] = dataset.features[:, dataset.feature_names.index('age')].astype(float)
ages = dataset.features[:, dataset.feature_names.index('age')]

plt.hist(ages, bins=20, color='skyblue')
plt.title("Age Distribution in COMPAS Dataset")
plt.xlabel("Age")
plt.ylabel("Count")
plt.savefig("age_distribution.png")
plt.show()
