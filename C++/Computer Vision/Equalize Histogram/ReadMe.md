# Image Histogram Equalization

Histogram equalization is a method to process images in order to adjust the contrast of an image by modifying the intensity distribution of the histogram. The objective of this technique is to give a linear trend to the cumulative probability function associated to the image.

<img src="../../../Snippets/C++/CV/Image%20Histogram%20Equalization/Images'%20histogram.png" height="300" alt="Images' histogram">

The goal is to take an image that is not Equalized, shown above, and improve its contrast for better processing.

## Process

here are the steps of Equalizing an image:

```c++
Mat EqualizeHistogram(Mat grey)
{
 Mat EQ = grey.clone();

 // 1. Pixel count
 int count[256] = { 0 };
 for (int i = 0; i < grey.cols; i++)
  for (int j = 0; j < grey.rows; j++)
   count[grey.at<uchar>(i, j)]++;
 
 // 2. Probability
 float probability[256];
 float img_size = grey.cols * grey.rows;
 for (int i = 0; i < 256; i++)
  probability[i] = (float) count[i] / img_size;

 // 3. Accumulative probability
 float acc_probability[256];
 acc_probability[0] = probability[0];
 for (int i = 1; i < 256; i++)
  acc_probability[i] = probability[i] + acc_probability[i-1];

 // 4. Evaluate the new pixel value (G - 1 = 255)
 for (int i = 0; i < EQ.rows; i++)
  for (int j = 0; j < EQ.cols; j++)
   EQ.at<uchar>(i, j) = (int)(acc_probability[grey.at<uchar>(i, j)] * 255);
 
 return EQ;
}
```

Here's an example of an image after getting equalized:

<img src="../../../Snippets/C++/CV/Image%20Histogram%20Equalization/Equalized%20image.jpg" height="300" alt="Images' histogram">
