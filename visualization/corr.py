import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
data = pd.read_csv('data/student_labels/train2023.csv')

# Extract the relevant columns for pathologies
pathologies = data.iloc[:, -9:]

# Remove columns with all NaN values
pathologies = pathologies.dropna(axis=1, how='all')

# Compute the correlation matrix
correlation_matrix = pathologies.corr()

# Plot the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix of Pathologies')
plt.savefig("2024/pp/figs/corr.png")
plt.show()
