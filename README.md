# Classifier-for-Iris-Dataset

# What I Built?
I built a Python script that loads the Iris dataset, performs basic exploratory data analysis (EDA), and creates visualizations to understand the distribution of features across different Iris species (setosa, versicolor, virginica).

# Why I Built ?
- Learning and Exploration: To understand patterns in the classic Iris dataset, a staple in machine learning.
- Visualization: To see how features like sepal length/width and petal length/width vary across species.
- EDA Practice: To practice exploratory data analysis techniques using pandas, seaborn, and matplotlib.

# How I Built ?
1. Data Loading: Used load_iris() from sklearn.datasets to get the Iris data.
2. DataFrame Creation: Converted data into a pandas DataFrame with species as a categorical variable.
3. Summary Statistics: Printed descriptive statistics using df.describe().
4. Data Preview: Displayed first few rows with df.head().
5. Visualizations:
    - Pairplot: Created with seaborn.pairplot() to show relationships between features, colored by species.
    - Violin Plot: Showed distribution of petal length for each species using seaborn.violinplot().

# Tools & Libraries Used:-
- Python: Core language.
- pandas: Data manipulation.
- seaborn & matplotlib: Visualizations.
- scikit-learn: Dataset loading (load_iris).

# Key Outcomes:-
- Insights into Iris species: Visualizations highlight differences in features across species.
- Practice EDA: Example of exploring a dataset with common Python libraries.
