# visualize the distribution of frontal and lateral training images
import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

NUM_CATEGORIES = 9

file_path = 'data/student_labels/train2023.csv'

# key is the pid
# value is a set containing "Frontal" and/or "Lateral"
data = {}


with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)

    header = next(csv_reader)

    for line in csv_reader:
        person_id = line[2]
        person_id = person_id[person_id.find("/") + 1:]
        person_id = person_id[:person_id.find("/")]
        
        if person_id not in data:
            data[person_id] = set()
        data[person_id].add(line[5])

categories = ["Frontal only", "Lateral only", "Both"]
counts = [0, 0, 0]
for s in data.values():
    if len(s) == 2:
        counts[2] += 1
    elif "Frontal" in s:
        counts[0] += 1
    else:
        counts[1] += 1

sns.set_theme(style="white")
plt.figure(figsize=(8,5))
plt.bar(categories, counts, color='skyblue')  # You can customize the color

# Adding titles and labels
plt.title('Perspective Distribution')
plt.xlabel('Data Type')
plt.ylabel('Count')

plt.xticks(categories)
plt.tight_layout()
plt.savefig('2024/pp/figs/frontal_lateral_count.png')
plt.show()