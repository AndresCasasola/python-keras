###########################################################
#
# - Description: 
#
# - This code is based on cifar10_cnn.py  example  uploaded
#   in Keras  github  repository  named  as  cifar10_cnn.py:
#   https://github.com/keras-team/keras/blob/master/
#   examples/cifar10_cnn.py
#
# - Some code are taken from https://appliedmachinelearning
#   .blog/2018/03/24/achieving-90-accuracy-in-object-
#   recognition-task-on-cifar-10-dataset-with-keras-
#   convolutional-neural-networks/
#
# - Modifications by: Andres Casasola Dominguez.
#
###########################################################

########## Libraries
import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
import os
# Libraries to show images and labels
from matplotlib import pyplot as plt
from matplotlib import pyplot
from scipy.misc import toimage # If import error: needs to install Pillow (pip install Pillow)
import numpy as np
import threading
from threading import Thread
import time
import csv

########## Configuration parameters
batch_size = 32
num_classes = 10
epochs = 5
steps_per_epoch = 10
evaluation_samples = 200
data_augmentation = True
save_dir = os.path.join(os.getcwd(), 'saved_models')
model_name = 'andres_keras_cifar10_trained_model.h5'

######################################## Functions definition
def show_images(X):
  pyplot.figure(1)
  k = 0
  for i in range(0,4):
      for j in range(0,4):
          pyplot.subplot2grid((4,4),(i,j))
          pyplot.imshow(toimage(X[k]))
          k = k+1
  # show the plot
  pyplot.show()
def show_images2(X): # This function could be useful to understand datagen.flow() and reshape()
	# Configure batch size and retrieve one batch of images
	for X_batch, y_batch in datagen.flow(x_train, y_train, batch_size=9):
		# Show 9 images
		for i in range(0, 9):
			plt.subplot(330 + 1 + i)
	  	#plt.imshow(toimage(X_batch[i].reshape(img_rows, img_cols, 3)))
			plt.imshow(toimage(X_batch[i].reshape(32, 32, 3)))
		# show the plot
		plt.show()
		break
def csvwrite_acc_loss(filename):
	with open(filename, mode='w') as csvfile:
		fieldnames = ['Accuracy', 'Losses']
		csvwriter = csv.writer(csvfile, delimiter='\t')

		csvwriter.writerow(fieldnames)
		data_length = int(len(history.history['acc']))
		for i in range(data_length):
			csvwriter.writerow([history.history['acc'][i], history.history['loss'][i]])
######################################## Functions definition 

########## Preprocessing data
# The data, split between train and test sets:
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# Convert class vectors to binary class matrices.
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

########## Create neural network model
model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same',
                 input_shape=x_train.shape[1:]))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes))
model.add(Activation('softmax'))

# initiate RMSprop optimizer
opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)

########## Compile and Fit
# Let's train the model using RMSprop
model.compile(loss='categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

if not data_augmentation:
    print('Not using data augmentation.')
    model.fit(x_train, y_train,
              batch_size=batch_size,
              epochs=epochs,
              validation_data=(x_test, y_test),
              shuffle=True)
else:
    print('Using real-time data augmentation.')
    # This will do preprocessing and realtime data augmentation:
    datagen = ImageDataGenerator(
        featurewise_center=False,  # set input mean to 0 over the dataset
        samplewise_center=False,  # set each sample mean to 0
        featurewise_std_normalization=False,  # divide inputs by std of the dataset
        samplewise_std_normalization=False,  # divide each input by its std
        zca_whitening=False,  # apply ZCA whitening
        zca_epsilon=1e-06,  # epsilon for ZCA whitening
        rotation_range=0,  # randomly rotate images in the range (degrees, 0 to 180)
        # randomly shift images horizontally (fraction of total width)
        width_shift_range=0.1,
        # randomly shift images vertically (fraction of total height)
        height_shift_range=0.1,
        shear_range=0.,  # set range for random shear
        zoom_range=0.,  # set range for random zoom
        channel_shift_range=0.,  # set range for random channel shifts
        # set mode for filling points outside the input boundaries
        fill_mode='nearest',
        cval=0.,  # value used for fill_mode = "constant"
        horizontal_flip=True,  # randomly flip images
        vertical_flip=False,  # randomly flip images
        # set rescaling factor (applied before any other transformation)
        rescale=None,
        # set function that will be applied on each input
        preprocessing_function=None,
        # image data format, either "channels_first" or "channels_last"
        data_format=None,
        # fraction of images reserved for validation (strictly between 0 and 1)
        validation_split=0.0)

    # Compute quantities required for feature-wise normalization
    # (std, mean, and principal components if ZCA whitening is applied).
    datagen.fit(x_train)

#model.load_weights('keras_cifar10_trained_model.h5') # Replace training by loading weights from compiled model

# Fit the model on the batches generated by datagen.flow().
history = model.fit_generator(datagen.flow(x_train, y_train,
                                 batch_size=batch_size),
                    epochs=epochs,
                    validation_data=(x_test, y_test), 
										workers=0,
										steps_per_epoch=steps_per_epoch)

# Save fit data into file
csvwrite_acc_loss('cifar10_acc_loss.txt')

########## Save model and weights
if not os.path.isdir(save_dir):
    os.makedirs(save_dir)
model_path = os.path.join(save_dir, model_name)
model.save(model_path)
print('Saved trained model at %s ' % model_path)

########## Predict
y_pred = model.predict(x_test[0:16])

########## Show prediction results
labels =  ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']
indices = np.argmax(y_pred, 1)
print("Predictions:")
print ([labels[x] for x in indices])
print("Solutions:")
indices2 = np.argmax(y_test[0:16], 1)
print ([labels[x] for x in indices2])

########## Evaluate trained model and show score
score = model.evaluate(x_test[:evaluation_samples], y_test[:evaluation_samples], verbose=1)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

########## Show images
#show_images(x_test[0:16])


