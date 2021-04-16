# Morphological operations for LPR plate detection

<img src="../../../Snippets/C++/CV/edge%20detection/Vertical%20Sobel.png" height="300" alt="vertical Sobel">

Looking closely at the characters of the image altered by vertical edge detection, we see that characters are segmented, so let us apply some morphological operations remove those segments.

## Dilation

Dilation is a morphological method used to increase the white pixels' density which in our case will bridge the gap between characters and reduce segmentation. We start by testing different dilation kernels to find the best one to remove all segments.

<img src="../../../Snippets/C++/CV/morphological%20operations/dilation.png" height="300" alt="vertical Sobel">

A 9x9 kernel is the smallest that removes all segments. Since the task is to pre-process the image for LPR plate detection, we do not care if the characters are not readable.

## Erosion

Since dilation increases the white's density, any surrounding noise will increase, thus we erode those noises before dilating the image a process known as **opening**. With trial, we reach the following choices of neighbor consideration in our two functions:

```c++
 /* Opening */
 // Erode Image
 Mat erodedImg = Erosion(verical_edge);
 // Dilate the Eroded image
 imshow("morophogical opening mask", Dilation(erodedImg, 6));
```

Those configurations give the following image:

<img src="../../../Snippets/C++/CV/morphological%20operations/opening.png" height="300" alt="vertical Sobel">
