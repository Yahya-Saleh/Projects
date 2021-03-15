#include <iostream>

#include "highgui/highgui.hpp"
#include "core/core.hpp"
#include "opencv.hpp"

// cv::
using namespace cv;

int main() {
	// Using the Mat datatype defined in cv
	Mat LPRImage;
	// Load an image
	LPRImage = imread("1.jpg");

	// Display the image
	imshow("Car Image", LPRImage);
	// Without this function the image will close immediately
	waitKey();
}