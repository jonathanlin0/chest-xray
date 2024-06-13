# show the distribution of dimensions from the training set
import matplotlib.pyplot as plt

# Simulated data from a text file
f = open("2024/pp/preprocessing/dimensions.txt", "r")
data = f.read()
f.close()

# Parsing the data
dimensions = []
for line in data.strip().split("\n"):
    parts = line.split()
    width, height, count = int(parts[0]), int(parts[1]), int(parts[2])
    dimensions.extend([(width, height)] * count)

# Unpacking widths and heights
widths, heights = zip(*dimensions)

# Plotting histograms
fig, ax = plt.subplots(1, 2, figsize=(8, 3))  # Adjusted to 1 row, 2 columns

# Histogram for widths
ax[0].hist(widths, bins=10, color='blue', alpha=0.7)
ax[0].set_title('Distribution of Picture Widths')
ax[0].set_xlabel('Width')
ax[0].set_ylabel('Frequency')

# Histogram for heights
ax[1].hist(heights, bins=10, color='green', alpha=0.7)
ax[1].set_title('Distribution of Picture Heights')
ax[1].set_xlabel('Height')
ax[1].set_ylabel('Frequency')

plt.tight_layout()
plt.savefig('2024/pp/figs/dimensions.png')  # Saving the figure to a file
