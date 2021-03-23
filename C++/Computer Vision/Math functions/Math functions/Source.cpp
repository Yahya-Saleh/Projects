#include <iostream>

#include "highgui/highgui.hpp"
#include "core/core.hpp"
#include "opencv.hpp"

// cv::
using namespace cv;

Mat RBGtoGrey(Mat RBG);
Mat Inversion(Mat grey);
Mat Step(Mat grey, int TH1, int TH2);
Mat Darken(Mat grey, int TH);
Mat Darken_RGB(Mat RGB, int TH);

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
	//imshow("Grey scaled Car Image", greyImage);

	// Invert image
	Mat inverted = Inversion(greyImage);
	// Display
	//imshow("Inverted Grey scaled Car Image", inverted);
	
	// Step function
	Mat stepped = Step(greyImage, 100, 180);
	// Display
	//imshow("Grey scaled Car Image (Step applied)", stepped);

	Mat dark = Darken(greyImage, 80);
	// Display
	//imshow("Darkened Grey scaled Car Image", dark);

	Mat dark_RBG = Darken_RGB(LPRImage, 80);
	imshow("Darkened Car Image", dark_RBG);

	// Without this function the image will close immediately
	waitKey();
}

Mat Inversion(Mat grey) {
	Mat inverted = Mat::zeros(grey.size(), CV_8UC1);

	// For each row of the image
	for (int i = 0; i < grey.rows; i++)
		// For every value of the coloumn
		for (int j = 0; j < grey.cols; j++)
			// inverted_value = 255 - inputted_value
			inverted.at<uchar>(i, j) = 255 - grey.at<uchar>(i, j);

	return inverted;
}

Mat Step(Mat grey, int TH1, int TH2) {
	Mat stepped = Mat::zeros(grey.size(), CV_8UC1);

	// For each row of the image
	for (int i = 0; i < grey.rows; i++)
		// For every value of the coloumn
		for (int j = 0; j < grey.cols; j++) {
			int value = grey.at<uchar>(i, j);
			// inverted_value = 255 - inputted_value
			if (TH1 <= value && value <= TH2)
				stepped.at<uchar>(i, j) = 255;
		}

	return stepped;
}

Mat Darken(Mat grey, int TH) {
	Mat darkened = Mat::zeros(grey.size(), CV_8UC1);

	// For each row of the image
	for (int i = 0; i < grey.rows; i++)
		// For every value of the coloumn
		for (int j = 0; j < grey.cols; j++)
			darkened.at<uchar>(i, j) = grey.at<uchar>(i, j) > TH? TH : grey.at<uchar>(i, j);

	return darkened;
}

Mat Darken_RGB(Mat RGB, int TH) {
	Mat darkened = Mat::zeros(RGB.size(), CV_8UC3);

	// For each row of the image
	for (int i = 0; i < RGB.rows; i++)
		// For every value of the coloumn
		for (int j = 0; j < RGB.cols * 3; j++)
			darkened.at<uchar>(i, j) = RGB.at<uchar>(i, j) > TH ? TH : RGB.at<uchar>(i, j);

	return darkened;
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