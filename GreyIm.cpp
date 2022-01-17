#include "highgui.h"
#include <imgproc\imgproc.hpp>
#include <iostream>
using namespace cv;
using namespace std;
int main(int argc, char** argv)
{
	Mat src = cv::imread("damcuoi.jpg", IMREAD_COLOR );
	if (src.empty())
	{
		cout << "Could not open or find the image!\n" <<endl;
		cout << "Usage: " << argv[0] << " <Input image>" <<endl;
		return -1;
	}
	cvtColor( src, src, COLOR_BGR2GRAY);
	Mat dst;
	cv::equalizeHist( src, dst );
	imshow( "Source image", src );
	imshow( "Equalized Image", dst );
	waitKey();
	return 0;
}