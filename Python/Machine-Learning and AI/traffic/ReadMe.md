# Traffic

An AI to identify which traffic sign appears in a photograph. [Watch it in action!](https://youtu.be/a3O-3cGGw_E)

## Table of content

- [Traffic](#traffic)
  - [Table of content](#table-of-content)
  - [Background](#background)
  - [German Traffic Sign Recognition Benchmark Dataset](#german-traffic-sign-recognition-benchmark-dataset)
  - [Traffic.py](#trafficpy)
  - [Acknowledgements](#acknowledgements)

## Background

As research continues in the development of self-driving cars, one of the key challenges is [**computer vision**](https://en.wikipedia.org/wiki/Computer_vision), allowing these cars to develop an understanding of their environment from digital images. In particular, this involves the ability to recognize and distinguish road signs – stop signs, speed limit signs, yield signs, and more.

In this project, we’ll use TensorFlow to build a neural network to classify road signs based on an image of those signs. To do so, we'll use the [German Traffic Sign Recognition Benchmark (GTSRB)](http://benchmark.ini.rub.de/?section=gtsrb&subsection=news) dataset, which contains thousands of images of 43 different kinds of road signs.

---

## German Traffic Sign Recognition Benchmark Dataset

43 subdirectories, numbered 0 through 42, exist in the `gtsrb` directory in this dataset. Each numbered subdirectory represents a different category (a different type of road sign). Within each traffic sign’s directory is a collection of images of that type of traffic sign.

- [Download the full dataset](https://cdn.cs50.net/ai/2020/x/projects/5/gtsrb.zip).
- [Download a modified dataset](https://cdn.cs50.net/ai/2020/x/projects/5/gtsrb-small.zip) with 3 subdirectories.

---

## [Traffic.py](traffic.py)

In the `main` function, we accept as command-line arguments a directory containing the data and (optionally) a filename to which to save the trained model. The data and corresponding labels are then loaded from the data directory (via the `load_data` function) and split into training and testing sets. After that, the `get_model` function is called to obtain a compiled neural network that is then fitted on the training data. The model is then evaluated on the testing data. Finally, if a model filename was provided, the trained model is saved to disk.

---

## Acknowledgements

Data provided by [J. Stallkamp, M. Schlipsing, J. Salmen, and C. Igel. The German Traffic Sign Recognition Benchmark: A multi-class classification competition. In Proceedings of the IEEE International Joint Conference on Neural Networks, pages 1453–1460. 2011](http://benchmark.ini.rub.de/index.php?section=gtsrb&subsection=dataset#Acknowledgements). The `Main` function was implemented by CS50AI staff.
