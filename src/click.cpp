Mat xyz;
setMouseCallback("cascade_image", onMouse, &xyz); // pass the address

static void onMouse(int event, int x, int y, int flags, void* param) // now it's in param
{
    Mat &xyz = *((Mat*)param); //cast and deref the param

    if (event == EVENT_LBUTTONDOWN)
    {
        short val = xyz.at< short >(y,x); // opencv is row-major ! 
        cout << "x= " << x << " y= " << y << "val= "<<val<< endl;
    }
}