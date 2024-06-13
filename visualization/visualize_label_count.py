# visualize how many labels each image has in teh training set
import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

NUM_CATEGORIES = 9

file_path = 'data/student_labels/train2023.csv'

categories = [a for a in range(10)]
counts = [0 for a in range(10)]

with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)

    header = next(csv_reader)
    offset = len(header) - NUM_CATEGORIES

    for line in csv_reader:
        cnt = 0
        for i, label in enumerate(line):
            if i < offset:
                continue
            if label != "":
                cnt += 1
        counts[cnt] += 1

sns.set_theme(style="white")
plt.figure(figsize=(8,5))
plt.bar(categories, counts, color='skyblue')  # You can customize the color

# Adding titles and labels
plt.title('Category Counts')
plt.xlabel('Categories')
plt.ylabel('Count')

plt.xticks(categories)
plt.tight_layout()
plt.savefig('2024/pp/figs/label_count.png')
plt.show()