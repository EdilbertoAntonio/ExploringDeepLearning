# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 12:19:18 2025

@author: 109149
"""

import numpy as np
import pandas as pd
import os

labels = pd.read_csv('D:\\Diplomado CDD BUAP\\modulo 6\\chinese mnist\\chinese_mnist.csv')
image_name = [f"input_{labels['suite_id'][i]}_{labels['sample_id'][i]}_{labels['code'][i]}.jpg" for i in range(len(labels))]

labels['image_name'] = np.array(image_name)
labels = labels[['code', 'character', 'image_name']]
labels = labels.copy() 
labels['code'] = labels['code']-1

random = np.array([], dtype=int)

for i in range(0,15000,1000):
    aux = np.random.randint(i, i+1000, 100)
    aux = np.sort(aux)
    random = np.concatenate((random,aux))
    
labels['code'][random].value_counts()
    
sample = labels['image_name'][random]

#%%

import shutil

carpeta_origen = 'D:\\Diplomado CDD BUAP\\modulo 6\\chinese mnist\\data\\data'
carpeta_destino = 'D:\\Diplomado CDD BUAP\\modulo 6\\chinese mnist\\sample images'

nombres = sample.tolist()

for nombre in nombres:
    ruta_origen = os.path.join(carpeta_origen, nombre)
    ruta_destino = os.path.join(carpeta_destino, nombre)
    
    if os.path.exists(ruta_origen):
        shutil.copy(ruta_origen, ruta_destino)
    else:
        print(f"Imagen no encontrada: {nombre}")


#%%

labels = pd.read_csv('D:\\Diplomado CDD BUAP\\modulo 6\\chinese mnist\\chinese_mnist.csv')
sample_labels_chinese_mnist = labels.loc[random]
sample_labels_chinese_mnist.reset_index(drop=True, inplace=True)

sample_labels_chinese_mnist['code'].value_counts()
#%%
os.chdir('D:\\Diplomado CDD BUAP\\modulo 6\\chinese mnist')
sample_labels_chinese_mnist.to_csv('sample_chinese_mnist.csv', index=False)





