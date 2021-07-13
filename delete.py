import numpy as np
import tensorflow as tf

img_data = np.random.random(size=(100, 100, 3))
img = tf.keras.preprocessing.image.array_to_img(img_data)
array = tf.keras.preprocessing.image.img_to_array(img)
img.show()

# img = np.expand_dims(img, axis = 0)
# model.predict(img)