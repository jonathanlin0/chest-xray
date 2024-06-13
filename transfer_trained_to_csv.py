# transfers all the new output labels into the CSV file called "original.csv".
import json
import numpy as np

categories = ["frontal"]
for CATEGORY_IDX in range(1, 2):
    for category in categories:

        existing_csv_path = "2024/pp/original.csv"
        f = open(f"2024/pp/labels/output_labels_{category}{CATEGORY_IDX}.json", "r")
        new_data = json.load(f)
        f.close()

        # get relative index of the pathology trained on (cuz order of pathology columns r dif between training and test data)
        f = open("data/student_labels/train2023.csv", "r")
        data = f.read().split("\n")[0].split(",")[-9:]
        f.close()

        pathology = data[CATEGORY_IDX]

        f = open(existing_csv_path, "r")
        data = f.read().split("\n")[0].split(",")[-9:]
        f.close()

        adjusted_idx = data.index(pathology)

        # map ID to path and path to ID
        f = open("data/student_labels/test_ids.csv", "r")
        data = f.read().split("\n")[1:]
        f.close()

        ID_to_path = {}
        path_to_ID = {}
        for line in data:
            if line == "":
                continue
            line = line.split(",")
            ID_to_path[line[0]] = line[1]
            path_to_ID[line[1]] = line[0]

        f = open(existing_csv_path, "r")
        existing_csv = f.read().split("\n")
        f.close()

        out = []

        for i, line in enumerate(existing_csv):
            line = line.split(",")
            if i != 0 and len(line) > 1:
                matching_path = ID_to_path[line[0]]
                if matching_path in new_data:
                    # change specific index
                    val = new_data[matching_path]
                    # do this manually cuz for some reason np.clip doesn't work
                    val = min(1.0, val)
                    val = max(-1.0, val)
                    # if val > 1.0:
                    #     val = 1.0
                    # if val < -1.0:
                    #     val = -1.0
                    line[1 + adjusted_idx] = str(val)
            out.append(",".join(line))
            
        f = open(existing_csv_path, "w")
        f.write("\n".join(out))
        f.close()