#include<iostream>
#include<opencv2/opencv.hpp>
#include<vector>
#include<string>
using namespace cv;
using namespace std;

 char imgpath[] = "Untitled 5.png";
 Mat img = imread(imgpath,IMREAD_COLOR);
 Mat kenel1 = getStructuringElement(MORPH_RECT, Size(15, 15));
 Mat kenel2 = getStructuringElement(MORPH_RECT, Size(5, 5));

vector<vector<Point>> findcontours(Scalar up,Scalar low)
{
   
    Mat img2,imgHSV;
    vector<vector<Point>> contours;
    vector<Vec4i> h;
    GaussianBlur(img,img2,Size(7,7),2,2);
    cvtColor(img2,imgHSV,COLOR_BGR2HSV);
    inRange(imgHSV,low,up,img2);
    morphologyEx(img2, img2, MORPH_OPEN, kenel1);
    morphologyEx(img2, img2, MORPH_CLOSE, kenel2);
    findContours(img2,contours,h,RETR_TREE,CHAIN_APPROX_NONE);
    return contours;
}

void drawcontour(vector<vector<Point>> contours,Scalar color,string tag)
{
    for (int i=0;i<contours.size();i++)
    {
        RotatedRect rect = minAreaRect(contours[i]);
        Point2f P[4];
        rect.points(P);
        for (int j = 0; j <= 3; j++)
        {
            line(img, P[j], P[(j + 1) % 4], color, 3);
        }
        Moments m = moments(contours[i]); 
        double cx = m.m10 / m.m00;
        double cy = m.m01 / m.m00;
        string cx_str = to_string((int)cx);
        string cy_str = to_string((int)cy);
        putText(img,("("+cx_str+","+cy_str+")"+tag),Point(cx,cy),FONT_HERSHEY_COMPLEX_SMALL,1,color,2);
        circle(img,Point(cx,cy),4,color,-1);
    }
}

int main()
{

    Scalar blue1_low = Scalar (100, 80, 70);
    Scalar blue1_up = Scalar (120, 255, 255);
    Scalar red2_low = Scalar (0, 170, 46);
    Scalar red2_up = Scalar (7, 255, 255);
    Scalar red1_low = Scalar (156, 43, 46);
    Scalar red1_up = Scalar (179, 255, 255);
    Scalar red = Scalar (0,0,255);
    Scalar blue = Scalar (255,0,0);
    vector<vector<Point>> red1_contours,red2_contours,blue1_contours;
    
    blue1_contours = findcontours(blue1_up,blue1_low);
    red2_contours = findcontours(red2_up,red2_low);
    kenel2 = getStructuringElement(MORPH_RECT, Size(10, 10));
    red1_contours = findcontours(red1_up,red1_low);

    drawcontour(red1_contours,blue,"red");
    drawcontour(red2_contours,blue,"red");
    drawcontour(blue1_contours,red,"blue");
   
    imshow("1",img);
    waitKey();
    
    return 0;
}