# this changes the values of certain class classifications based on other class labels for that given data point
# the classes that were able to be predicted well act like a "spring" for the classes that weren't able to be predicted well. So, it's like a tug of war between the correlated labels to influence the target label
# all indices here are with respect to the pathology indices in the validation data

# import the validation csv at the path of 2024/pp/original.csv

"""
low performing classes (CNNs didn't work well on these):
lung opacity
pleural other
pneumonia
support devices

good classes:
cardiomegaly
enlarged cardiomediastinum
no finding
pleural effusion
"""
# the index is the column index in the submit file
idx_to_weight = {
    3: 1 - 0.64,
    1: 1 - 0.76,
    2: 1 - 0.78,
    4: 1 - 0.45
}

"""
Format (indices are the column numbers, 0-indexed, in the validation csv file):
CORR_IDXS = list of the indicies of the pathologies heavily correlated with the target pathology
CORR_COEFF = list of correlation factors of each pathology in CORR_IDXS and the target pathology
TARGET_IDX = index of the target pathology
"""

# UNCOMMENT BELOW THE SECTION THAT YOU WANT TO APPLY SPRING TO

# # FOR PNEUOMNIA
# # represents which indexes you want to affect the target val
# CORR_IDXS = [4, 2, 1]
# # correlation coefficient between each pathology in CORR_IDXS and the TARGET_IDX
# CORR_COEFF = [0.12, -0.49, 0.02]
# TARGET_IDX = 5

# # FOR FRACTURE
# # represents which indexes you want to affect the target val
# CORR_IDXS = [1,2,3,4]
# # correlation coefficient between each pathology in CORR_IDXS and the TARGET_IDX
# CORR_COEFF = [0.18, -0.67, 0.17, 0.46]
# TARGET_IDX = 8

# # FOR PLEURAL OTHER
# # represents which indexes you want to affect the target val
# CORR_IDXS = [1, 2, 3]
# # correlation coefficient between each pathology in CORR_IDXS and the TARGET_IDX
# CORR_COEFF = [0.02, -0.34, -0.13]
# TARGET_IDX = 7

# # FOR LUNG OPACITY
# # represents which indexes you want to affect the target val
# CORR_IDXS = [4, 3, 2]
# # correlation coefficient between each pathology in CORR_IDXS and the TARGET_IDX
# CORR_COEFF = [0.44, 0.23, -0.65]
# TARGET_IDX = 6

CORR_COEFF = [a / 10 for a in CORR_COEFF]

f = open("2024/pp/original.csv", "r")
data = f.read().split("\n")
f.close()
data = [l.split(",") for l in data]

for i in range(len(data)):
    if i == 0:
        continue
    total_change = 0
    target_val = float(data[i][TARGET_IDX])

    for j, idx in enumerate(CORR_IDXS):
        distance = float(data[i][idx]) - target_val
        if CORR_COEFF[j] < 0.0:
            distance *= -1.0
        # determine the direction
        weight = idx_to_weight[idx] + abs(CORR_COEFF[j])
        total_change += (weight * distance)
    
    total_change /= 5
    if total_change > 0.0:
        data[i][TARGET_IDX] = str(target_val + total_change)
        

for i in range(len(data)):
    data[i] = ",".join(data[i])

data = "\n".join(data)

f = open("2024/pp/original.csv", "w")
f.write(data)
f.close()