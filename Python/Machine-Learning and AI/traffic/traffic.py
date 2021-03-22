from cv2 import imread, resize
import numpy as np
import os
import sys

import tensorflow as tf

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()



    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    labels = []
    images = []
    # Loop over subdirectory
    for i in range(NUM_CATEGORIES):
        subdir = os.path.join(data_dir, str(i))

        # Loop over each image in the subdirectory
        for img_name in os.listdir(subdir):
            img_path = os.path.join(subdir, img_name)

            # Read the image
            im = imread(img_path, 1)
            # Resize image so they all have a common size
            images.append(resize(im, (IMG_WIDTH, IMG_HEIGHT)))
            # Add the category of the image
            labels.append(i)

    return (images, labels)


def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    # Create the model
    model = tf.keras.models.Sequential()

    # Image Convolution
    model.add(
        tf.keras.layers.Conv2D(
            32, (3, 3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
        )
    )

    model.add(tf.keras.layers.Conv2D(32, (3, 3), activation="relu"))
    model.add(tf.keras.layers.Conv2D(64, (3, 3), activation="relu"))

    model.add(tf.keras.layers.Conv2D(64, (3, 3), activation="relu"))
    model.add(tf.keras.layers.Conv2D(64, (3, 3), activation="relu"))
    model.add(tf.keras.layers.MaxPooling2D((2, 2)))
    
    # Flatten units
    model.add(tf.keras.layers.Flatten())

    # Add a hidden layer with dropout
    model.add(tf.keras.layers.Dense(128, activation="relu"))
    model.add(tf.keras.layers.Dense(128, activation="relu"))
    model.add(tf.keras.layers.Dropout(0.5))

    # Output layer with output units for all road signs.
    model.add(tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax"))

    # Compile the model
    model.compile(
        optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]
    )

    return model


if __name__ == "__main__":
    main()
