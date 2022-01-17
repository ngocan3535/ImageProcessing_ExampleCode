#include <iostream>
#include <string>
#include <opencv2\opencv.hpp>
#include <opencv2\highgui.hpp>
#include <opencv2\core.hpp>
#define MAX_KERNEL_LENGTH 11
using namespace std;
using namespace cv;

bool Loadanh(Mat &image,char *url)
{	
	if(!cvLoadImage(url,CV_LOAD_IMAGE_COLOR))
	{
		return false;
	}
	else
		image = cvLoadImage(url,CV_LOAD_IMAGE_COLOR);
}
void Hienanh(String name,Mat &image)
{	
	imshow(name,image);

}
void Blur(Mat &image)
{
		cv::Mat src = image;
        cv::Mat dst;
        for (int i = 1; i < MAX_KERNEL_LENGTH; i += 2)
        {
            cv::blur(src, dst, cv::Size(i, i), cv::Point(-1, -1));
        }
        Hienanh("Blur",dst);
}
void Gaus(Mat &image)
{
	   cv::Mat src = image;
       cv::Mat dst;
       for (int i = 1; i < MAX_KERNEL_LENGTH; i += 2)
       {
           cv::GaussianBlur(src, dst, cv::Size(i, i), 0, 0);
       }
       Hienanh("Gauss",dst);
}
void Median(Mat &image)
{
	   cv::Mat src = image;
       cv::Mat dst;
       for (int i = 1; i < MAX_KERNEL_LENGTH; i += 2)
       {
           cv::medianBlur(src, dst, i);
       }
       Hienanh("Median",dst);
}
void Bilateral(Mat &image)
{
	   cv::Mat src = image;
       cv::Mat dst;
       for (int i = 1; i < MAX_KERNEL_LENGTH; i += 2)
        {
            cv::bilateralFilter(src, dst, i, i * 2, i / 2);
        }
       Hienanh("Bilateral",dst);
}
void Choice(Mat image)
{
	int item;
	bool exit = true;
	cout<<"==========Menu=========="<<endl;
	cout<<"0. Anh goc"<<endl;
	cout<<"1. Blur"<<endl;
	cout<<"2. Gaus"<<endl;
	cout<<"3. Median"<<endl;
	cout<<"4. Bilateral"<<endl;
	cout<<"5. Exit"<<endl;
	cout<<"========================"<<endl;
	do {
	cout<<"Please Choice:";
	cin>>item;	
	switch(item)
	{
	case 0:
		Hienanh("anh_goc",image);
		break;
	case 1:
		Blur(image);
		break;
	case 2:
		Gaus(image);
		break;
	case 3:
		Median(image);
		break;
	case 4:
		Bilateral(image);
		break;
	default:
		exit = false;
		cout<<"Exit";
		break;		
	}
	cvWaitKey();
	}while(exit);
}
int main()
{
	Mat image;
	bool kiemTra = Loadanh(image,"duong_dan_anh.jpg");
	if(!kiemTra)
	{
		cout <<"Khong the mo file\n";
	}
	else
	{
		Choice(image);
	}
	system("pause");
	return 0;
}
