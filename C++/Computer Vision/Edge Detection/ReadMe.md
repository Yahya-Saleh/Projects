# Edge detection

Image detection is a very import task of CV and this projects leverages both Laplacian and Sobel's algorithms to detect vertical, horizontal, or both edges.

## Preprocessing

Before we start with edge detection we apply some preprocessing to the image

```c++
// Using the Mat datatype defined in cv
 Mat LPRImage;
 // Load an image
 LPRImage = imread("1.jpg");
 // Change it to grey scale
 Mat greyImage = RBGtoGrey(LPRImage);
 // Equalize the image
 Mat EQImg = EqualizeHistogram(greyImage);
 // Blur the image to remove any noise
 Mat blurred = Avg_neighbour(EQImg);
```

- We will convert the image to grey scale, since color will not affect the execution result, and thus we decrease the number of operations to perform by converting the image to grey scale as now we have less channels to handle.
- We will then equalize the image to get an adequate contrast.
- Lastly, we will blur the image a little with `INeighbour=1` to remove some of the noise.

## Laplacian

What we will do in our implementation is apply the kernel and if the value is above the threshold, usually 50, we will make it white and black otherwise. This approach will make visualizing the edges detected easier:

<img src="../../../Snippets/C++/CV/edge%20detection/Laplacian.png" height="300" alt="Laplacian">

## Sobel

Since our goal is to detect a car plate image, we will go about this in a different matter. Rather than applying both the `Gx` and `Gy` kernel we will apply one at a time. This way we can either detect vertical or horizontal edges, respectively. As we will see detecting only the vertical edges is more effective than detecting both.

We implement a function that will either apply Gx or Gy depending on the given parameter, and here's the results:

<img src="../../../Snippets/C++/CV/edge%20detection/sobel.png" height="300" alt="sobel">

We can see that vertical edge detection is better than an all edge detection in locating characters because of their nature.
