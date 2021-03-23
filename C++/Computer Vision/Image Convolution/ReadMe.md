# Image Convolution

A very powerful tool in image preprocessing.

## Blur

Using the average kernel matrix we can blur the image. Here's a `9*9` average kernel:

![Blurry image](../../../Snippets/C++/CV/convolution/blur.jpg)

A 9*9 kernel matrix looks at 4 neighbors. The higher the neighbors the more blurry the image will become as it blends with more neighbors.

## Max

The max kernel matrix will also blur an image focusing on the pixel with the highest values from the neighbors.

Here's an example looking at 2 neighbors (`5*5`):

![Max mask](../../../Snippets/C++/CV/convolution/max.jpg)

## Mini

Likewise, the mini kernel matrix will blur focusing on a the lowest values among the neighbors

Here's an example looking at 2 neighbors (`5*5`):


![Mini mask](../../../Snippets/C++/CV/convolution/mini.jpg)
