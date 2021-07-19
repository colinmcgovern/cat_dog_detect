import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import os
import time
from PIL import Image

import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img

import utility

train_neg_images,train_neg_labels = utility.get_neg()
train_pos_images,train_pos_labels = utility.get_pos()

cur_dir = os.getcwd()

i = 0

num_neg_tests = 300
num_pos_tests = 300

utility.clear(cur_dir+"/evaluation/TN")
utility.clear(cur_dir+"/evaluation/FP")
utility.clear(cur_dir+"/evaluation/TP")
utility.clear(cur_dir+"/evaluation/FN")

for img in train_neg_images:

	if(i>num_neg_tests):
		break

	pred = utility.run(img)
	if(pred==0):
		print("correct")
		array_to_img(img).save(os.path.join(cur_dir,"evaluation/TN",str(i)+".jpeg"))
		i += 1
	else:
		print("incorrect")
		array_to_img(img).save(os.path.join(cur_dir,"evaluation/FP",str(i)+".jpeg"))
		i += 1

for img in train_pos_images:

	pred = utility.run(img)
	
	if(i>num_pos_tests+num_neg_tests):
		break

	if(pred):
		print("correct")
		array_to_img(img).save(os.path.join(cur_dir,"evaluation/TP",str(i)+".jpeg"))
		i += 1
	else:
		print("incorrect")
		array_to_img(img).save(os.path.join(cur_dir,"evaluation/FN",str(i)+".jpeg"))
		i += 1
