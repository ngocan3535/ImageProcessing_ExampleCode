// do canh bien sobel

#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
using namespace cv;
void main(){
	Mat gray = cv::imread("Anh1.jpg", CV_LOAD_IMAGE_GRAYSCALE);
	Mat dst1, dst2;
	imshow("Anh xam", gray);
	GaussianBlur(gray, gray, Size(9,9), 2);
	cv::Sobel(gray, dst1, gray.depth(), 1, 0, 3);
	cv::Sobel(gray, dst2, gray.depth(), 0, 1, 3);
	imshow("Bien trong anh voi nguong 1", dst1);
	imshow("Bien trong anh voi nguong 2", dst2);
	waitKey(0);
}