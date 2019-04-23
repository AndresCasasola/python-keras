	
# Importing libraries
import numpy as np
from random import randint
from sklearn.preprocessing import MinMaxScaler
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.utils.vis_utils import plot_model

# Preprocessing Data
a_list = []		# Input list A
b_list = []		# Input list B
c_list = []		# Knowledged output to train
x_list = []		# Input list X to predict

for i in range (3000):
	a_value = randint(0, 50)
	x_value = randint(0, 50)
	
	if a_value > 25:
		c_value = 1
	else:
		c_value = 0
	
	a_list.append(a_value)
	c_list.append(c_value)
	x_list.append(x_value)

a_array = np.array(a_list)
b_array = np.array(b_list)
c_array = np.array(c_list)
x_array = np.array(x_list)

print("A values:")
for i in range (30):
	print(a_array[i])

print("C values:")	
for i in range(30):
	print(c_array[i])
	
scaler = MinMaxScaler(feature_range=(0,1))
scaled_a_samples = scaler.fit_transform((a_array).reshape(-1,1))
scaled_c_samples = scaler.fit_transform((c_array).reshape(-1,1))
scaled_x_samples = scaler.fit_transform((x_array).reshape(-1,1))


# Creating neural network
model = Sequential([
    Dense(16, input_shape=(1,), activation = 'relu'),		# input_shape=(1,) <=> input_dim=1
    Dense(32, activation = 'relu'),
    Dense(2, activation = 'softmax'),
    
])

model.summary()

# Plot neural network
#plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)

# Training neural network
print("Training...")
model.compile(Adam(lr=.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(scaled_a_samples, scaled_c_samples, validation_split = 0.1, batch_size=10, epochs=20, shuffle=True, verbose=2)

# Predicting
print("Predicting...")
predictions = model.predict(scaled_x_samples, batch_size=10, verbose=0)

print("X Values:")
for i in range(10):
    print(x_array[i])

#print("Predictions...")
#for i in range(10):
#    print(predictions[i])

print("Rounded predictions...")
rounded_predictions = model.predict_classes(scaled_x_samples, batch_size=10, verbose=0)

for i in range(10):
    print(rounded_predictions[i])



