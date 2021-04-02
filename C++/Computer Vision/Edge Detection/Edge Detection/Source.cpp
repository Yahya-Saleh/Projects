#include <iostream>

#include "highgui/highgui.hpp"
#include "core/core.hpp"
#include "opencv.hpp"

// cv::
using namespace cv;

Mat RBGtoGrey(Mat RBG);
Mat EqualizeHistogram(Mat grey);
Mat Avg_neighbour(Mat grey, int INeighbour=1);
Mat Sobel(Mat grey, int kernel_toUse = 0, int TH=50, int INeighbour=1);
Mat Laplacian(Mat grey, int TH=50, int INeighbour=1);

int main() {
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

	Mat Vsobel = Sobel(blurred);
	imshow("Vertical Sobel Car Image", Vsobel);
	Mat Hsobel = Sobel(blurred, 1);
	imshow("Horizontal Sobel Car Image", Hsobel);

	imshow("Laplacian Car Image", Laplacian(blurred));


	// Without this function the image will close immediately
	waitKey();
}

Mat Sobel(Mat grey, int kernel_toUse, int TH, int INeighbour)
{
	// Declare the kernels
	int Gx[3][3] = { {-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1} };
	int Gy[3][3] = { {-1, -2, -1}, {0, 0, 0}, {1, 2, 1} };

	// Pick the kernel to use
	int(*kernel)[3] = (kernel_toUse == 0) ? Gx : Gy;

	Mat VS = grey.clone();
	// Excludes INeighbour borders
	for (int i = INeighbour; i < grey.rows - INeighbour; i++)
		// Excludes INeighbour borders
		for (int j = INeighbour; j < grey.cols - INeighbour; j++) {
			int value = 0;
			for (int x = -1; x < 2; x++)
				for (int y = -1; y < 2; y++)
					value += grey.at<uchar>(i + x, j + y) * kernel[x + 1][y + 1];

			VS.at<uchar>(i, j) = value > TH ? 255 : 0;
		}

	return VS;
}

Mat Laplacian(Mat grey, int TH, int INeighbour)
{
	// Declare the kernel
	int kernel[3][3] = { {0, 1, 0}, {1, -4, 1}, {0, 1, 0} };

	Mat LapImg = grey.clone();
	// Excludes INeighbour borders
	for (int i = INeighbour; i < grey.rows - INeighbour; i++)
		// Excludes INeighbour borders
		for (int j = INeighbour; j < grey.cols - INeighbour; j++) {
			int value = 0;
			for (int x = -1; x < 2; x++)
				for (int y = -1; y < 2; y++)
					value += grey.at<uchar>(i + x, j + y) * kernel[x + 1][y + 1];

			LapImg.at<uchar>(i, j) = value > TH ? 255 : 0;
		}

	return LapImg;
}

Mat Avg_neighbour(Mat grey, int INeighbour)
{
	// Create a black grey scaled image
	Mat blurred = grey.clone();

	// Excludes INeighbour borders
	for (int i = INeighbour; i < grey.rows - INeighbour; i++)
		// Excludes INeighbour borders
		for (int j = INeighbour; j < grey.cols - INeighbour; j++) {
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
		probability[i] = (float)count[i] / img_size;

	// 3. Accumulative probability
	float acc_probability[256];
	acc_probability[0] = probability[0];
	for (int i = 1; i < 256; i++)
		acc_probability[i] = probability[i] + acc_probability[i - 1];

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