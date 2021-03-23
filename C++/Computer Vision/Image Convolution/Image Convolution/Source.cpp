#include <iostream>

#include "highgui/highgui.hpp"
#include "core/core.hpp"
#include "opencv.hpp"

// cv::
using namespace cv;

Mat RBGtoGrey(Mat RBG);
Mat Avg(Mat grey);
Mat Avg_neighbour(Mat grey, int INeighbour=1);
Mat Max(Mat grey, int INeighbour = 1);
Mat Mini(Mat grey, int INeighbour=1);

int main() {
	// Using the Mat datatype defined in cv
	Mat LPRImage;
	// Load an image
	LPRImage = imread("1.jpg");
	// Display the image
	//imshow("Car Image", LPRImage);

	// Change it to grey scale
	Mat greyImage = RBGtoGrey(LPRImage);
	// Display the grey scaled image as well
	imshow("Grey scaled Car Image", greyImage);
	
	// Blur
	Mat blurred = Avg(greyImage);
	// Display
	//imshow("Blurred Grey scaled Car Image", blurred);

	// Blur more
	Mat blurred_deep = Avg_neighbour(greyImage, 1);
	// Display
	//imshow("Blurred Grey scaled Car Image", blurred_deep);

	// Max mask
	Mat maxed = Max(greyImage, 2);
	// Display
	//imshow("Maxed Grey scaled Car Image", maxed);

	// Mini mask
	Mat mini = Max(greyImage, 2);
	// Display
	imshow("Mini Grey scaled Car Image", mini);

	// Without this function the image will close immediately
	waitKey();
}

// 3*3 Kernel
Mat Avg(Mat grey)
{
	// Create a black grey scaled image
	Mat blurred = Mat::zeros(grey.size(), CV_8UC1);

	// For each row of the image
	for (int i = 0; i < grey.rows; i++)
		// For every three values of the coloumn
		for (int j = 0; j < grey.cols; j++) {
			// Exclude borders
			if (i == 0 || j == 0 || i == grey.rows - 1 || j == grey.cols - 1)
				continue;

			int total = 0;
			// Iterate 3 times
			for (int x = -1; x < 2; x++)
				// Iterate 3 times
				for (int y = -1; y < 2; y++)
					total += grey.at<uchar>(i+x, j+y);
			
			// Set the value to average
			blurred.at<uchar>(i, j) = total/9;
		}

	return blurred;
}

// Different implementation for border exclusion
Mat Avg_neighbour(Mat grey, int INeighbour)
{
	// Create a black grey scaled image
	Mat blurred = Mat::zeros(grey.size(), CV_8UC1);

	// Excludes INeighbour borders
	for (int i = INeighbour; i < grey.rows- INeighbour; i++)
		// Excludes INeighbour borders
		for (int j = INeighbour; j < grey.cols- INeighbour; j++) {
			int total = 0;
			// Reflects the number ot divide by to get the average
			int count = 0;
			// Iterate 3 times
			for (int x = -INeighbour; x <= INeighbour; x++)
				// Iterate 3 times
				for (int y = -INeighbour; y <= INeighbour; y++) {
					count++;
					total += grey.at<uchar>(i + x, j + y);
				}

			// Set the value to average
			blurred.at<uchar>(i, j) = total / count;
		}

	return blurred;
}


Mat Max(Mat grey, int INeighbour)
{
	// Create a black grey scaled image
	Mat maxed = Mat::zeros(grey.size(), CV_8UC1);

	// Excludes INeighbour borders
	for (int i = INeighbour; i < grey.rows - INeighbour; i++)
		// Excludes INeighbour borders
		for (int j = INeighbour; j < grey.cols - INeighbour; j++) {
			int highest = 0;
			// Iterate 3 times
			for (int x = -INeighbour; x <= INeighbour; x++)
				// Iterate 3 times
				for (int y = -INeighbour; y <= INeighbour; y++) {
					int value = grey.at<uchar>(i + x, j + y);
					if(value > highest)
						highest = value;
				}

			maxed.at<uchar>(i, j) = highest;
		}

	return maxed;
}

Mat Mini(Mat grey, int INeighbour)
{
	// Create a black grey scaled image
	Mat mini = Mat::zeros(grey.size(), CV_8UC1);

	// Excludes INeighbour borders
	for (int i = INeighbour; i < grey.rows - INeighbour; i++)
		// Excludes INeighbour borders
		for (int j = INeighbour; j < grey.cols - INeighbour; j++) {
			int lowest = 0;
			// Iterate 3 times
			for (int x = -INeighbour; x <= INeighbour; x++)
				// Iterate 3 times
				for (int y = -INeighbour; y <= INeighbour; y++) {
					int value = grey.at<uchar>(i + x, j + y);
					if (value > lowest)
						lowest = value;
				}

			mini.at<uchar>(i, j) = lowest;
		}

	return mini;
}

Mat RBGtoGrey(Mat RGB) {
	// Create a black grey scaled image
	Mat grey = Mat::zeros(RGB.size(), CV_8UC1);

	// For each row of the image
	for (int i = 0; i < RGB.rows; i++)
		// For every three values of the coloumn
		for (int j = 0; j < RGB.cols * 3; j += 3) {
			// Average the three RGB channels
			int grey_value = (RGB.at<uchar>(i, j) + RGB.at<uchar>(i, j + 1) + RGB.at<uchar>(i, j + 2)) / 3;
			// Assign them to the respective pixel
			grey.at<uchar>(i, j / 3) = grey_value;
		}

	return grey;
}