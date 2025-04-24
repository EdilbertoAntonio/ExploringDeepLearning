# Deep learning

This repository will have two projects of how can deep learning can predict closing values of AAME and predict the chinese character.

## Dataset of AAME

The dataset includes the following columns:
- Date: Trading date
- Open: Opening stock price
- High: Highest price of the day
- Low: Lowest price of the day
- Close: Closing stock price
- Adjusted Close: Closing price adjusted for splits/dividends
- Volume: Number of shares traded

This repository includes a sample extracted from the [original dataset](https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset).
You can find it in the `data` folder.


## About Chinese Mnist project

This dataset contains 15 Chinese characters, each representing a number and classified into one of 15 different classes. The data was collected from 100 volunteers, each of whom wrote every character 10 times, resulting in 15,000 unique images with 1,000 samples per class. The dataset was collected by Dr. K. Nazarpour and Dr. M. Chen from Newcastle University.

The dataset includes the following columns:
- suite_id: the ID of the volunteer
- sample_id: the sample number written by the volunteer
- code: the class that the character belongs
- value: the number represented by the character
- character: the chinese character

In this repository only contains a sample from the original dataset, which is available on [kaggle](https://www.kaggle.com/datasets/gpreda/chinese-mnist)

Here are the description of the files:
- chinese_mnist.ipynb: the CNN project notebbok
- image_filtering: the script used to apply filters to the images
- sample choose: the script of how the sample was extracted from the original dataset
- MSYH: the chinese font used to display the characters
- data/sample_chinese_mnist.csv: labels of the sampled images
- data/X_sample_filtered.npy: Numpy array of the filtered sample images (useful if you don’t want to download the images)
- data/X_sample_not_filtered.npy: Numy array of the sample images (useful if you don’t want to download the images)
- data/sample images: the sample images






 
