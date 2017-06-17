/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#import "main.h"

int fd;

void setup(){
    
    
  if ((fd = serialOpen ("/dev/ttyAMA0", 38400)) < 0)
  {
    fprintf (stderr, "Unable to open serial device: %s\n", strerror (errno)) ;
    return 1 ;
  }

  if (wiringPiSetupGpio () == -1)
  {
    fprintf (stdout, "Unable to start wiringPi: %s\n", strerror (errno)) ;
    return 1 ;
  }
    
}

void sendByte (){
    serialPutchar (fd, 0xAD) ;
}

int getChar (){
    if (serialDataAvail (fd))
    {
      return serialGetchar (fd);
    }
}



int getFG(){
    return fb;
}
