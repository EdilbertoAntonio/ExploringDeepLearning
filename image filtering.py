# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 19:29:10 2025

@author: 109149
"""

import numpy as np
import pandas as pd
import cv2
import os

#%% 
ruta_labels = 'D:\\Diplomado CDD BUAP\\modulo 6\\chinese mnist\\chinese_mnist.csv' #ruta donde está csv
ruta_imagenes = 'D:\\Diplomado CDD BUAP\\modulo 6\\chinese mnist\\data\\data\\' #ruta donde están las imagenes 
ruta_arrays = 'D:\\Diplomado CDD BUAP\\modulo 6' #ruta donde se guardarán los arreglos que tendrán la información de las imagenes

#%%
labels = pd.read_csv(ruta_labels)
image_name = [f"input_{labels['suite_id'][i]}_{labels['sample_id'][i]}_{labels['code'][i]}.jpg" for i in range(len(labels))]

labels['image_name'] = np.array(image_name)
labels = labels[['code', 'character', 'image_name']]
labels = labels.copy() 
labels['code'] = labels['code']-1

#%% guardado sin filtro
X_not_filtered = []
for i in range(len(labels)):
    img_path = os.path.join(ruta_imagenes, labels['image_name'][i])
    image = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE) 
    
    
    X_not_filtered.append(image)
    
X_not_filtered = np.array(X_not_filtered)

os.chdir(ruta_arrays)
np.save('X_not_filtered.npy', X_not_filtered)

#%% guardado con filtro
X_filtered = []
for i in range(len(labels)):
    img_path = os.path.join(ruta_imagenes, labels['image_name'][i])
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) 
    inverted = cv2.bitwise_not(image)
    img_blur = cv2.GaussianBlur(inverted, (1,1), 5)
    binary = cv2.adaptiveThreshold(img_blur, 255, 
                               cv2.ADAPTIVE_THRESH_MEAN_C, 
                               cv2.THRESH_BINARY_INV, blockSize=19, C=2)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
    cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    final = (255 - cleaned)/255
    
    X_filtered.append(final)
    
X_filtered = np.array(X_filtered)

os.chdir(ruta_arrays)
np.save('X_filtereds.npy', X_filtered)