#include <iostream>

#include "highgui/highgui.hpp"
#include "core/core.hpp"
#include "opencv.hpp"

// cv::
using namespace cv;

Mat RBGtoGrey(Mat RBG);
Mat EqualizeHistogram(Mat grey);

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

	// Equalize image
	Mat EQimg = EqualizeHistogram(greyImage);
	imshow("EQ scaled Car Image", EQimg);

	// Without this function the image will close immediately
	waitKey();
}

Mat EqualizeHistogram(Mat grey)
{
	Mat EQ = grey.clone();

	// 1. Pixel count
	int count[256] = { 0 };
	for (int i = 0; i < grey.rows; i++)
		for (int j = 0; j < grey.cols; j++)
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