// do canh bien canny

#include <iostream>
#include <opencv2\core\core.hpp>
#include <opencv2\imgproc\imgproc.hpp>
#include <opencv2\highgui\highgui.hpp>

using namespace cv;
using namespace std;

void main(){

	Mat gray = cv::imread("Anh1.jpg", CV_LOAD_IMAGE_GRAYSCALE);

	if(gray.empty())
       std::cout << "failed to open img.jpg" << std::endl;
    else
       std::cout << "img.jpg loaded OK" << std::endl;
	Mat dst1, dst2;
	imshow("Anh xam", gray);
	GaussianBlur(gray, gray, Size(9,9), 2);
	double t1 = 30, t2 = 200;
	cv::Canny(gray, dst1, t1, t2, 3, false);
	t1 = 100; t2 = 120;
	cv::Canny(gray, dst2, t1, t2, 3, false);
	imshow("Bien trong anh voi nguong 1", dst1);
	imshow("Bien trong anh voi nguong 2", dst2);
	waitKey(0);
}
