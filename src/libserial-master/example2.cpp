
#include <SerialStream.h>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;
using namespace LibSerial;

int main(){


SerialStream my_serial_stream;

my_serial_stream.Open( "/dev/ttyUSB0") ;
my_serial_stream.SetBaudRate( SerialStreamBuf::BAUD_9600 ) ;

my_serial_stream.SetVTime(1);
my_serial_stream.SetVMin(0);

while (true)
{
    char c = 'x';
    my_serial_stream >> c;
    std::cout << c << std::endl;
    if (c == '?') std::cout << "hahaha got it!" << std::endl;
}


my_serial_stream.Close();
return 0;
}
