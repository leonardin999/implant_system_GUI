import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import keras
import os.path
from pathlib import Path
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Input
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix
savedModel=keras.models.load_model('D://TRUC/AFinal_kieu_than.h5')
from keras.preprocessing import image

test_image = image.load_img('D://HIEN/Implant/x-ray-illustration-implant-and-crown-cropped.jpg', target_size = (200, 90,3))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = savedModel.predict(test_image)
print(result)
a=np.round(result)
print(a)
'''
if (result== [1., 0., 0.]).all():
    prediction = 'Tapered'
elif (result == [0., 1., 0.]).all():
    prediction = 'TaperedApex'
elif (result == [0., 0., 1.]).all():
    prediction = 'NonTapered'
else:
    prediction = 'Not found'
print(prediction)
'''
if (a== [1, 0, 0]).all():
    prediction = 'Tapered'
elif (a == [0, 1, 0]).all():
    prediction = 'TaperedApex'
elif (a == [0, 0, 1]).all():
    prediction = 'NonTapered'
else:
    prediction = 'Not found'
print(prediction)
