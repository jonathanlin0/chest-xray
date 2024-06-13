# visalize the label frequency for the training set
import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

NUM_CATEGORIES = 9

file_path = 'data/student_labels/train2023.csv'

data = None
headers = None

with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)

    header = next(csv_reader)
    
    # index of first of last 9 columns
    offset = len(header) - NUM_CATEGORIES
    headers = header[-NUM_CATEGORIES:]

    temp = {"-1.0":0, "0.0": 0, "1.0": 0}

    data = []
    for _ in range(NUM_CATEGORIES):
        data.append(temp.copy())

    for line in csv_reader:
        for i, label in enumerate(line):
            if i < offset:
                continue
            true_idx = i - offset
            
            if label != "":
                data[true_idx][label] += 1
        
temp = {}

for i, header in enumerate(headers):
    temp[header] = data[i]

data = temp

categories = list(data.keys())
values_minus_one = [data[category]['-1.0'] for category in categories]
values_zero = [data[category]['0.0'] for category in categories]
values_one = [data[category]['1.0'] for category in categories]

# Setting up the bar width
barWidth = 0.5

# Set position of bar on X axis
r1 = np.arange(len(categories))

# Make the plot
sns.set_theme(style="white")
plt.figure(figsize=(20,8))
plt.bar(r1, values_minus_one, color='red', width=barWidth, edgecolor='grey', label='-1')
plt.bar(r1, values_zero, bottom=values_minus_one, color='blue', width=barWidth, edgecolor='grey', label='0')
plt.bar(r1, values_one, bottom=[i+j for i,j in zip(values_minus_one, values_zero)], color='green', width=barWidth, edgecolor='grey', label='1')

# Add xticks on the middle of the group bars
plt.xlabel('Category', fontweight='bold')
plt.xticks([r for r in range(len(categories))], categories)

plt.title("Label Frequences")

# Create legend & Show graphic
plt.legend()
plt.tight_layout()
plt.savefig('2024/pp/figs/label_frequency.png')

plt.show()

for i in data:
    print(f"{i}: {data[i]}")
