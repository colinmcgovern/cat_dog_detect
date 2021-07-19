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

import utility

root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

while True:
	filepath = askopenfilename()
	utility.load_and_run(filepath)

print("done")