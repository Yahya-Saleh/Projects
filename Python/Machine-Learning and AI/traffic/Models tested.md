# Models tested

- [Models tested](#models-tested)
  - [First model](#first-model)
    - [Performance 1 (Accuracy: 97.64%)](#performance-1-accuracy-9764)
  - [Second model](#second-model)
    - [Performance 2 (Accuracy: 93.99%)](#performance-2-accuracy-9399)
  - [Third model](#third-model)
    - [Performance 3 (Accuracy: 96.05%)](#performance-3-accuracy-9605)
  - [Fourth Model](#fourth-model)
    - [Performance 4 (Accuracy: 95.05%)](#performance-4-accuracy-9505)
  - [Fifth Model](#fifth-model)
    - [Performance 5 (Accuracy: 96.89%)](#performance-5-accuracy-9689)
  - [Sixth model](#sixth-model)
    - [Performance 6 (Accuracy: 97.74%)](#performance-6-accuracy-9774)
  - [Seventh model](#seventh-model)
    - [Performance 7 (Accuracy: 96.63%)](#performance-7-accuracy-9663)
  - [Eighth Model](#eighth-model)
    - [Performance 8 (Accuracy: 96.416)](#performance-8-accuracy-96416)
  - [Ninth Model](#ninth-model)
    - [Performance (Accuracy: 98.25)](#performance-accuracy-9825)
  - [Tenth Model](#tenth-model)
    - [Performance 10 (Accuracy: 98.12%)](#performance-10-accuracy-9812)

## First model

The first model had 3 layers of convolution, two max-pooling layer, and one hidden layer:

- Convolution layer
  - 32 filter
  - 3x3 Kernel-matrix
  - relu activation function
- Max-pooling (2x2 grid)
- Convolution layer
  - 64 filter
  - 3x3 Kernel-matrix
  - relu activation function
- Max-pooling (2x2 grid)
- Convolution layer
  - 64 filter
  - 3x3 Kernel-matrix
  - relu activation function
- Dense Hidden layer
  - 128 units
  - relu activation function
  - 50% drop-out

### Performance 1 (Accuracy: 97.64%)

```bash
> python -u traffic.py gtsrb model_1.h
Epoch 1/10
500/500 [==============================] - 8s 15ms/step - loss: 2.5218 - accuracy: 0.3801
Epoch 2/10
500/500 [==============================] - 8s 15ms/step - loss: 0.8473 - accuracy: 0.7501
Epoch 3/10
500/500 [==============================] - 8s 15ms/step - loss: 0.4825 - accuracy: 0.8559
Epoch 4/10
500/500 [==============================] - 8s 16ms/step - loss: 0.3436 - accuracy: 0.8978
Epoch 5/10
500/500 [==============================] - 8s 15ms/step - loss: 0.2900 - accuracy: 0.9167
Epoch 6/10
500/500 [==============================] - 8s 15ms/step - loss: 0.2343 - accuracy: 0.9337
Epoch 7/10
500/500 [==============================] - 8s 15ms/step - loss: 0.1958 - accuracy: 0.9448
Epoch 8/10
500/500 [==============================] - 8s 15ms/step - loss: 0.2037 - accuracy: 0.9437
Epoch 9/10
500/500 [==============================] - 8s 15ms/step - loss: 0.1792 - accuracy: 0.9491
Epoch 10/10
500/500 [==============================] - 8s 15ms/step - loss: 0.1505 - accuracy: 0.9580
333/333 - 1s - loss: 0.1002 - accuracy: 0.9764
```

## Second model

This model had the same layers as the first model with the addition of a second hidden layer of the same configuration as this first. Adding the second layer decreased the accuracy.

### Performance 2 (Accuracy: 93.99%)

```bash
> python -u traffic.py gtsrb model_2.h
Epoch 1/10
500/500 [==============================] - 8s 16ms/step - loss: 3.6452 - accuracy: 0.1503
Epoch 2/10
500/500 [==============================] - 8s 15ms/step - loss: 2.0789 - accuracy: 0.4113
Epoch 3/10
500/500 [==============================] - 8s 15ms/step - loss: 1.4416 - accuracy: 0.5733
Epoch 4/10
500/500 [==============================] - 8s 15ms/step - loss: 1.0693 - accuracy: 0.6844
Epoch 5/10
500/500 [==============================] - 8s 15ms/step - loss: 0.8000 - accuracy: 0.7601
Epoch 6/10
500/500 [==============================] - 8s 15ms/step - loss: 0.6765 - accuracy: 0.7993
Epoch 7/10
500/500 [==============================] - 8s 15ms/step - loss: 0.6078 - accuracy: 0.8227
Epoch 8/10
500/500 [==============================] - 8s 15ms/step - loss: 0.4849 - accuracy: 0.8584
Epoch 9/10
500/500 [==============================] - 8s 15ms/step - loss: 0.4490 - accuracy: 0.8721
Epoch 10/10
500/500 [==============================] - 8s 16ms/step - loss: 0.4121 - accuracy: 0.8843
333/333 - 1s - loss: 0.2331 - accuracy: 0.9399
```

## Third model

This model is identical to the first model, but with no hidden layers.

### Performance 3 (Accuracy: 96.05%)

```bash
> python -u traffic.py gtsrb model_3.h
Epoch 1/10
500/500 [==============================] - 7s 15ms/step - loss: 1.6373 - accuracy: 0.6440
Epoch 2/10
500/500 [==============================] - 7s 15ms/step - loss: 0.3134 - accuracy: 0.9223
Epoch 3/10
500/500 [==============================] - 7s 15ms/step - loss: 0.1787 - accuracy: 0.9534
Epoch 4/10
500/500 [==============================] - 7s 15ms/step - loss: 0.1245 - accuracy: 0.9668
Epoch 5/10
500/500 [==============================] - 7s 15ms/step - loss: 0.1208 - accuracy: 0.9695
Epoch 6/10
500/500 [==============================] - 7s 15ms/step - loss: 0.1272 - accuracy: 0.9666
Epoch 7/10
500/500 [==============================] - 8s 15ms/step - loss: 0.0793 - accuracy: 0.9810
Epoch 8/10
500/500 [==============================] - 8s 15ms/step - loss: 0.0807 - accuracy: 0.9791
Epoch 9/10
500/500 [==============================] - 7s 15ms/step - loss: 0.0999 - accuracy: 0.9755
Epoch 10/10
500/500 [==============================] - 7s 15ms/step - loss: 0.1080 - accuracy: 0.9745
333/333 - 1s - loss: 0.2372 - accuracy: 0.9605
```

## Fourth Model

This model has an additional max-pool layer after the third convolution layer.

### Performance 4 (Accuracy: 95.05%)

```bash
> python -u traffic.py gtsrb model_4.h
Epoch 1/10
500/500 [==============================] - 8s 15ms/step - loss: 3.2331 - accuracy: 0.2257
Epoch 2/10
500/500 [==============================] - 8s 15ms/step - loss: 1.4822 - accuracy: 0.5633
Epoch 3/10
500/500 [==============================] - 8s 15ms/step - loss: 0.8647 - accuracy: 0.7424
Epoch 4/10
500/500 [==============================] - 8s 15ms/step - loss: 0.5946 - accuracy: 0.8283
Epoch 5/10
500/500 [==============================] - 8s 15ms/step - loss: 0.4569 - accuracy: 0.8681
Epoch 6/10
500/500 [==============================] - 8s 15ms/step - loss: 0.3509 - accuracy: 0.8966
Epoch 7/10
500/500 [==============================] - 8s 15ms/step - loss: 0.3180 - accuracy: 0.9098
Epoch 8/10
500/500 [==============================] - 8s 15ms/step - loss: 0.2615 - accuracy: 0.9273
Epoch 9/10
500/500 [==============================] - 8s 15ms/step - loss: 0.2651 - accuracy: 0.9286
Epoch 10/10
500/500 [==============================] - 8s 15ms/step - loss: 0.2317 - accuracy: 0.9336
333/333 - 1s - loss: 0.1902 - accuracy: 0.9505
```

## Fifth Model

In this model the first convolution layer was altered to generate 64 filters.

### Performance 5 (Accuracy: 96.89%)

```bash
> python -u "c:\Users\tp057094\Desktop\Traffic\traffic.py" gtsrb model_5.h
Epoch 1/10
500/500 [==============================] - 13s 26ms/step - loss: 2.8695 - accuracy: 0.3169
Epoch 2/10
500/500 [==============================] - 13s 27ms/step - loss: 1.1157 - accuracy: 0.6772
Epoch 3/10
500/500 [==============================] - 13s 27ms/step - loss: 0.6729 - accuracy: 0.8099
Epoch 4/10
500/500 [==============================] - 14s 28ms/step - loss: 0.4746 - accuracy: 0.8647
Epoch 5/10
500/500 [==============================] - 13s 26ms/step - loss: 0.3868 - accuracy: 0.8914
Epoch 6/10
500/500 [==============================] - 13s 26ms/step - loss: 0.3447 - accuracy: 0.9042
Epoch 7/10
500/500 [==============================] - 13s 26ms/step - loss: 0.2790 - accuracy: 0.9219
Epoch 8/10
500/500 [==============================] - 13s 26ms/step - loss: 0.2398 - accuracy: 0.9308
Epoch 9/10
500/500 [==============================] - 13s 26ms/step - loss: 0.2245 - accuracy: 0.9393
Epoch 10/10
500/500 [==============================] - 14s 28ms/step - loss: 0.2286 - accuracy: 0.9411
333/333 - 2s - loss: 0.1174 - accuracy: 0.9689
```

## Sixth model

The second convolution layer was altered to inference 32 filters instead of 64.

### Performance 6 (Accuracy: 97.74%)

```bash
> python -u "c:\Users\tp057094\Desktop\Traffic\traffic.py" gtsrb model_6.h
Epoch 1/10
500/500 [==============================] - 6s 13ms/step - loss: 2.1431 - accuracy: 0.4730
Epoch 2/10
500/500 [==============================] - 6s 13ms/step - loss: 0.6896 - accuracy: 0.8032
Epoch 3/10
500/500 [==============================] - 6s 13ms/step - loss: 0.4028 - accuracy: 0.8822
Epoch 4/10
500/500 [==============================] - 6s 13ms/step - loss: 0.3172 - accuracy: 0.9082
Epoch 5/10
500/500 [==============================] - 6s 13ms/step - loss: 0.2660 - accuracy: 0.9225
Epoch 6/10
500/500 [==============================] - 6s 13ms/step - loss: 0.2283 - accuracy: 0.9359
Epoch 7/10
500/500 [==============================] - 6s 13ms/step - loss: 0.1968 - accuracy: 0.9443
Epoch 8/10
500/500 [==============================] - 6s 13ms/step - loss: 0.1795 - accuracy: 0.9500
Epoch 9/10
500/500 [==============================] - 6s 13ms/step - loss: 0.1689 - accuracy: 0.9533
Epoch 10/10
500/500 [==============================] - 6s 13ms/step - loss: 0.1500 - accuracy: 0.9581
333/333 - 1s - loss: 0.0879 - accuracy: 0.9774
```

## Seventh model

The seventh model is based on the sixth with the exception that the first convolution layer inferences 16 filters instead of 32.

### Performance 7 (Accuracy: 96.63%)

```bash
> python -u "c:\Users\tp057094\Desktop\Traffic\traffic.py" gtsrb model_7.h
500/500 [==============================] - 4s 8ms/step - loss: 2.7080 - accuracy: 0.3826
Epoch 2/10
500/500 [==============================] - 4s 8ms/step - loss: 0.9495 - accuracy: 0.7290
Epoch 3/10
500/500 [==============================] - 4s 8ms/step - loss: 0.5562 - accuracy: 0.8425
Epoch 4/10
500/500 [==============================] - 4s 8ms/step - loss: 0.4224 - accuracy: 0.8806
Epoch 5/10
500/500 [==============================] - 4s 8ms/step - loss: 0.3588 - accuracy: 0.8998
Epoch 6/10
500/500 [==============================] - 4s 8ms/step - loss: 0.2839 - accuracy: 0.9186
Epoch 7/10
500/500 [==============================] - 4s 8ms/step - loss: 0.2511 - accuracy: 0.9292
Epoch 8/10
500/500 [==============================] - 4s 8ms/step - loss: 0.2172 - accuracy: 0.9374
Epoch 9/10
500/500 [==============================] - 4s 8ms/step - loss: 0.2127 - accuracy: 0.9400
Epoch 10/10
500/500 [==============================] - 4s 8ms/step - loss: 0.1989 - accuracy: 0.9452
333/333 - 1s - loss: 0.1410 - accuracy: 0.9663
```

## Eighth Model

This model is based on the sixth model and its last convolution layer inferences 80 filters instead of 64.

### Performance 8 (Accuracy: 96.416)

```bash
> python -u "c:\Users\tp057094\Desktop\Traffic\traffic.py" gtsrb model_8.h
Epoch 1/10
500/500 [==============================] - 6s 13ms/step - loss: 2.3903 - accuracy: 0.4164
Epoch 2/10
500/500 [==============================] - 6s 13ms/step - loss: 0.8853 - accuracy: 0.7466
Epoch 3/10
500/500 [==============================] - 6s 13ms/step - loss: 0.5435 - accuracy: 0.8420
Epoch 4/10
500/500 [==============================] - 6s 13ms/step - loss: 0.4027 - accuracy: 0.8811
Epoch 5/10
500/500 [==============================] - 6s 13ms/step - loss: 0.3248 - accuracy: 0.9052
Epoch 6/10
500/500 [==============================] - 6s 13ms/step - loss: 0.2968 - accuracy: 0.9109
Epoch 7/10
500/500 [==============================] - 6s 13ms/step - loss: 0.2370 - accuracy: 0.9308
Epoch 8/10
500/500 [==============================] - 6s 13ms/step - loss: 0.2239 - accuracy: 0.9334
Epoch 9/10
500/500 [==============================] - 6s 13ms/step - loss: 0.1944 - accuracy: 0.9416
Epoch 10/10
500/500 [==============================] - 6s 13ms/step - loss: 0.2089 - accuracy: 0.9392
333/333 - 1s - loss: 0.1218 - accuracy: 0.9646
```

## Ninth Model

- Convolution layer
  - 32 filter
  - 3x3 Kernel-matrix
  - relu activation function
- Max-pooling (2x2 grid)
- Convolution layer
  - 32 filter
  - 3x3 Kernel-matrix
  - relu activation function
- Convolution layer
  - 32 filter
  - 3x3 Kernel-matrix
  - relu activation function
- Max-pooling (2x2 grid)
- Convolution layer
  - 64 filter
  - 3x3 Kernel-matrix
  - relu activation function
- Dense Hidden layer
  - 128 units
  - relu activation function
  - 50% drop-out

### Performance (Accuracy: 98.25)

```bash
> python -u "c:\Users\tp057094\Desktop\Traffic\traffic.py" gtsrb model_9.h
Epoch 1/10
500/500 [==============================] - 8s 16ms/step - loss: 2.0908 - accuracy: 0.4800
Epoch 2/10
500/500 [==============================] - 8s 16ms/step - loss: 0.6635 - accuracy: 0.8154
Epoch 3/10
500/500 [==============================] - 8s 16ms/step - loss: 0.4031 - accuracy: 0.8862
Epoch 4/10
500/500 [==============================] - 8s 16ms/step - loss: 0.2915 - accuracy: 0.9171
Epoch 5/10
500/500 [==============================] - 8s 16ms/step - loss: 0.2290 - accuracy: 0.9364
Epoch 6/10
500/500 [==============================] - 8s 16ms/step - loss: 0.2105 - accuracy: 0.9398
Epoch 7/10
500/500 [==============================] - 8s 16ms/step - loss: 0.1777 - accuracy: 0.9529
Epoch 8/10
500/500 [==============================] - 8s 16ms/step - loss: 0.1648 - accuracy: 0.9542
Epoch 9/10
500/500 [==============================] - 8s 16ms/step - loss: 0.1482 - accuracy: 0.9586
Epoch 10/10
500/500 [==============================] - 8s 16ms/step - loss: 0.1442 - accuracy: 0.9609
333/333 - 1s - loss: 0.0751 - accuracy: 0.9825
```

## Tenth Model

- Convolution layer
  - 32 filter
  - 3x3 Kernel-matrix
  - relu activation function

- Max-pooling (2x2 grid)
- Convolution layer
  - 32 filter
  - 3x3 Kernel-matrix
  - relu activation function
- Convolution layer
  - 32 filter
  - 3x3 Kernel-matrix
  - relu activation function

- Max-pooling (2x2 grid)
- Convolution layer
  - 64 filter
  - 3x3 Kernel-matrix
  - relu activation function
- Convolution layer
  - 64 filter
  - 3x3 Kernel-matrix
  - relu activation function

- Dense Hidden layer
  - 128 units
  - relu activation function
  - 50% drop-out

### Performance 10 (Accuracy: 98.12%)

```bash
> python -u "c:\Users\tp057094\Desktop\Traffic\traffic.py" gtsrb model_10.h
Epoch 1/10
500/500 [==============================] - 8s 16ms/step - loss: 1.9168 - accuracy: 0.4969
Epoch 2/10
500/500 [==============================] - 8s 16ms/step - loss: 0.5639 - accuracy: 0.8423
Epoch 3/10
500/500 [==============================] - 8s 16ms/step - loss: 0.3030 - accuracy: 0.9152
Epoch 4/10
500/500 [==============================] - 8s 16ms/step - loss: 0.2092 - accuracy: 0.9440
Epoch 5/10
500/500 [==============================] - 8s 16ms/step - loss: 0.1675 - accuracy: 0.9536
Epoch 6/10
500/500 [==============================] - 8s 16ms/step - loss: 0.1752 - accuracy: 0.9533
Epoch 7/10
500/500 [==============================] - 8s 16ms/step - loss: 0.1287 - accuracy: 0.9647
Epoch 8/10
500/500 [==============================] - 8s 16ms/step - loss: 0.1225 - accuracy: 0.9669
Epoch 9/10
500/500 [==============================] - 8s 16ms/step - loss: 0.1273 - accuracy: 0.9658
Epoch 10/10
500/500 [==============================] - 8s 16ms/step - loss: 0.1246 - accuracy: 0.9701
333/333 - 1s - loss: 0.0874 - accuracy: 0.9812
```
