<h2 align="center"> Potato Diseases Classification </h2>

Notes (not so important): I made this in wsl ubuntu. So, if you want to run the codes (drugs-classification.ipynb, train.py) again make sure don't forget to change the paths.

<!-- ABOUT THE PROJECT -->

## About The Project

This project is about classification potato diseases based on image using pre-trained model. The dataset that I used is from kaggle:

[https://www.kaggle.com/datasets/mukaffimoin/potato-diseases-datasets](https://www.kaggle.com/datasets/mukaffimoin/potato-diseases-datasets)

The dataset has 7 classes: black scurf, blackleg, common scab, dry rot, healthy potatoes, miscellaneous, pink rot. You can find the dataset in repository here too at `data/original_dataset` or `data/split_dataset` that I already splitted to train, val and test (70%, 15%, 15%).

The purpose of this project are to classification image in the potatoes. It will be good help for farmer and agricultural industry

## About Folders and Files

### Folders

- `data` = contains dataset before and after splitted
- `Notebook` = EDA, model training and parameter tuning too.
- `model` = saved model in .h5 format and tflite format

### Files

- `tensorflow-model.ipynb` = script to convert h5 model to tflite model. Also testing the model too.

## Deployment (Plan for future)

Unfortunately, I still can't solved the problem that I have in `tensoflow-model.ipynb`. The error said 'ValueError: Cannot set tensor: Got value of type UINT8 but expected type FLOAT32 for input 0, name: serving_default_input_8:0'. I tried checking which one that cause the error but still can't find. Anyone that read this and have suggestions are really helpful for me.

Also for the plan: I will try using docker first and the next one is cloud (most likely AWS)
