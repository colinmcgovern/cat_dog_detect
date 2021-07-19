import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import os
import time
import shutil
from PIL import Image

import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img

def clear(folder):
	for filename in os.listdir(folder):
	    file_path = os.path.join(folder, filename)
	    try:
	        if os.path.isfile(file_path) or os.path.islink(file_path):
	            os.unlink(file_path)
	        elif os.path.isdir(file_path):
	            shutil.rmtree(file_path)
	    except Exception as e:
	        print('Failed to delete %s. Reason: %s' % (file_path, e))

def get_neg():
	train_neg_images = []
	train_neg_labels = []

	for filename in os.listdir("not_cute"):
	  #print(filename)
	  train_neg_images.append(img_to_array(load_img("not_cute/"+filename,
	                      target_size = (227, 227))))
	  train_neg_labels.append(0)

	return train_neg_images,train_neg_labels

def get_pos():
	train_pos_images = []
	train_pos_labels = []

	for filename in os.listdir("cute"):
	  #print(filename)
	  train_pos_images.append(img_to_array(load_img("cute/"+filename,
	                      target_size = (227, 227))))
	  train_pos_labels.append(1)

	return train_pos_images,train_pos_labels

def load_and_run(filepath):

	model = keras.models.load_model('saved_model/my_model')

	failure = False

	if len(filepath) > 0:
		img_width, img_height = 227, 227
		img = load_img(filepath, target_size = (img_width, img_height))

		img.show()
		
		img = img_to_array(img)

		return run(img)

	else: 
		print("upload failure")
		exit()

	return np.argmax(pred)

def run(img):

	img = np.expand_dims(img,axis=0)

	model = keras.models.load_model('saved_model/my_model')

	pred = model.predict(img)

	print(pred)
	print(np.argmax(pred))

	return np.argmax(pred)