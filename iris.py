import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris_data = load_iris()
df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)

# Print summary statistics
print("Summary statistics:")
print(df.describe())

# Print first five rows
print("\nFirst five rows:")
print(df.head())

# Pairplot visualization
sns.pairplot(df, hue='species')
plt.suptitle("Iris Dataset Pairplot", y=1.02)
plt.show()

# Violin plot for petal length by species
plt.figure(figsize=(8, 5))
sns.violinplot(x='species', y='petal length (cm)', data=df)
plt.title("Petal Length Distribution by Species")
plt.show()