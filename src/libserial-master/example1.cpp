
#include <SerialStream.h>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;
using namespace LibSerial;

main(){


SerialStream my_serial_stream;

my_serial_stream.Open( "/dev/ttyUSB0") ;
my_serial_stream.SetBaudRate( SerialStreamBuf::BAUD_9600 ) ;

while(true)
{

    std::string my_string = "123";

    my_serial_stream << my_string << std::flush ;
}
my_serial_stream.Close();

}