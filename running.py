import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import os
import time

import tkinter
from tkinter.filedialog import askopenfilename

import numpy as np

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img

CLASS_NAMES= ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

model = keras.models.load_model('saved_model/my_model')

root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

failure = False

while failure == False:
	filepath = askopenfilename()

	if len(filepath) > 0:
		img_width, img_height = 227, 227
		img = load_img(filepath, target_size = (img_width, img_height))

		img.show()
		
		input_arr = img_to_array(img)

		img = np.expand_dims(img, axis = 0)

		pred = model.predict(img)


		print(CLASS_NAMES[np.argmax(pred)])

	else: 
		print("upload failure")
		failure = True

print("done")