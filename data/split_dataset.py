## to split original dataset into 0.7, 0.15, 0.15 ration

import splitfolders 

dataset_path = "D:\github\potato-diseases\data\original_dataset"
output_path = "D:\github\potato-diseases\data\split_dataset"

splitfolders.ratio(dataset_path, 
                   output=output_path, 
                   seed=42, 
                   ratio=(0.7, 0.15,0.15))

print("succes to split the dataset")