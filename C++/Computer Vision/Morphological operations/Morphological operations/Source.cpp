#include <iostream>

#include "highgui/highgui.hpp"
#include "core/core.hpp"
#include "opencv.hpp"

// cv::
using namespace cv;

Mat RBGtoGrey(Mat RBG);
Mat EqualizeHistogram(Mat grey);
Mat Blur(Mat grey, int INeighbour = 1);
Mat Sobel(Mat grey, int kernel_toUse = 0, int TH = 50, int INeighbour = 1);
Mat Dilation(Mat grey, int INeighbour=1);
Mat Erosion(Mat grey, int INeighbour=1);

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
	Mat blurred = Blur(EQImg);
	// Vertical edge detection
	Mat verical_edge = Sobel(blurred);
	
	/* Opening */
	// Erode Image
	Mat erodedImg = Erosion(verical_edge);
	// Dilate the Eroded image
	imshow("morophogical opening mask", Dilation(erodedImg, 6));
	
	// Without this function the image will close immediately
	waitKey();
}

Mat Dilation(Mat grey, int INeighbour)
{
	Mat dilated = grey.clone();

	// Loop over the rows excluding the borders
	for (int i = INeighbour; i < grey.rows; i++)
		// Loop over the columns excluding the borders
		for (int j = INeighbour; j < grey.cols; j++)
		{
			// Focus on the black pixels
			if (grey.at<uchar>(i, j) == 0)
			{
				bool changed = false;
				for (int x = -INeighbour; x <= INeighbour; x++)
				{
					for (int y = -INeighbour; y <= INeighbour; y++)
						// If a neighbor is white
						if (grey.at<uchar>(i+x, j+y) == 255)
						{
							// Make the pixel white
							dilated.at<uchar>(i, j) = 255;
							changed = true;
							break;
						}
					// If the pixel is altered, stop iterating over the neighbors
					if (changed)
						break;
				}

			}
		}

	return dilated;
}

Mat Erosion(Mat grey, int INeighbour)
{
	Mat eroded = grey.clone();

	// Loop over the rows excluding the borders
	for (int i = INeighbour; i < grey.rows; i++)
		// Loop over the columns excluding the borders
		for (int j = INeighbour; j < grey.cols; j++)
		{
			// Focus on the white pixels
			if (grey.at<uchar>(i, j) == 255)
			{
				bool changed = false;
				for (int x = -INeighbour; x <= INeighbour; x++)
				{
					for (int y = -INeighbour; y <= INeighbour; y++)
						// If a neighbor is black
						if (grey.at<uchar>(i + x, j + y) == 0)
						{
							// Make the pixel black
							eroded.at<uchar>(i, j) = 0;
							changed = true;
							break;
						}
					// If the pixel is altered, stop iterating over the neighbors
					if (changed)
						break;
				}

			}
		}

	return eroded;
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

Mat Blur(Mat grey, int INeighbour)
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