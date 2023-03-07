import tensorflow as tf
from tensorflow import keras
from keras.datasets import fashion_mnist
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# Pull out data from dataset (we use predifined Keras dataset (70k of 28*28 images))
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


# Show data 
#print(train_labels[0])
#print(train_images[0])
#plt.imshow(train_images[40000], cmap = 'gray', vmin = 0, vmax = 255)
#plt.show()


model = keras.Sequential([

    # input is a 28*28 image ("Flatten" flattens the 28*28 into a single 784*1 input layer)
    keras.layers.Flatten(input_shape=(28,28)),

    # hidden layer is 128 deep. relu returns the value, or 0 (works good enough, much faster)
    keras.layers.Dense(128, activation=tf.nn.relu),

    # output is 0-10 (depending on what piece of clothing it is). return maximum
    keras.layers.Dense(10, activation=tf.nn.softmax)
])
 
# Compile our model
model.compile(optimizer=tf.optimizers.Adam(), loss='sparse_categorical_crossentropy')

# Train our model, using our training data
model.fit(train_images, train_labels, epochs=5)

# Test our model, using our training data
test_loss = model.evaluate(test_images, test_labels)

# Make predictions
predictions = model.predict(test_images)

# Print our predictions
print(list(predictions[0]).index(max(predictions[0])))
# Print the correct answer
print(test_labels[0])
plt.imshow(train_images[0], cmap = 'gray', vmin = 0, vmax = 255)
plt.show()

