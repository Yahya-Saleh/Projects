#include <iostream>

#include "highgui/highgui.hpp"
#include "core/core.hpp"
#include "opencv.hpp"

// cv::
using namespace cv;

Mat RBGtoGrey(Mat RBG);
Mat GreytoBinary(Mat Grey);

int main() {
	// Using the Mat datatype defined in cv
	Mat LPRImage;
	// Load an image
	LPRImage = imread("1.jpg");
	// Display the image
	imshow("Car Image", LPRImage);

	// Change it to grey scale
	Mat greyImage = RBGtoGrey(LPRImage);
	// Display the grey scaled image as well
	imshow("Grey scaled Car Image", greyImage);

	// Change it to grey scale
	Mat binaryImage = GreytoBinary(greyImage);
	// Display the grey scaled image as well
	imshow("Binary Car Image", binaryImage);

	// Without this function the image will close immediately
	waitKey();
}

Mat RBGtoGrey(Mat RGB){
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

Mat GreytoBinary(Mat Grey) {
	Mat Binary = Mat::zeros(Grey.size(), CV_8UC1);

	// For each row of the image
	for (int i = 0; i < Grey.rows; i++)
		// For every three values of the coloumn
		for (int j = 0; j < Grey.cols; j++)
			// Assign them to the respective pixel
			Binary.at<uchar>(i, j) = Grey.at<uchar>(i, j) >= 128? 255 : 0;
	
	return Binary;
}